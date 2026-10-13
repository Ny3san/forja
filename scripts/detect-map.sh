#!/bin/sh
# Read-only: report optional code-graph tooling.
for t in graft codebase-memory-mcp; do
  if command -v "$t" >/dev/null 2>&1; then echo "found: $t"; else echo "missing: $t"; fi
done
[ -d graft ] && echo "graph dir: graft/ present (run 'graft check' for freshness)" || echo "graph dir: none"
[ -d .git ] && echo "git: yes" || echo "git: no"
