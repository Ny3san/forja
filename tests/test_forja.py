import subprocess, sys, pathlib, unittest, tempfile, os, re
R = pathlib.Path(__file__).resolve().parent.parent
def run(*a, **k): return subprocess.run(list(a), capture_output=True, text=True, **k)
class T(unittest.TestCase):
    def test_validate(self):
        r = run(sys.executable, str(R/"scripts/validate.py")); self.assertEqual(r.returncode, 0, r.stdout)
    def test_ai_score_flags(self):
        t = "Great question! It's not just a tool, it's a shift. Let that sink in."
        r = run(sys.executable, str(R/"scripts/ai-score.py"), input=t)
        self.assertGreaterEqual(int(re.search(r"tells=(\d+)", r.stdout).group(1)), 3)
    def test_ai_score_clean(self):
        r = run(sys.executable, str(R/"scripts/ai-score.py"), input="We shipped the report on Friday.")
        self.assertIn("tells=0", r.stdout)
    def test_debt_runs(self):
        self.assertEqual(run("sh", str(R/"scripts/debt.sh"), str(R/"examples")).returncode, 0)
    def test_mode_needs_consent(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertEqual(run("sh", str(R/"scripts/mode.sh"), "ultra", cwd=d).returncode, 3)
            env = dict(os.environ, FORJA_CONSENT="1")
            self.assertEqual(run("sh", str(R/"scripts/mode.sh"), "ultra", cwd=d, env=env).returncode, 0)
            self.assertEqual(run("sh", str(R/"scripts/mode.sh"), "bogus", cwd=d, env=env).returncode, 2)
    def test_compare_loc(self):
        with tempfile.TemporaryDirectory() as a, tempfile.TemporaryDirectory() as b:
            pathlib.Path(a, "x.py").write_text("a=1\nb=2\nc=3\nd=4\n"); pathlib.Path(b, "x.py").write_text("a=1\n")
            self.assertIn("-75%", run(sys.executable, str(R/"scripts/compare-loc.py"), a, b).stdout)
if __name__ == "__main__": unittest.main()
