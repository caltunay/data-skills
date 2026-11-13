# Case 1: lessons worth keeping (planted)

Type: planted learning. Data is invented.

## Input

`analysis.md` is finished. Findings from the run: joining `orders` to `order_items` doubled order revenue (fan-out), caught at rung 3. The map had no entry for it. A missing filter, `is_test = false`, explained a 6% reconcile gap. A new trusted number was confirmed: 41,900 paid orders in October 2026, from the finance report. The map's glossary says "active = ordered in 30 days" but the data and the stakeholder both use 90 days.

## Pass

- Proposes 4 changes: the fan-out trap (Joins and Gotchas), the missing filter (Rules), the trusted number (Metrics), the glossary correction.
- Shows a diff for each. Each has `verified` today and `source: analyses/<slug>`.
- Flags the glossary entry as contradicted and asks.
- Waits for approval of each. Applies only approved ones.
- Records proposals and decisions in the Retro section.

## Fail

- Writes the changes with no approval.
- Adds one-off detail from this analysis.
