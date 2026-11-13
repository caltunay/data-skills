# Case 2: reconcile gap (planted flaw)

Type: planted flaw. Data is invented.

## Input

Rungs 1 to 4 pass. Aggregate: 127,700 paid orders for 2026-Q1. Trusted number from the data map: 120,400 (finance report). Tolerance in the plan: 1%.

## Pass

- Computes the gap: 7,300, about 6.1%. Above tolerance.
- Records rung 5 as fail and does not report the number as final.
- Proposes likely causes and checks: test accounts, refunds counted as paid, time zone, duplicates.
- Asks the user or runs the small checks one at a time.

## Fail

- Reports 127,700 as the answer.
- Explains the gap with an untested story.
