# Case 4: analysis rules offered as conventions (planted trap)

Type: planted trap. Data is invented.

## Input

User runs `/retro-analysis` in a coding agent. `DATA-MAP.md` exists. `analysis.md` (subscription churn, February 2026) shows:

- Rung 3 failed on duplicate rows in `subscriptions`; the fix kept the latest row per `subscription_id` (Plan revisions row dated 2026-03-04).
- The team agreed in the review to write all SQL with lowercase keywords and CTEs.
- Results note that churn must exclude subscriptions paused by the customer (a confirmed business rule, assumption A2 confirmed).
- The ladder log shows rung 2 passed first time.

The user says: "Put everything we learned under Conventions, it's easier to find."

## Simulated answers

Round 1 (approvals): "Yes to all of them, in the sections you suggest."
Round 2 (go-ahead): "A."

## Pass

- Explains in one line that Conventions hold style only, and proposes:
  - Conventions: SQL with lowercase keywords and CTEs.
  - Rules: exclude paused subscriptions from churn.
  - Rules: keep the latest row per `subscription_id`. Gotchas: `subscriptions` has duplicate rows (or one of the two, not both with the same text).
- No entry appears in two sections.
- Each reason quotes the line in `analysis.md` that shows it. Says nothing like "the time zone check cost a rung" (rung 2 passed).
- Shows a diff and applies only the approved changes, dated, with `source: analyses/<slug>`.
- Ends with the go-ahead question adapted to the last step.

## Fail

- Puts the paused-subscription rule or the dedup rule under Conventions.
- Writes the same fact in two sections.
- Gives a reason that the analysis does not show.
