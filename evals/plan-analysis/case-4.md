# Case 4: "why did X drop" at standard depth (hypothesis tree)

Type: standard case. Data is invented.

## Input

`analysis.md` holds a grilled ask: "Why did paid orders drop in October?" Standard depth. Question type: exploratory, after a descriptive step. `DATA-MAP.md` lists `orders`, `customers` and `daily_marketing_spend`. Orders fell about 14% per day from September to October. Nothing else is known.

## Simulated answers

Round 1: "Follow H1 and H2. Park H3."
Round 2: "Yes, draft the readout skeleton. Go with your recommended method."

## Pass

- Writes a hypothesis tree before the method options: H1, H2, H3 with children (H1.1, H1.2 and at least one third-level node under one of them). At most 3 levels and about 12 nodes.
- Every node has a support condition, a refute condition and the child it leads to. Example: "H1: a logging break. Supported by zero or missing days in the daily series. Refuted by a full daily series. Leads to H1.1, a missing event type."
- Includes at least one data hypothesis (logging, duplicates, a filter change) and one business hypothesis (a channel, a segment, a spend change).
- Asks which paths to follow, with a recommended default, and marks the rest `parked`.
- Writes a Hypotheses section in `analysis.md` with a status per node.
- Offers the readout skeleton. If taken, `readout.md` has `**Status: SKELETON**` and placeholders only (XX%, [segment]). No invented number.
- Then lists options and a chosen plan, and states the ceiling: a pattern to test, not a cause.
- Ends with the go-ahead question, A) being `/run-analysis`.

## Fail

- Method options before any tree.
- A tree with nodes that have no refute condition.
- A skeleton that holds a real-looking number such as "orders fell 14.3%" that no run produced.
- More than 3 levels, or a flat list at standard depth.
