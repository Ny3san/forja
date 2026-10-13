# Review format

Review like the senior dev who gets paged when it breaks. Read the code the change touches, not only the diff.

Check: bugs, security, real load, risky code with no test, slow paths, and what to cut.

Each finding:
- **[must fix | should fix | nice to have]** `file:line` - title
- *What it does:* ...
- *What goes wrong:* ...
- *Fix:* ...
- *If ignored:* ...

Cross-file breakage counts: a renamed field that crashes an untouched file is a must-fix. Sort by severity. End with a verdict (what to fix first) and what was not checked. If nothing is found, say what was checked.

Targets in plain words: `uncommitted`, `staged`, `branch`, or a PR link.
