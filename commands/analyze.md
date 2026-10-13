---
name: analyze
summary: Diagnose a project with evidence
args: [path]
write: none
---
# /analyze
Every finding cites `file:line` or command output; no evidence, no finding. 1. Detect stack (manifests, lockfiles). 2. `/map` for orientation. 3. Run the existing test/build once; show the result. 4. List findings: **must fix** (breaks, insecure, data loss), **should fix**, **nice to have**. 5. End with the 3 highest-value fixes and what was NOT checked.
