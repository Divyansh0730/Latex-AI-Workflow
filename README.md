<div align="center">

# 🚀 Latex AI Workflow
### Local, AI-Augmented, Publication-Grade LaTeX Development Environment
**An Overleaf-Equivalent (and Beyond) Local LaTeX Stack for Antigravity IDE & VS Code**

[![Build & Verify](https://github.com/Divyansh0730/Latex-AI-Workflow/actions/workflows/compile-latex.yml/badge.svg)](https://github.com/Divyansh0730/Latex-AI-Workflow/actions/workflows/compile-latex.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](LICENSE)
[![Engine: TeX Live](https://img.shields.io/badge/TeX_Live-2023%2B-green.svg?style=flat-square&logo=latex)](https://www.tug.org/texlive/)
[![Platform: WSL2 / Linux](https://img.shields.io/badge/Platform-WSL2%20%7C%20Linux-orange.svg?style=flat-square&logo=ubuntu)](https://ubuntu.com/wsl)
[![IDE: Antigravity / VS Code](https://img.shields.io/badge/Editor-Antigravity%20%2F%20VS%20Code-purple.svg?style=flat-square&logo=visualstudiocode)](https://code.visualstudio.com/)
[![Python: 3.9+](https://img.shields.io/badge/Python-3.9%2B-yellow.svg?style=flat-square&logo=python)](https://python.org)

<p align="center">
  <a href="#-core-features">Features</a> •
  <a href="#-template-showcase-gallery">Template Gallery</a> •
  <a href="#-quick-start-30-second-setup">Quick Start</a> •
  <a href="#-in-editor-workflow--shortcuts">Editor Guide</a> •
  <a href="#-master-cli-engine">CLI Engine</a> •
  <a href="#-ai-prompt-playbook">AI Playbook</a> •
  <a href="#-overleaf-vs-latex-ai-workflow">Comparison</a>
</p>

</div>

---

## 🌟 Core Features

- ⚡ **Zero Cloud Bottlenecks**: Compile unlimited, publication-length documents locally with zero timeouts, zero server queueing, and 100% offline capability.
- 🔄 **Instant Side-by-Side Live Preview**: Auto-compiles on save (`Ctrl + S`) with sub-second reload and bidirectional SyncTeX navigation (`Ctrl + Alt + J` / `Ctrl + Click`).
- 🤖 **Agentic AI Layout Inspection**: Automatically renders high-DPI page images (`pdftoppm`) so AI assistants and humans can visually audit table overflows, typography balance, and margin symmetry.
- 📦 **Turn-Key Production Templates**: Pre-configured, publication-ready templates for **Engineering Technical Specs**, **IEEE/ACM Academic Papers**, and **Executive Reports**.
- 🛠️ **Unified Automation CLI**: Single master Python CLI (`scripts/latex_workflow.py`) for scaffolding projects, compiling, log diagnosis, and visual page extraction.
- 🚀 **GitHub Actions CI/CD**: Pre-configured CI workflow that compiles all templates on push/PR and uploads production PDFs as downloadable build artifacts.

---

## 🏗️ Architecture & Workflow

```mermaid
flowchart TD
    subgraph Editor ["🖥️ Antigravity IDE / VS Code"]
        TEX["📝 LaTeX Source (.tex)"]
        SYNC["📍 Bidirectional SyncTeX"]
        PREV["📄 Live PDF Viewer Tab"]
    end

    subgraph Engine ["⚡ Local TeX Live Engine (WSL2 / Linux)"]
        MK["⚙️ latexmk / pdflatex"]
        PPM["🖼️ pdftoppm (High-DPI Render)"]
    end

    subgraph Automation ["🤖 AI Assistant & Automation CLI"]
        CLI["🛠️ scripts/latex_workflow.py"]
        QA["🔍 Visual Page QA"]
        CI["🚀 GitHub Actions CI Pipeline"]
    end

    TEX -->|"Ctrl + S (Auto-Build)"| MK
    MK -->|"Instant Output"| PREV
    PREV <-->|"SyncTeX Jump"| TEX
    MK -->|"Inspect Command"| PPM
    PPM -->|"Extract Pages"| QA
    QA -->|"Prompt Feedback"| TEX
    TEX -->|"Push to GitHub"| CI
```

---

## 🎨 Template Showcase Gallery

| Template | Preview | Description & Scaffolding |
| :--- | :---: | :--- |
| **Technical Specification**<br/>`templates/technical_specification/` | <img src="assets/preview_tech_spec.png" width="220" alt="Technical Specification Preview"/> | Industrial engineering specs, ICDs, hardware/software telemetry tables, and code syntax listings.<br/><br/>`python scripts/latex_workflow.py init technical_specification my_spec` |
| **Academic Paper**<br/>`templates/academic_paper/` | <img src="assets/preview_academic_paper.png" width="220" alt="Academic Paper Preview"/> | IEEE / ACM 2-column format with bibliography references (`references.bib`), abstracts, and mathematical proofs.<br/><br/>`python scripts/latex_workflow.py init academic_paper my_paper` |
| **Executive Report**<br/>`templates/executive_report/` | <img src="assets/preview_executive_report.png" width="220" alt="Executive Report Preview"/> | Modern corporate whitepapers, KPI metric tables, and stylized callout boxes.<br/><br/>`python scripts/latex_workflow.py init executive_report my_report` |

---

## ⚡ Quick Start (30-Second Setup)

### 1. Prerequisites
- **Windows 10 / 11** with **WSL2** (`wsl --install -d Ubuntu-22.04`) or **Native Linux / macOS**.
- **Antigravity IDE** or **VS Code** with the `LaTeX Workshop` extension installed.

### 2. Automated WSL Environment Setup
Open PowerShell and run the one-line setup script:
```powershell
wsl -d Ubuntu-22.04 bash -c "cd '/mnt/e/Internship Material/Latex AI Workflow/scripts' && chmod +x setup_wsl.sh && ./setup_wsl.sh"
```
*This installs `texlive-latex-base`, `texlive-latex-extra`, `latexmk`, `poppler-utils`, and required font packages.*

---

## 🖥️ In-Editor Workflow & Shortcuts

Open the repository in **Antigravity IDE** or **VS Code**:

| Shortcut | Action | Description |
| :--- | :--- | :--- |
| **`Ctrl + Alt + V`** | **Open Live Preview** | Opens the rendered PDF side-by-side in an integrated tab. |
| **`Ctrl + S`** | **Save & Auto-Compile** | Compiles via WSL2 `latexmk` and refreshes the PDF in ~1 second. |
| **`Ctrl + Alt + J`** | **Source $\to$ PDF Jump** | Jumps directly to the corresponding paragraph in the PDF. |
| **`Ctrl + Click`** | **PDF $\to$ Source Jump** | Click any word in the PDF tab to jump to that exact line in `.tex`. |

---

## 🛠️ Master CLI Engine (`scripts/latex_workflow.py`)

A standalone CLI utility for end-to-end automation:

### 1. Compile a Document
```bash
python scripts/latex_workflow.py build templates/technical_specification/main.tex
```

### 2. Inspect PDF Layout (Visual PNG Extraction)
```bash
python scripts/latex_workflow.py inspect templates/academic_paper/main.tex --dpi 150
```
*Compiles the document and extracts `previews/page-1.png`, `previews/page-2.png`, etc., for visual inspection.*

### 3. Initialize a New Project from Template
```bash
python scripts/latex_workflow.py init technical_specification projects/robot_odometry_spec
```

### 4. Clean Auxiliary Build Artifacts
```bash
python scripts/latex_workflow.py clean projects/robot_odometry_spec
```

---

## 🤖 AI Prompt Playbook

Pair this environment with **Antigravity AI** or any LLM assistant to write and refine documents at 10x speed:

### 📐 1. Kinematic & Mathematical Formulations
> *"Draft a 6-DoF rigid body kinematics section in LaTeX. Include differential wheel odometry equations, a state vector definition, and an equation for spatial alignment cost using amsmath environments."*

### 📊 2. Engineering Telemetry & Spec Tables
> *"Create a responsive tabularx table for our drone telemetry specification. Include columns for Topic Name, Message Type, Frequency (Hz), Transport Protocol, and Description with professional booktabs styling."*

### 🔍 3. Visual Layout & Typography Audit
> *"Run visual inspection on `main.tex`. Inspect the generated page PNGs in `previews/` and fix any table overflows, margin overlaps, or awkward page breaks."*

### 📝 4. Markdown / Notes to Academic LaTeX
> *"Convert my engineering notes in `notes.md` into a formal 2-column IEEE academic paper in `templates/academic_paper/main.tex` with references."*

---

## 📊 Overleaf vs. Latex AI Workflow

| Feature | Overleaf (Free / Pro) | Latex AI Workflow |
| :--- | :---: | :---: |
| **Engine** | Cloud TeX Live | **Official Local TeX Live (WSL2)** |
| **Compilation Speed** | Queued on cloud servers | **Instant (~1s local compilation)** |
| **File / Compile Limits** | Strict timeout limits | **Unlimited (Compile entire books/theses)** |
| **Internet Requirement** | ❌ Required 100% of the time | **✅ 100% Offline Capability** |
| **AI Integration** | Basic autocomplete | **Full Agentic AI (Code, Debug, Visual Layout QA)** |
| **SyncTeX Navigation** | ✅ Yes | **✅ Yes (`Ctrl + Alt + J` / `Ctrl + Click`)** |
| **Codebase Integration** | ❌ Isolated in web browser | **✅ Direct access to Git, ROS 2, Python, CAD** |
| **Cost** | Free tier / \$15-\$30/mo | **100% Free & Open Source (MIT)** |

---

## 📁 Repository Structure

```text
Latex-AI-Workflow/
├── .github/
│   ├── workflows/compile-latex.yml  # Automated CI/CD GitHub Action
│   └── ISSUE_TEMPLATE/              # Issue and PR templates
├── .vscode/
│   ├── settings.json                # Pre-configured WSL latexmk recipes
│   └── tasks.json                   # Build and clean tasks
├── assets/                          # Showcase preview images
├── examples/
│   └── robotics_technical_spec/     # Complete working demo specification
├── scripts/
│   ├── latex_workflow.py            # Master CLI engine (build, inspect, init, clean)
│   ├── setup_wsl.sh                 # 1-click WSL environment installer
│   └── build.ps1                    # PowerShell build helper
├── templates/
│   ├── technical_specification/     # Industrial engineering spec template
│   ├── academic_paper/              # IEEE/ACM 2-column research paper template
│   └── executive_report/            # Corporate whitepaper / KPI report template
├── CONTRIBUTING.md                  # Contribution guidelines
├── LICENSE                          # MIT License
└── README.md                        # Documentation & Playbook
```

---

## 🤝 Contributing

Contributions, bug reports, and new LaTeX templates are warmly welcomed! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details on code style and testing.

---

## 📜 License

This project is open-source software licensed under the **[MIT License](LICENSE)**.

Developed with ❤️ by **[Divyansh Jha](https://github.com/Divyansh0730)**.
