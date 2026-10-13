#!/usr/bin/env python3
"""Compare lines of code between two directories (e.g. with vs without Forja). Honest, small, local."""
import sys, pathlib
EXT = {".py", ".js", ".ts", ".tsx", ".jsx", ".go", ".java", ".rb", ".rs", ".c", ".cpp", ".php", ".sh", ".sk"}
def loc(d):
    n = 0
    for p in pathlib.Path(d).rglob("*"):
        if p.suffix in EXT and p.is_file() and "node_modules" not in p.parts:
            n += sum(1 for l in p.read_text(errors="ignore").splitlines() if l.strip() and not l.strip().startswith(("#", "//")))
    return n
if len(sys.argv) != 3: sys.exit("usage: compare-loc.py <baseline_dir> <forja_dir>")
a, b = loc(sys.argv[1]), loc(sys.argv[2])
print(f"baseline={a} forja={b} change={(b-a)/a*100:+.0f}%" if a else f"baseline=0 forja={b}")
