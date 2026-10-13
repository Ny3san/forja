---
name: ponytail
summary: Do the least that works (the laziest senior dev)
args: [path] [lite|full|ultra|off]
write: on request
---
# /ponytail
Climb the ladder in `SKILL.md` (exist? in codebase? stdlib? platform? installed dependency? one line? minimum) after reading the code. Example: a date picker request becomes the repo's existing `Input` with `type="date"`, not a 300-line calendar. Mark each shortcut `// shortcut: <reason; when to revisit>`. One small test for risky logic. Never touch the Never-skip list. End with `Skipped:`.
Modes: no argument reports the current mode; `lite` suggests only; `full` applies; `ultra` applies and removes dead code; `off` disables.
