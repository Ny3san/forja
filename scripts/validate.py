#!/usr/bin/env python3
"""Validate Forja itself: frontmatter, router, references, markers."""
import re, sys, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
errs = []
skill = (root / "SKILL.md").read_text()
m = re.match(r"---\n(.*?)\n---\n", skill, re.S)
if not m: errs.append("SKILL.md: missing frontmatter")
else:
    fm = m.group(1)
    if "name: forja" not in fm: errs.append("SKILL.md: name must be forja")
    d = re.search(r"description: (.*)", fm)
    if not d or len(d.group(1)) > 1024: errs.append("SKILL.md: description missing or >1024 chars")
if len(skill.splitlines()) > 150: errs.append("SKILL.md too long (>150 lines)")
cmds = sorted(p.stem for p in (root / "commands").glob("*.md"))
for c in cmds:
    if f"commands/{c}.md" not in skill: errs.append(f"router missing {c}")
    body = (root / "commands" / f"{c}.md").read_text()
    for key in ("name:", "summary:", "write:"):
        if key not in body.split("---")[1]: errs.append(f"commands/{c}.md: no {key}")
for ref in set(re.findall(r"(?:references|scripts)/[\w.-]+", skill + "".join(p.read_text() for p in (root/"commands").glob("*.md")))):
    if not (root / ref).exists(): errs.append(f"missing file: {ref}")
for p in root.rglob("*.md"):
    if "tests" in p.parts: continue
    for link in re.findall(r"\]\((?!http)([^)#]+)\)", p.read_text()):
        if not (p.parent / link).exists(): errs.append(f"{p.relative_to(root)}: broken link {link}")
print(f"commands: {len(cmds)}")
print("\n".join(errs) or "OK")
sys.exit(1 if errs else 0)
