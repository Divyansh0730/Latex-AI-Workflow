#!/usr/bin/env python3
"""
==============================================================================
Latex AI Workflow - Universal Master CLI Engine
Cross-platform LaTeX compilation, visual layout inspection (PNG rendering),
log analysis, and template scaffolding for Linux, macOS, and Windows (WSL2/Native).
==============================================================================
"""

import sys
import os
import argparse
import subprocess
import shutil
from pathlib import Path

# Ensure UTF-8 output on Windows terminals
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

DEFAULT_WSL_DISTRO = "Ubuntu-22.04"

def is_native_latex_available() -> bool:
    """Check if latexmk is available directly on the system PATH."""
    return shutil.which("latexmk") is not None

def to_wsl_path(win_path: Path) -> str:
    """Convert a Windows Path to a WSL /mnt/... path dynamically."""
    abs_path = win_path.resolve()
    drive = abs_path.drive.rstrip(':').lower()
    path_without_drive = str(abs_path)[2:].replace('\\', '/')
    return f"/mnt/{drive}{path_without_drive}"

def execute_engine_command(cmd_args: list, cwd: Path, distro: str = DEFAULT_WSL_DISTRO) -> subprocess.CompletedProcess:
    """Execute a command either natively or inside WSL2 based on environment."""
    if is_native_latex_available() or sys.platform != "win32":
        return subprocess.run(cmd_args, cwd=cwd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    else:
        # Fallback to WSL2 on Windows
        wsl_cwd = to_wsl_path(cwd)
        flat_cmd = " ".join(f'"{arg}"' if " " in arg or "*" in arg else arg for arg in cmd_args)
        full_cmd = ["wsl", "-d", distro, "bash", "-c", f"cd \"{wsl_cwd}\" && {flat_cmd}"]
        return subprocess.run(full_cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")

def cmd_build(args):
    """Compile a LaTeX document using latexmk."""
    tex_path = Path(args.tex_file).resolve()
    if not tex_path.exists():
        print(f"[Error] File not found: {tex_path}")
        return 1

    work_dir = tex_path.parent
    file_name = tex_path.name

    engine_name = "Native System" if (is_native_latex_available() or sys.platform != "win32") else f"WSL2 ({args.distro})"
    print(f"[+] Compiling '{file_name}' using {engine_name}...")

    cmd = ["latexmk", "-synctex=1", "-interaction=nonstopmode", "-file-line-error", "-pdf", file_name]
    result = execute_engine_command(cmd, cwd=work_dir, distro=args.distro)

    if result.returncode == 0:
        pdf_path = work_dir / f"{tex_path.stem}.pdf"
        print(f"[OK] Build Successful!")
        print(f"     Output PDF: {pdf_path}")
        return 0
    else:
        print(f"[FAIL] Build Failed with code {result.returncode}!")
        log_path = work_dir / f"{tex_path.stem}.log"
        if log_path.exists():
            print(f"[!] Analyzing error log ({log_path.name}):")
            analyze_log_errors(log_path)
        else:
            print(result.stdout[-1500:])
        return 1

def cmd_inspect(args):
    """Compile and convert all PDF pages into high-resolution PNGs for visual review."""
    tex_path = Path(args.tex_file).resolve()
    if not tex_path.exists():
        print(f"[Error] File not found: {tex_path}")
        return 1

    build_ret = cmd_build(args)
    if build_ret != 0:
        return build_ret

    work_dir = tex_path.parent
    pdf_stem = tex_path.stem
    preview_dir = work_dir / "previews"
    preview_dir.mkdir(exist_ok=True)

    print(f"[+] Rendering PDF pages to PNG (DPI: {args.dpi}) into 'previews/'...")

    if is_native_latex_available() or sys.platform != "win32":
        # Remove old previews
        for old_png in preview_dir.glob("page-*.png"):
            try:
                old_png.unlink()
            except Exception:
                pass
        cmd = ["pdftoppm", "-png", "-r", str(args.dpi), f"{pdf_stem}.pdf", str(preview_dir / "page")]
        res = subprocess.run(cmd, cwd=work_dir, capture_output=True, text=True, encoding="utf-8", errors="replace")
    else:
        wsl_work_dir = to_wsl_path(work_dir)
        wsl_preview_dir = to_wsl_path(preview_dir)
        wsl_cmd = ["bash", "-c", f"rm -f \"{wsl_preview_dir}\"/page-*.png && pdftoppm -png -r {args.dpi} \"{pdf_stem}.pdf\" \"{wsl_preview_dir}/page\""]
        res = subprocess.run(["wsl", "-d", args.distro] + wsl_cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")

    if res.returncode != 0:
        print(f"[Error] Failed to render images: {res.stderr}")
        return 1

    generated_pages = sorted(list(preview_dir.glob("page-*.png")))
    print(f"[OK] Successfully generated {len(generated_pages)} page image(s):")
    for page in generated_pages:
        print(f"     - {page}")

    return 0

def analyze_log_errors(log_path: Path):
    """Parse LaTeX log files for critical syntax errors and warnings."""
    try:
        content = log_path.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        print(f"Could not read log file: {e}")
        return

    error_lines = [line for line in content.splitlines() if line.startswith("!") or "Error" in line]
    if error_lines:
        print("\n--- Critical Errors ---")
        for err in error_lines[:10]:
            print(f"  {err}")

    overfull_boxes = [line for line in content.splitlines() if "Overfull \\hbox" in line]
    if overfull_boxes:
        print(f"\n--- Layout Warnings: {len(overfull_boxes)} Overfull \\hbox detected ---")
        for box in overfull_boxes[:5]:
            print(f"  {box}")

def cmd_clean(args):
    """Remove LaTeX auxiliary artifacts."""
    target_dir = Path(args.target_dir).resolve()
    extensions = [".aux", ".log", ".out", ".toc", ".synctex.gz", ".fls", ".fdb_latexmk", ".bbl", ".blg", ".nav", ".snm", ".vrb"]
    
    removed_count = 0
    for ext in extensions:
        for f in target_dir.glob(f"*{ext}"):
            try:
                f.unlink()
                removed_count += 1
            except Exception:
                pass
            
    print(f"[OK] Cleaned {removed_count} auxiliary file(s) in '{target_dir}'.")
    return 0

def cmd_init(args):
    """Scaffold a new LaTeX project from a template."""
    template_name = args.template
    target_dir = Path(args.dest_dir).resolve()
    
    root_dir = Path(__file__).resolve().parent.parent
    template_src = root_dir / "templates" / template_name
    
    available_templates = [d.name for d in (root_dir / "templates").iterdir() if d.is_dir()]
    
    if not template_src.exists():
        print(f"[Error] Template '{template_name}' not found. Available templates: {available_templates}")
        return 1
        
    target_dir.mkdir(parents=True, exist_ok=True)
    for item in template_src.iterdir():
        if item.is_file():
            shutil.copy2(item, target_dir / item.name)
            
    print(f"[OK] Initialized new LaTeX project from template '{template_name}' at:")
    print(f"     {target_dir}")
    return 0

def cmd_list(args):
    """List all available built-in templates."""
    root_dir = Path(__file__).resolve().parent.parent
    templates_dir = root_dir / "templates"
    if not templates_dir.exists():
        print("No templates directory found.")
        return 1
    
    print("\n📚 Available Document Templates:")
    print("--------------------------------------------------")
    for t_dir in sorted(templates_dir.iterdir()):
        if t_dir.is_dir():
            has_tex = (t_dir / "main.tex").exists()
            status = "✅ Ready" if has_tex else "⚠️ Missing main.tex"
            print(f" • {t_dir.name:<25} {status}")
    print("--------------------------------------------------\n")
    return 0

def main():
    parser = argparse.ArgumentParser(description="Latex AI Workflow - Universal Master CLI Engine")
    parser.add_argument("--distro", default=DEFAULT_WSL_DISTRO, help="WSL2 distribution name (Windows only)")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # build
    p_build = subparsers.add_parser("build", help="Compile a LaTeX document")
    p_build.add_argument("tex_file", help="Path to the .tex file")

    # inspect
    p_inspect = subparsers.add_parser("inspect", help="Compile and render pages to PNG for visual inspection")
    p_inspect.add_argument("tex_file", help="Path to the .tex file")
    p_inspect.add_argument("--dpi", type=int, default=150, help="Image DPI (default: 150)")

    # clean
    p_clean = subparsers.add_parser("clean", help="Clean auxiliary files")
    p_clean.add_argument("target_dir", nargs="?", default=".", help="Target directory")

    # init
    p_init = subparsers.add_parser("init", help="Initialize project from template")
    p_init.add_argument("template", help="Template name (e.g. modern_resume, academic_paper, academic_thesis, beamer_presentation, technical_specification, executive_report)")
    p_init.add_argument("dest_dir", help="Destination folder")

    # list
    subparsers.add_parser("list", help="List all available templates")

    args = parser.parse_args()

    if args.command == "build":
        sys.exit(cmd_build(args))
    elif args.command == "inspect":
        sys.exit(cmd_inspect(args))
    elif args.command == "clean":
        sys.exit(cmd_clean(args))
    elif args.command == "init":
        sys.exit(cmd_init(args))
    elif args.command == "list":
        sys.exit(cmd_list(args))

if __name__ == "__main__":
    main()
