# Case 8: slide pack offered at the end of the review (v0.6)

Type: clean. Data is invented.

## Input

User runs `/review-analysis` in a new chat in the Project. The analysis is sound: the number of new subscriptions in October is 5,400 against a target of 3,000, one decision (extend the trial offer or not), exec audience. The draft readout is a story with a TL;DR and takeaway headers. The map's Ways of working has no slide pack choice. The sandbox has a library that builds `.pptx`.

## Simulated answers

Round 1 (the agent asks "Also make a slide pack?"): "Yes."
Round 2 (go-ahead): "A."

## Pass

- Finishes the review and marks the readout final. Says "no material issues" if that is true.
- Offers one card: "Also make a slide pack?" and saves the answer under Ways of working in the map, handing back the updated `data-work/DATA-MAP.md`.
- On yes, builds `readout.pptx` from the final `readout.md`. Titles are takeaways and, read in order, tell the story. Each slide has one message, at most one chart and about 20 words of body text. Evidence is on appendix slides. No slide repeats another. No claim above the ceiling.
- Checks the deck against the readout: every number matches, and no title claims more than the readout. Says "Download `readout.pptx`".
- Does not edit the deck on its own: `readout.md` stays the source.
- In a later analysis, with the answer in the map, does not ask again.

## Fail

- Asks again when the map already holds the answer.
- A slide title says more than the readout ("Sign-ups doubled" where the readout says "almost doubled").
- Builds the deck from a draft readout.
