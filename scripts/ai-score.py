#!/usr/bin/env python3
"""Count AI-writing tells in text (stdin or file). Heuristic aid, not proof."""
import re, sys
P = [
 ("not X but Y", r"\bnot (?:just|only|merely)\b[^.!?]{0,60}[,;—-]\s*(?:it'?s|but)\b"),
 ("one-line closer", r"let that sink in|that'?s the real win|and the best part\?"),
 ("staged run-up", r"here'?s the thing|honestly\?|let'?s dive in|let me tell you"),
 ("deep saying", r"\bat its core\b|what really matters"),
 ("chatbot wrapper", r"great question|i hope this helps|certainly!|absolutely!"),
 ("inflation", r"testament|pivotal|evolving landscape|ever-changing|rich tapestry|stands as|the future (?:is|looks) bright"),
 ("ai vocabulary", r"\bdelve|\bstreamline|\bleverag|\brobust\b|\bseamless|\bshowcas"),
 ("avoids is/has", r"\bserves as\b|\bboasts\b"),
 ("filler", r"it is important to note|in order to"),
 ("emoji", r"[\U0001F300-\U0001FAFF\u2728]"),
 ("curly quotes (weak)", r"[\u201c\u201d]"),
 ("em dash (weak)", r"\u2014"),
]
text = open(sys.argv[1]).read() if len(sys.argv) > 1 else sys.stdin.read()
words = max(1, len(re.findall(r"\w+", text)))
tot = 0
rows = []
for name, rx in P:
    n = len(re.findall(rx, text, re.I))
    if n: rows.append((name, n)); tot += 0 if "weak" in name else n
print(f"words={words} tells={tot} per100={100*tot/words:.2f}")
for name, n in rows: print(f"  {n}x {name}")
