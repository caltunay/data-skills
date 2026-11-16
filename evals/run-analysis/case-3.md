# Case 3: everything passes (clean)

Type: clean. Data is invented.

## Input

Quick depth. Plan: count paid orders in October 2026, UTC, test accounts excluded. Rung 1 (order 2210: one row, paid, 31 Oct 23:40 UTC) passes. Total 41,820. Trusted number 41,900. Tolerance 1%.

## Pass

- Computes the gap: 80, about 0.2%. Within tolerance. Reports rung 5 as pass.
- Gives the answer with the ceiling (descriptive: "was") and any open assumptions.
- Writes no files at quick depth.
- Raises no invented issues.

## Fail

- Invents extra checks or doubts.
- Uses causal or predictive wording.
