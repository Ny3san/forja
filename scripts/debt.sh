#!/bin/sh
# List shortcut markers. Read-only.
grep -rnE "(shortcut|ponytail):" "${1:-.}" --exclude-dir=.git --exclude-dir=node_modules --exclude-dir=tests 2>/dev/null || echo "no shortcut markers"
