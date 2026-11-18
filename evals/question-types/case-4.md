# Case 4: single series with a launch date

Type: method choice. Data is invented. Grade the method chosen and the checks named, not calculations.

## Input

"We redesigned the sign-up page for everyone on 10 September. No holdout. We have daily sign-ups for two years. Did the redesign increase sign-ups?"

## Simulated answers

None needed.

## Pass

- Question type: causal, with a weak design.
- Method: interrupted time series (one series, known change date, no comparison group).
- Names these checks: what else changed around 10 September (campaigns, prices, tracking), seasonality (same weeks last year), autocorrelation handled, a placebo date.
- Says that if a rival event exists, the claim drops to descriptive: "sign-ups changed after 10 September".
- States the claim allowed, with "another cause cannot be ruled out".
- Suggests a holdout for next time.

## Fail

- Compares the mean before with the mean after and calls it the effect.
- Uses difference-in-differences with no comparison group.
