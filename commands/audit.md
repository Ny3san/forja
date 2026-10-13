---
name: audit
summary: Rank what to fix across the whole repo
args: [path]
write: none
---
# /audit
1. Map first: entry points, how data moves, what load is expected (`/map`). 2. Run the same checks as `/review` across the repo. 3. Rank: must fix, should fix, nice to have. 4. Verdict: name the single thing to fix first. 5. List what was not checked. Findings cite `file:line`; no evidence, no finding. Deletion candidates are listed, never deleted.
