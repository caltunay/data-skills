# Case 2: A/B readout (planted flaws)

Type: planted flaws. Adapted from an earlier design. Data is invented.

## Input

User runs `/review-analysis` on:

> **New checkout button lifts conversion 4.2% (p = 0.03). Ship it.**
> Planned: 50/50 split, 14 days. Stopped at day 7 because p fell below 0.05. Arms: 52,300 users (control) vs 47,700 (variant). Randomised by user, analysed by session. Mobile showed a +9% lift (found after slicing by 6 segments). Average order value was not significant.

## Pass

- Verdict: `needs rework`.
- Finds the sample ratio mismatch: planned 50/50, got 52.3% and 47.7%, chi-square p well below 0.001. Result is not trustworthy until explained.
- Finds early stopping (peeking) and under one weekly cycle.
- Finds the unit mismatch (users randomised, sessions analysed), so the interval is too narrow.
- Labels the mobile result as a hypothesis from slicing.
- Notes the ceiling: a valid randomised test supports causal. This one is not valid yet.
- Does not call the sample too small.

## Fail

- Says ship.
- Raises AOV not being significant as a flaw.
