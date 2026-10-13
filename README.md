# Forja

**Do any work with the least that solves it, then verify it.**

Forja is an agent skill for code, text, plans, research and prompts. It is lazy about the solution and never lazy about reading: it understands first, picks the smallest thing that works, proves it, and says what it skipped. 15 commands, one loop, strict write permissions.

## Install

Skills-compatible agents (Claude Code, Codex, OpenCode and others):

```
npx skills add Ny3san/forja
```

Or copy this folder into your agent's skills directory (for Claude Code: `~/.claude/skills/forja/`). Check your agent's docs for its exact path.

Agents without skills: paste `adapters/AGENTS.md` into your `AGENTS.md`, `CLAUDE.md` or equivalent rules file (no commands, always-on rules only).

## The loop

1. **Understand**: read what the change touches and trace the real flow.
2. **Ladder**, stop at the first rung that holds: needs to exist? already in the codebase? standard library? native platform feature? installed dependency? one line? only then the minimum, plus one small test if it has logic.
3. **Plan** anything over about 3 steps.
4. **Verify** (tests, rereading, opened sources, spot checks).
5. **Report**, ending with a `Skipped:` line.

Never skipped, in any mode: security, input validation, accessibility, data-loss protection.

## Commands

| Command | What it does | Writes |
|---|---|---|
| `/analyze` | Diagnose a project; every finding cites evidence | no |
| `/understand` | Explain code or a system | no |
| `/create-project` | Minimal project in a new folder | new folder only |
| `/prompt` | Review and improve a prompt | no |
| `/humanize` | Remove AI tells without changing facts; optional `--voice` sample | no (file mode: named file) |
| `/ponytail` | Reduce complexity; modes `lite`, `full`, `ultra`, `off` | on request |
| `/plan` | Goal to steps, risks, done-criterion | no |
| `/debug` | Reproduce, hypothesize, root cause, regression test | on request |
| `/review` | Review a change like the dev who gets paged | no |
| `/audit` | Rank what to fix across the whole repo | no |
| `/research` | Search with sources: confirmed vs inferred | no |
| `/map` | Orient in a codebase (uses Graft if present) | no |
| `/remember` | Keep corrections in `.forja/lessons.md` | `.forja/` only |
| `/debt` | Ledger of deferred `shortcut:` comments | no |
| `/help` | Quick reference | no |

Examples are in `examples/before-after.md`.

## Shortcuts leave a trail

Every deliberate shortcut in code gets a comment such as `// shortcut: no pagination; add when lists exceed 100 rows`. `/debt` collects them so "later" does not become "never".

## Permissions

Forja reads the workspace and writes only to the target you name, a new folder for `/create-project`, or `.forja/` after you agree. It never installs, deletes, pushes or edits agent config unasked; it shows the command and prefers `--dry-run`. Full rules: `references/permissions.md` and `references/never-skip.md`.

## Optional code graph

If [Graft](https://github.com/trailhq/Graft) is installed, `/map` and `/review` use its CLI (`graft map`, `ask`, `callers`, `grep`, `blast`, `check`). Forja detects it with `scripts/detect-map.sh` and never installs or wires it for you. A graph says where to look; text search or tests confirm. Details: `references/mapping-tools.md`.

## Scripts and tests

| File | Purpose |
|---|---|
| `scripts/validate.py` | Checks Forja itself: frontmatter, router, references, links |
| `scripts/ai-score.py` | Counts AI-writing tells before and after `/humanize` |
| `scripts/compare-loc.py` | Lines of code with vs without the skill, on your own tasks |
| `scripts/debt.sh` | Collects `shortcut:` markers |
| `scripts/detect-map.sh` | Detects Graft and codebase-memory-mcp |
| `scripts/mode.sh` | Reads or persists the mode (writing needs `FORJA_CONSENT=1`) |

```
python3 scripts/validate.py
python3 tests/test_forja.py
```

`evals/evals.json` holds 14 prompts with the expected behavior, including cases where the skill must not activate. They have not been run against an agent yet.

## Credits and honesty

- Ponytail (DietrichGebert/ponytail, MIT): decision ladder, "lazy but never negligent", tests for risky logic, `shortcut:` markers, review, audit and debt shapes.
- Humanizer (blader/humanizer, MIT) and Wikipedia's "Signs of AI writing": the 26-pattern taxonomy and the draft, critique, final process, rewritten in Forja's own words.
- Graft (trailhq/Graft, MIT): optional code graph.

The savings and accuracy figures published by those projects are their own measurements. Forja has no benchmark of its own yet.

## License

MIT.
