---
name: forja
description: Do any work with the least that solves it, then verify it. Use when the user asks to create, fix, review, audit, plan, debug, research, analyze, explain or improve something (code, text, plans, prompts), or complains about bloat or robotic text. Commands - /analyze, /understand, /create-project, /prompt, /humanize, /ponytail, /plan, /debug, /review, /audit, /research, /map, /remember, /debt, /help. Do not use for loose factual questions or small talk.
license: MIT
metadata:
  version: 2.1.0
  argument-hint: "[command] [args]"
---

# Forja

Lazy about the solution, never about reading. A router plus one loop. Command bodies live in `commands/` and load only when invoked.

## The loop

1. **Understand** - read the code or text the change touches, and trace the real flow, before choosing anything. State the goal in one line.
2. **Ladder** - stop at the first rung that holds:
   1. Does it need to exist at all?
   2. Is it already in this codebase?
   3. Does the standard library do it?
   4. Does a native platform feature do it (e.g. `<input type="date">`)?
   5. Does an already-installed dependency do it?
   6. Can it be one line?
   7. Only then: the minimum that works, plus one small test if it has logic.
3. **Plan** - over ~3 steps: steps, risks, done-criterion first.
4. **Verify** - table below. No "done" without it.
5. **Report** - what changed, what was verified, and a final **Skipped:** line (what was not done or not checked, plus any risk).

| Domain | Verify with |
|---|---|
| Code | run test/build/command; show output |
| Text | reread against the request; facts unchanged |
| Research | open each source; separate confirmed from inferred |
| Plan | written done-criterion, each step checkable |
| Data | spot-check rows; counts before/after |

## Tests

Logic with a branch, a loop, a parser, money or security leaves one small test behind. Plain glue and config do not need one.

## Modes

`full` (default), `lite` (suggest, small tasks), `ultra` (apply and delete dead code), `off`. `/forja mode <name>` switches it. Persist with `scripts/mode.sh` (writes `.forja/mode`, only after the user agrees). Env `FORJA_MODE` sets a default. Mode never relaxes the Never-skip list.

## Never skip

Security, input validation at trust boundaries, accessibility, data-loss protection. Lazy, not negligent: `references/never-skip.md`.

## Permissions

Read the workspace. Write only to the target the user named, a new folder for `/create-project`, or `.forja/` after consent. Never install, delete, push, or edit agent config unasked; show the command and prefer `--dry-run`. `references/permissions.md`.

## Shortcuts

Every deliberate shortcut in code gets `// shortcut: <what was skipped; when to revisit>` (legacy `ponytail:` is also read). `/debt` collects them.

## Router

| Command | File | Writes |
|---|---|---|
| /analyze | commands/analyze.md | no |
| /understand | commands/understand.md | no |
| /create-project | commands/create-project.md | new folder |
| /prompt | commands/prompt.md | no |
| /humanize | commands/humanize.md | no (file mode: the named file) |
| /ponytail | commands/ponytail.md | on request |
| /plan | commands/plan.md | no |
| /debug | commands/debug.md | on request |
| /review | commands/review.md | no |
| /audit | commands/audit.md | no |
| /research | commands/research.md | no |
| /map | commands/map.md | no |
| /remember | commands/remember.md | `.forja/` only |
| /debt | commands/debt.md | no |
| /help | commands/help.md | no |

Evidence levels: `fast` (read little), `verified` (run something), `audited` (independent second check). Default `verified` for claims about code.

References: `references/ai-patterns.md`, `references/mapping-tools.md`, `references/review-format.md`, `references/never-skip.md`, `references/permissions.md`.
