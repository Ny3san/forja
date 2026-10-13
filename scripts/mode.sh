#!/bin/sh
# Usage: mode.sh [lite|full|ultra|off]. No arg: print mode. Writing needs FORJA_CONSENT=1.
f=.forja/mode
if [ -z "$1" ]; then cat "$f" 2>/dev/null || echo "${FORJA_MODE:-full}"; exit 0; fi
case "$1" in lite|full|ultra|off) ;; *) echo "invalid mode: $1" >&2; exit 2;; esac
[ "$FORJA_CONSENT" = "1" ] || { echo "refusing to write $f without FORJA_CONSENT=1 (ask the user first)" >&2; exit 3; }
mkdir -p .forja && echo "$1" > "$f" && echo "mode=$1"
