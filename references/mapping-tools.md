# Code-graph tools (optional)

Forja never installs, indexes or wires these without an explicit yes. Detect with `scripts/detect-map.sh`. Command names below come from Graft's README (checked 2026-10-13); run `graft --help` before relying on them.

## Graft (trailhq/Graft, MIT, npm `@nanonets/graft`)

Builds a local graph in `graft/` (git-ignored cache). Plain `graft build` is deterministic tree-sitter: no model, no key.

| Question | Command |
|---|---|
| First look at an unfamiliar repo | `graft map` |
| Where is the code for this task? | `graft ask "<task>"` |
| API surface of one file, no bodies | `graft skeleton <file>` |
| Who calls X? | `graft callers <symbol>` |
| What does X call? | `graft callers <symbol> --direction out` |
| Blast radius of X (N levels) | `graft callers <symbol> -d N` |
| Every occurrence of a pattern | `graft grep "<regex>"` |
| What does this diff reach? | `graft blast --base origin/main` |
| Is the graph stale? | `graft check` |

MCP tools (when registered): `graft_find_code`, `graft_file_api`, `graft_trace_calls`, `graft_find_all`, `graft_repo_map`, `graft_check_freshness`.

Ask-first list (each needs an explicit yes):
- `npm install -g @nanonets/graft` or `npx @nanonets/graft init`.
- `graft init`: writes instruction files, hooks, MCP config in the repo and, when `~/.codex/` exists, user-level Codex files. Show `graft init --dry-run` first; offer `--no-global`.
- `graft build --deep`: LLM summaries through the user's own provider key; spends tokens.
- `graft trail push|pull`: signs up in the browser; `pull` rewrites CLAUDE.md/AGENTS.md.
- Telemetry: anonymous usage ping exists; `graft telemetry disable` or `DO_NOT_TRACK=1` turns it off. Mention it when proposing install.
- `graft uninstall` is the inverse of init.

## codebase-memory-mcp (DeusData)
Not re-checked in this version. Read its README before using; treat it like Graft (ask before install).

## Rules
- A graph says where to look; only text search or running code proves "nobody calls this".
- Savings and accuracy figures in these projects' READMEs are their own measurements, not Forja's.
- No tool present: `grep`, `git log`, `git blame`, and the tests.
