---
name: review
summary: Review a change or deliverable like the dev who gets paged
args: [uncommitted|staged|branch|PR link|path]
write: none
---
# /review
1. Pick the target (default: current diff). 2. Read the touched code and what depends on it; with Graft use `graft blast --base origin/main` and `graft callers`, else `grep`. 3. Check bugs, security, real load, missing tests, slow paths, what to cut. 4. Report per `references/review-format.md`. 5. End with a verdict and what was not checked.
Non-code deliverables (plans, texts): check against the request, missing risks, unverifiable claims. No praise padding.
