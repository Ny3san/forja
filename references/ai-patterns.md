# AI-writing patterns (for /humanize)

Pattern list adapted from Wikipedia's "Signs of AI writing" (the guide its editors use), as organized by the MIT-licensed `blader/humanizer`; rewritten here in Forja's own words. Goal: text that reads well for people. Not detector evasion; detectors may still flag it.

Why they happen: a model picks the most likely next phrase, which fits the widest range of readers. A person writes for one reader about one subject. Every tell below is that default showing.

## Strongest five (one sighting justifies an edit)
1. **Not X but Y** - "It's not just a feature, it's a shift."
2. **One-line closers** - "Let that sink in." / "That is the real win."
3. **Sayings that sound deep** - "At its core, what matters is..."
4. **Staged run-up** - "Here's the thing." "Honestly?" "Let's dive in."
5. **Arguing with no one** - "I'm not saying X, but..." about an objection nobody raised.

## A. Staging instead of stating
Dramatic fragments ("No prior. No nostalgia."), a closer that repeats the example, fake options ("A tempting approach would be..."). Fix: state the claim directly; cut the run-up.

## B. Rhythm by rule
Forced triads; repeated sentence openings; dashes as universal glue *(weak alone)*; stacked qualifiers *(weak alone)*; hyphenating everything *(weak alone)*; passive voice with no actor *(weak alone)*. Fix: use as many items as the meaning needs; vary openings; keep only qualifiers the source supports.

## C. Inflation and borrowed authority
Overused words (delve, testament, landscape, pivotal, showcase, streamline, leverage, robust, seamless); inflated significance ("marking a pivotal moment", "the future looks bright"); vague connection ("in connection with"); shallow -ing riders ("symbolizing, reflecting..."); sales language ("nestled in a breathtaking region"); borrowed authority ("experts believe", a list of famous outlets); dodging "is/are/has" ("serves as", "boasts"). Fix: plain words, the fact only, name a real source or drop the claim, end on the last concrete fact.

## D. Formatting by rule
Bold as decoration, labeled bullet lists that should be prose, decorative headings with emoji or title case, curly quotes *(weak alone)*. Fix: plain prose, sentence-case headings.

## E. Leftovers from the chat and draft
Chatbot wrapper ("Great question!", "I hope this helps"), knowledge-limit hedging ("details are limited in available sources"), a heading echoed by the first sentence, writing about the document instead of the subject ("The table below compares..."). Fix: remove the wrapper; describe the subject.

## F. Wrong reader
Re-explaining what the reader already knows before the decision. Fix: lead with the decision; put the proof after.

## Weak patterns
A *weak alone* pattern counts only when several tells share a passage. A careful writer may use any one on purpose. Do not rewrite correct, specific prose.

## Process (shows its work)
1. List the tells found, strongest first.
2. Draft a rewrite; treat the original structure as optional.
3. Critique the draft in one or two lines: what still sounds artificial.
4. Final version.

Pasted text: show draft, critique, final. A file: change only prose; leave code, data, frontmatter and link targets alone.

## Facts
Names, numbers, dates, quotes and citations come from the source or the writer. If a sentence needs a missing detail, ask instead of inventing one.

## Voice matching
From the sample, measure: sentence length and its spread, contractions, punctuation habits (including dashes if they use them), favorite connectors, formality, deliberate quirks. Apply those; do not copy the sample's topics. Personal writing keeps the writer's opinions and quirks; technical or reference prose stays neutral and plain.
