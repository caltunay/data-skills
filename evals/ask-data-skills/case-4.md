# Case 4: a design ask (routing)

Type: standard case. Data is invented.

## Input

User runs `/ask-data-skills`: "I need to design an A/B test for the shop's new pricing page. We have no data for it yet."

## Simulated answers

None needed.

## Pass

- Recommends `/wayfinder-data` (fast path), not `/grill-the-ask`.
- One line why: a design with no data needed yet needs one spec, not an analysis.
- Names `/grill-the-ask` as the next command, for the analysis that will read the test out.
- Asks no questions. Does not begin the design.

## Fail

- Recommends `/grill-the-ask` or `/plan-analysis` first.
- Starts asking about the test design.
