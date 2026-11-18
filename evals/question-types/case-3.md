# Case 3: cut-off on a score

Type: method choice. Data is invented. Grade the method chosen and the checks named, not calculations.

## Input

"Customers who spent 200 or more last year got a loyalty discount automatically. Customers below 200 did not. Did the discount increase orders this year?"

## Simulated answers

None needed.

## Pass

- Question type: causal.
- Method: regression discontinuity (assignment by a cut-off on a score).
- Says it is a short card: needs a specialist review before shipping.
- Names the key checks: plot the outcome against last year's spend around 200, bunching just above the cut-off (could customers steer their spend?), no jump in pre-treatment covariates, stable across bandwidths.
- Asks whether customers knew about the threshold in advance.
- States the limit: the effect holds for customers near 200 only.

## Fail

- Compares all discounted customers with all others.
- Claims an effect for all customers.
