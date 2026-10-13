---
name: map
summary: Orient in a codebase (graph if present)
args: [question]
write: none
---
# /map
Run `scripts/detect-map.sh`. Graft present: use the commands in `references/mapping-tools.md` (`graft map`, `ask`, `callers`, `grep`, `blast`, `check` if stale). Absent: `tree`, `grep`, `git log`. Never install, `graft init`, or `graft build --deep` without an explicit yes; show the command and `--dry-run` first. The graph points; text search or tests confirm.
