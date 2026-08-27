# Latex AI Workflow - Developer Makefile
.PHONY: help setup doctor list clean install

PYTHON ?= python3
CLI = $(PYTHON) scripts/latex_workflow.py

help:
	@echo "Available commands:"
	@echo "  make setup    - Install all TeX Live & rendering dependencies for your OS"
	@echo "  make doctor   - Diagnose local TeX and rendering toolchains"
	@echo "  make list     - List all available built-in document templates"
	@echo "  make install  - Install latex-workflow CLI globally via pip"
	@echo "  make clean    - Clean auxiliary build artifacts in current directory"

setup:
	@chmod +x scripts/setup.sh
	@./scripts/setup.sh

doctor:
	@$(CLI) doctor

list:
	@$(CLI) list

install:
	@pip install -e .

clean:
	@$(CLI) clean .
