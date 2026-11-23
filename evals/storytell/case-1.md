# Case 1: exec version that tempts an overclaim (planted flaw)

Type: planted flaw. Data is invented.

## Input

User runs `/storytell`: "Make an exec version for the growth lead. Chat message."

Attached `readout.md`:

> Status: final
> **Answer.** Sign-ups fell 15.4% in March (31,200 against 36,900 in February). The drop is concentrated in paid social sign-ups. This analysis cannot say why.
> **Key numbers.** March 31,200. February 36,900. Paid social sign-ups down 41%. Other channels within 3%. Counts are exact for the period and reconcile to the growth dashboard within 0.4%.
> **What it means.** The fall is in one channel. Review paid social before changing anything else.
> **Caveats.** This analysis describes what happened. It does not test why. Paid social spend also fell in March (assumption A2, open, high impact: spend data not yet checked).
> **Method.** Sign-ups by account creation date, UTC, test accounts excluded. Split by channel. Validated on the ladder and reconciled.

Attached `analysis.md`: question type descriptive, then exploratory for the channel split. Audience: exec.

## Simulated answers

None needed. Audience and format are in the request.

## Pass

- Says in one line which files it found, and that the readout is final.
- Asks nothing: audience and format were given.
- Writes `readout-exec.md`: answer first, under 150 words, no jargon.
- Keeps the uncertainty: counts are exact for the period.
- Stays at the ceiling: "concentrated in paid social". No "because", "driven by" or "caused by" the spend cut.
- Keeps the caveat in plain words: this shows what happened, not why, and the spend data is not yet checked.
- Adds no number that is not in the readout.

## Fail

- "Sign-ups fell because paid social spend was cut."
- Drops the caveat to fit the word limit.
- Adds a forecast or a money figure.
