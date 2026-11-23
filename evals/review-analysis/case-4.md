# Case 4: draft readout with one overclaiming sentence (planted flaw)

Type: planted flaw. Data is invented.

## Input

User runs `/review-analysis`. `analysis.md` holds a sound descriptive analysis: question type descriptive, full ladder log with all rungs passed, reconcile within tolerance, no open high-impact assumptions. Finding: sign-ups were 31,200 in March against 36,900 in February, down 15.4%. The fall is concentrated in paid social (down 41%). Other channels are within 3%.

The draft `readout.md` says:

> Status: draft
> **Answer.** Sign-ups fell 15.4% in March (31,200 against 36,900 in February). The cut in paid social budget caused the drop.
> **Key numbers.** March 31,200. February 36,900. Paid social sign-ups down 41%. Other channels within 3%. Counts are exact for the period and reconcile to the growth dashboard within 0.4%.
> **What it means.** The fall is concentrated in one channel. Review paid social before changing anything else.
> **Caveats.** This analysis describes what happened. It does not test why.
> **Method.** Sign-ups counted by account creation date, UTC, test accounts excluded. Split by acquisition channel. Validated on the ladder and reconciled.

## Simulated answers

None needed.

## Pass

- Reads the readout sentence by sentence.
- Finds exactly one sentence above the ceiling: "The cut in paid social budget caused the drop."
- Fixes it and shows "was" and "now". For example, now: "The drop is concentrated in paid social sign-ups. This analysis cannot say why."
- Notes that the readout contradicts its own caveat.
- Leaves the other sentences unchanged.
- Verdict: `ready` or `ready with caveats`. Sets the readout to `Status: final` after the fix.
- Raises no invented issues with the analysis.

## Fail

- Marks the readout final with "caused" still in it.
- Rewrites the whole readout.
- Returns `needs rework` for a sound analysis.
