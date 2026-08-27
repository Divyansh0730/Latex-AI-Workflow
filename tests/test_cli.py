import unittest
import subprocess
import sys
import shutil
import tempfile
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

class TestLatexWorkflowCLI(unittest.TestCase):
    def test_cli_version(self):
        res = subprocess.run([sys.executable, "scripts/latex_workflow.py", "--version"], cwd=ROOT_DIR, capture_output=True, text=True)
        self.assertEqual(res.returncode, 0)
        self.assertIn("latex-workflow v", res.stdout)

    def test_cli_list(self):
        res = subprocess.run([sys.executable, "scripts/latex_workflow.py", "list"], cwd=ROOT_DIR, capture_output=True, text=True)
        self.assertEqual(res.returncode, 0)
        self.assertIn("modern_resume", res.stdout)
        self.assertIn("academic_paper", res.stdout)
        self.assertIn("academic_thesis", res.stdout)

    def test_cli_doctor(self):
        res = subprocess.run([sys.executable, "scripts/latex_workflow.py", "doctor"], cwd=ROOT_DIR, capture_output=True, text=True)
        self.assertIn("Latex AI Workflow - Environment Doctor", res.stdout)

    def test_cli_init_clean_isolation(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            dest = Path(tmp_dir) / "test_project"
            res = subprocess.run([sys.executable, "scripts/latex_workflow.py", "init", "modern_resume", str(dest)], cwd=ROOT_DIR, capture_output=True, text=True)
            self.assertEqual(res.returncode, 0)
            self.assertTrue((dest / "main.tex").exists())
            # Ensure no auxiliary build files or PDFs leaked into initial scaffold
            self.assertFalse((dest / "main.pdf").exists())
            self.assertFalse((dest / "main.aux").exists())
            self.assertFalse((dest / "main.log").exists())
            self.assertFalse((dest / "main.synctex.gz").exists())

if __name__ == "__main__":
    unittest.main()
