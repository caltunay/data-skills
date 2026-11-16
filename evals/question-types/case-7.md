# Case 7: churn model with a leak and a rare outcome

Type: method choice, predictive. Data is invented. Grade the method chosen and the checks named, not calculations.

## Input

"We want to predict which subscribers will cancel in the next 30 days, so the retention team can call them. They can make about 500 calls a week. About 8% cancel in a month. Our first gradient boosting model has 99% accuracy. Features include plan, tenure, logins in the last 30 days, days since last login, and `cancellation_reason`. We split the rows at random. Is this good to ship?"

## Pass

- Question type: predictive. The ceiling: "predicts", not "why they cancel".
- Says not to ship. Names the leak: `cancellation_reason` only exists for customers who cancelled (target leakage).
- Names the split problem: a random split on time-ordered data, and the same customer possibly on both sides. Asks for a split by time and by customer.
- Asks for the prediction time, and whether each feature is known before it.
- Says accuracy is the wrong metric at an 8% base rate. Asks for precision and recall, PR-AUC against the base rate, and a threshold set by the 500 calls a week.
- Says: baseline first (base rate, the current rule), then logistic regression, and gradient boosting only if it beats the simple model on a time-ordered holdout.
- Says feature importance will show what the model uses, not what causes churn.
- If the scores are used as probabilities, asks for a calibration check.

## Fail

- Accepts 99% accuracy.
- Suggests tuning or a bigger model before the leak and the split are fixed.
- Reads feature importance as the causes of churn.
