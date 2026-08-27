#!/usr/bin/env bash
# ==============================================================================
# Latex AI Workflow - WSL2 TeX Live & Toolchain Installer
# Compatible with Ubuntu 20.04 / 22.04 / 24.04 in WSL2
# ==============================================================================

set -e

echo "[+] Updating Ubuntu package repositories..."
sudo apt-get update -y

echo "[+] Installing official TeX Live compiler suite & utilities..."
sudo apt-get install -y \
    texlive-latex-base \
    texlive-latex-extra \
    texlive-fonts-recommended \
    texlive-science \
    latexmk \
    poppler-utils \
    ghostscript

echo "[+] Verifying installations:"
echo "    - pdflatex : $(pdflatex --version | head -n 1)"
echo "    - latexmk  : $(latexmk --version | head -n 1)"
echo "    - pdftoppm : $(pdftoppm -v 2>&1 | head -n 1)"

echo ""
echo "[✓] Environment Setup Complete! You can now compile and visually inspect LaTeX documents."
