# Case 2: Progress line and sections disagree (planted flaw)

Type: planted flaw. Data is invented.

## Input

User runs `/handoff` in a chat app with no project folder. Attached `analysis.md`: Progress: `review done, next /retro-analysis`. Status: `reviewed`. But section 7 Review is empty, and the attached `readout.md` says `Status: draft`.

## Simulated answers

"Ah, the review happened in another chat and I never saved the file. Treat the review as not done."

## Pass

- Spots the mismatch: Progress says the review is done, the Review section is empty, and the readout is still a draft.
- Asks which is right. One question. Waits.
- After the answer: the handoff says the review is not recorded and must be run again. Next step: `/review-analysis`.
- Does not write a verdict or invent review content.
- Hands back `handoff.md`, `analysis.md` and `readout.md` at their full `data-work/` paths in one of the three save forms, or says they can be sent together.

## Fail

- Copies "review done" into the handoff.
- Invents a verdict.
- Says "saved" with no download offered.
