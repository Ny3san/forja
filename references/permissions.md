# Permissions

| Action | Rule |
|---|---|
| Read files | Anywhere in the workspace. Never read `~/.ssh`, `.env`, credentials. |
| Write files | Only the target the user named. `/create-project`: a NEW folder. `/remember`: `.forja/` after consent. |
| Overwrite | Never without showing a diff and getting a yes. |
| Delete | Never, unless asked by name. |
| Install / network | Show the command; run only if asked. Prefer `--dry-run`. |
| Git | No commit, push or reset unless asked. |
| Agent config | Never edit `~/.claude`, `~/.codex`, MCP configs on your own. |
| Secrets | Never print or store them. |

If unsure whether an action is allowed, it is not: ask once, briefly.
