# Contributing to Latex AI Workflow 🤝

Thank you for your interest in contributing to **Latex AI Workflow**! We welcome template contributions, bug fixes, CLI enhancements, and documentation improvements.

---

## 📋 Ground Rules & Guidelines

1. **Keep Templates Modular**: All new LaTeX templates should be placed in `templates/<template_name>/` and must compile cleanly with `latexmk` under standard TeX Live without missing dependencies.
2. **Scalable Fonts**: Always include `\usepackage{lmodern}` or another scalable Type 1 / OpenType font package to guarantee compatibility with `\usepackage{microtype}`.
3. **No Auxiliary Build Files**: Ensure your PR does not commit auxiliary artifacts (`.aux`, `.log`, `.synctex.gz`, `.fls`, `.fdb_latexmk`).
4. **Visual Inspection**: Run `python scripts/latex_workflow.py inspect <path_to_tex>` to verify that page balances, margins, and tables are visually clean and generate crisp preview images.

---

## 🛠️ Development Workflow

1. **Fork & Clone**
   ```bash
   git clone https://github.com/Divyansh0730/Latex-AI-Workflow.git
   cd Latex-AI-Workflow
   ```

2. **Set up WSL2 Environment**
   ```powershell
   wsl -d Ubuntu-22.04 bash -c "cd scripts && chmod +x setup_wsl.sh && ./setup_wsl.sh"
   ```

3. **Create a Feature Branch**
   ```bash
   git checkout -b feature/my-new-template
   ```

4. **Verify All Builds Locally**
   ```powershell
   python scripts/latex_workflow.py inspect templates/technical_specification/main.tex
   python scripts/latex_workflow.py inspect templates/academic_paper/main.tex
   python scripts/latex_workflow.py inspect templates/executive_report/main.tex
   ```

5. **Commit & Open Pull Request**
   Use descriptive commit messages following the [Conventional Commits](https://www.conventionalcommits.org/) specification:
   - `feat: add IEEE transaction template`
   - `fix: resolve table overflow in executive report`
   - `docs: update CLI guide and keybindings`

---

## 💬 Questions or Help?
Open an issue on the [GitHub Issues](https://github.com/Divyansh0730/Latex-AI-Workflow/issues) tab!
