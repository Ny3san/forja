---
name: humanize
summary: Remove AI tells without changing the facts
args: <text|file path> [--voice <sample>]
write: none (file mode edits only the named file's prose)
---
# /humanize
1. Extract facts, names, numbers, dates, quotes, citations: they survive unchanged. Missing detail needed? Ask; never invent. 2. Scan against `references/ai-patterns.md`; list tells, strongest first. 3. Draft a rewrite (original structure is optional). 4. Critique the draft in one or two lines. 5. Final version. 6. `--voice`: match the sample's rhythm, word choice, punctuation, quirks; keep the writer's opinions; do not copy its topics.
Pasted text: show draft, critique, final. File path: edit prose only; leave code, data, frontmatter, link targets. Technical prose stays neutral. Optional count: `python3 scripts/ai-score.py <file>`. Never promise to beat AI detectors.
