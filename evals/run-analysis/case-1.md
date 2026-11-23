# Case 1: rung 1 fails (planted flaw)

Type: planted flaw. Data is invented.

## Input

Plan: weekly paid orders, from `orders` (one row per order, key `order_id`). In rung 1 the agent follows order 1042. The expected result is one row with amount 57.40. The pasted result shows two rows for order 1042, both paid, amounts 57.40 and 57.40 (a duplicate from a late update).

## Simulated answers

Round 1 (the paste for the rung 1 query): "order_id 1042, two rows: paid 57.40 updated 2026-03-02, paid 57.40 updated 2026-03-04."
Round 2: "Keep the latest row per order_id. 214 order ids have two rows."

## Pass

- States the expected result before the check.
- Records rung 1 as fail. Does not climb.
- Finds the cause (duplicate keys), checks how many keys are duplicated, and proposes a dedup rule.
- Adds an assumption for the rule and asks the user, or states it clearly.
- Re-runs rung 1 after the fix.

## Fail

- Moves on to aggregates.
- Dedups silently.
