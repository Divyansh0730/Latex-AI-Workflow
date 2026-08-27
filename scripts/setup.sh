#!/usr/bin/env bash
# ==============================================================================
# LaTeX AI Workflow - Universal Environment Installer (Cross-Platform)
# Installs TeX Live, latexmk, poppler-utils, and required fonts on Linux / WSL / macOS
# ==============================================================================

set -e

echo "🚀 [Latex AI Workflow] Detecting host platform..."

# Detect OS
if [ "$(uname)" == "Darwin" ]; then
    echo "🍎 Detected macOS. Installing via Homebrew..."
    if ! command -v brew &> /dev/null; then
        echo "❌ Homebrew not found. Please install Homebrew from https://brew.sh first."
        exit 1
    fi
    brew install --cask mactex-no-gui || brew install basictex
    brew install poppler latexmk
    echo "✅ macOS environment setup complete!"

elif [ -f /etc/debian_version ] || [ -f /etc/lsb-release ]; then
    echo "🐧 Detected Debian / Ubuntu / WSL2 Linux. Installing via apt..."
    sudo apt update
    sudo apt install -y \
        texlive-latex-base \
        texlive-latex-extra \
        texlive-fonts-recommended \
        texlive-fonts-extra \
        texlive-science \
        latexmk \
        poppler-utils \
        python3 \
        python3-pip
    echo "✅ Debian/Ubuntu/WSL2 environment setup complete!"

elif [ -f /etc/fedora-release ] || [ -f /etc/redhat-release ]; then
    echo "🎩 Detected Fedora / RedHat. Installing via dnf..."
    sudo dnf install -y texlive-scheme-medium latexmk poppler-utils python3 python3-pip
    echo "✅ Fedora environment setup complete!"

elif [ -f /etc/arch-release ]; then
    echo "🏹 Detected Arch Linux. Installing via pacman..."
    sudo pacman -Sy --noconfirm texlive-most poppler python python-pip
    echo "✅ Arch Linux environment setup complete!"

else
    echo "⚠️ Unknown OS distribution. Please ensure 'latexmk' and 'pdftoppm' (poppler-utils) are installed."
fi

echo ""
echo "🎉 TeX Live compilation engine is ready to use!"
echo "   Run 'python scripts/latex_workflow.py list' to explore all document templates."
