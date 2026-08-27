# Changelog

All notable changes to **Latex AI Workflow** will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.1.0] - 2026-08-27

### Added
- **`latex-workflow doctor` Diagnostic Command**: Automatically tests local TeX Live, `latexmk`, `pdflatex`, `pdftoppm`, Python runtime, and provides exact platform-specific remediation commands.
- **Universal Multi-Platform Installer (`scripts/setup.sh`)**: Added automated support for Debian/Ubuntu, macOS (Homebrew), Fedora/RHEL, Arch Linux, openSUSE, Alpine Linux, and Termux/Android.
- **Python Package Support (`pyproject.toml`)**: Allows installing `latex-workflow` as a global or virtualenv CLI command via `pip install -e .`.
- **Developer `Makefile`**: Added targets for `make setup`, `make doctor`, `make list`, `make clean`, `make build`, and `make test`.
- **Semantic Versioning & CLI Version Flag**: Added `-v` / `--version` flag reporting `latex-workflow v1.1.0`.

### Changed
- Refactored example documents to use open-source lab naming (`Autonomous Systems Lab`) in place of proprietary affiliations.
- Enhanced CLI terminal output with colored formatting and clear status indicators.

---

## [1.0.0] - 2026-08-26

### Added
- **Master CLI Engine (`scripts/latex_workflow.py`)**: Unified cross-platform builder supporting `build`, `inspect` (PNG extraction), `init`, `clean`, and `list`.
- **Production Template Suite**:
  - `modern_resume`: 1-Page ATS-compliant software/engineering resume.
  - `academic_paper`: IEEE / ACM 2-column paper with BibTeX citation database.
  - `academic_thesis`: Master / PhD thesis book format with complete chapter structure.
  - `beamer_presentation`: Modern 16:9 conference slide deck.
  - `technical_specification`: Industrial RFC / ICD specification format.
  - `executive_report`: Corporate whitepaper & executive KPI briefing.
- **Visual Layout Inspection**: High-DPI page rendering to `previews/` for AI layout QA.
- **GitHub Actions CI Pipeline**: Automated multi-template compilation matrix verification.
- **1-Click DevContainer**: Complete ready-to-code cloud container for VS Code & GitHub Codespaces.
