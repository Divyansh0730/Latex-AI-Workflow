#!/usr/bin/env bash
# ==============================================================================
# LaTeX AI Workflow - Universal Environment Installer (Cross-Platform)
# Installs TeX Live, latexmk, poppler-utils, and toolchains across all platforms
# ==============================================================================

set -e

# Detect if sudo is needed and available
SUDO=""
if [ "$(id -u)" -ne 0 ]; then
    if command -v sudo &> /dev/null; then
        SUDO="sudo"
    else
        echo "⚠️ Running as non-root without 'sudo'. Package installations may require elevated privileges."
    fi
fi

echo "🚀 [Latex AI Workflow] Detecting host platform..."

# Detect macOS
if [ "$(uname)" == "Darwin" ]; then
    echo "🍎 Detected macOS. Installing via Homebrew..."
    if ! command -v brew &> /dev/null; then
        echo "❌ Homebrew not found. Please install Homebrew from https://brew.sh first."
        exit 1
    fi
    brew install --cask mactex-no-gui || brew install basictex
    brew install poppler latexmk
    echo "✅ macOS environment setup complete!"

# Detect Termux / Android
elif command -v pkg &> /dev/null && ([ -d /data/data/com.termux ] || [ -n "$TERMUX_VERSION" ]); then
    echo "📱 Detected Termux / Android environment. Installing via pkg..."
    pkg update -y
    pkg install -y texlive-bin poppler python git
    echo "✅ Termux environment setup complete!"

# Detect Debian / Ubuntu / Mint / WSL2
elif [ -f /etc/debian_version ] || [ -f /etc/lsb-release ] || command -v apt-get &> /dev/null; then
    echo "🐧 Detected Debian / Ubuntu / WSL2 Linux. Installing via apt..."
    $SUDO apt-get update -y
    $SUDO apt-get install -y \
        texlive-latex-base \
        texlive-latex-extra \
        texlive-fonts-recommended \
        texlive-fonts-extra \
        texlive-science \
        latexmk \
        poppler-utils \
        python3 \
        python3-pip \
        git
    echo "✅ Debian/Ubuntu/WSL2 environment setup complete!"

# Detect Fedora / RHEL / CentOS / Rocky
elif [ -f /etc/fedora-release ] || [ -f /etc/redhat-release ] || command -v dnf &> /dev/null; then
    echo "🎩 Detected Fedora / RedHat. Installing via dnf..."
    $SUDO dnf install -y texlive-scheme-medium latexmk poppler-utils python3 python3-pip git
    echo "✅ Fedora environment setup complete!"

# Detect Arch Linux / Manjaro
elif [ -f /etc/arch-release ] || command -v pacman &> /dev/null; then
    echo "🏹 Detected Arch Linux. Installing via pacman..."
    $SUDO pacman -Sy --noconfirm texlive-most poppler python python-pip git
    echo "✅ Arch Linux environment setup complete!"

# Detect openSUSE
elif [ -f /etc/os-release ] && grep -qi "opensuse" /etc/os-release; then
    echo "🦎 Detected openSUSE. Installing via zypper..."
    $SUDO zypper install -y texlive-scheme-medium latexmk poppler-tools python3 python3-pip git
    echo "✅ openSUSE environment setup complete!"

# Detect Alpine Linux
elif [ -f /etc/alpine-release ] || command -v apk &> /dev/null; then
    echo "🏔️ Detected Alpine Linux. Installing via apk..."
    $SUDO apk add --no-cache texlive-full poppler-utils python3 py3-pip git
    echo "✅ Alpine Linux environment setup complete!"

else
    echo "⚠️ Unknown OS distribution. Please ensure 'latexmk', 'pdflatex', 'pdftoppm' (poppler), and 'python3' are installed."
fi

echo ""
# Run doctor check
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if [ -f "$SCRIPT_DIR/latex_workflow.py" ]; then
    python3 "$SCRIPT_DIR/latex_workflow.py" doctor || true
fi

echo "🎉 TeX Live compilation engine is ready to use!"
echo "   Run 'python3 scripts/latex_workflow.py list' to explore all document templates."
echo "   Run 'python3 scripts/latex_workflow.py init modern_resume my_resume' to scaffold a project."
