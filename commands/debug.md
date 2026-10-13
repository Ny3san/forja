---
name: debug
summary: Reproduce, hypothesize, find root cause
args: <symptom>
write: on request
---
# /debug
1. Reproduce (exact command/input). 2. List 2-3 hypotheses, cheapest test first. 3. Test one at a time; log evidence. 4. State root cause, not symptom. 5. Fix minimally, add a regression test, rerun the reproduction.
If you cannot reproduce, say so and stop guessing.
