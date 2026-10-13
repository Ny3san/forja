---
name: create-project
summary: Make a minimal project in a new folder
args: <name> [stack]
write: new folder only
---
# /create-project
1. Refuse if the folder exists and is non-empty. 2. Apply the ladder: standard library and zero dependencies first. 3. Create only: entry file, one test, README (run + test commands), .gitignore. 4. Run the test; show output. 5. Never run `npm install`/`pip install` without asking; print the command instead.
