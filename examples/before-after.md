# Examples

## /humanize
Before: "I'm thrilled to announce shared drafts! It's not just a feature, it's a whole new way to collaborate. Let that sink in."
After: "Shared drafts are out today. Two people can edit the same doc at once."

## /ponytail
Request: add a date picker. No skill: install a library or hand-build a calendar. Forja: reuse the repo's `Input` with `type="date"`; the browser brings the calendar.
`// shortcut: native picker only; add a range picker if users ask`

## /review
**[must fix]** `src/routes/feed.js:14` - crashes on every request. *What it does:* reads `post.title`. *What goes wrong:* the change renamed the field to `heading`. *Fix:* use `post.heading`. *If ignored:* the Atom feed is down.

## /debt
`src/api.js:12: // shortcut: no pagination; add when lists exceed 100 rows`
