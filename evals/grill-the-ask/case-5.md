# Case 5: period comparison across a seasonal boundary (planted flaw)

Type: planted flaw. Data is invented.

## Input

User runs `/grill-the-ask` in a coding agent with a `DATA-MAP.md` that holds two years of shop order history.

"Our head of e-commerce says orders fell off a cliff. Compare the last 30 days (2 to 31 January 2026) with the 30 days before (3 December 2025 to 1 January 2026). It feeds a decision on whether to cut the January promo budget."

## Simulated answers

Round 1: "Orders means paid orders. All markets. The requester is the head of e-commerce."
Round 2: "Go with your recommended comparison. Exec audience. Deadline is the budget meeting on 6 February."

## Pass

- Notices that the prior window holds the December peak and the holiday days, so a back-to-back comparison builds in a seasonal drop.
- Recommends a comparison that handles seasonality: the same 30 days last year (2 to 31 January 2025), or year on year for both windows, with the same weekdays. The recommended option is marked with a reason.
- If it also offers the back-to-back comparison, flags in that option that it ignores seasonality and what it would hide.
- Every question has one real recommended default, the deadline included.
- Requester and date are filled in Meta.
- Ends with the go-ahead question, A) being `/plan-analysis`.

## Fail

- Recommends "last 30 vs prior 30 days" with no seasonality flag.
- Accepts "fell off a cliff" as the finding before any data is checked.
- Leaves a question with no default, or uses a hedge such as "C if unknown".
