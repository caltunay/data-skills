# Case 3: sound analysis (clean)

Type: clean. Tests precision. Adapted from an earlier design. Data is invented.

## Input

User runs `/review-analysis` on:

> **Win-back email to lapsed customers: break-even at best. Do not roll out.**
> Randomised holdout: 20,000 customers got the email, 20,000 did not (random assignment by customer, split checked: 50.0% / 50.0%). Window: 28 days, closed before the pull. Revenue is net of refunds, summed per customer before joining, zeros included. Difference in revenue per customer: +0.31 (95% interval -0.12 to +0.74). Email cost per send: 0.05. Margin 35%. Unsubscribes: 1.1% vs 0.4%, stated as a cost. Segment cuts are labelled exploratory.
> Recommendation: do not roll out as is. The interval includes a loss. Test a smaller list or a better offer.

## Pass

- Verdict: `ready`.
- Says "No material issues" plainly.
- At most 3 optional checks, labelled optional (for example, longer-term value, margin assumption).
- Quotes no flaw that is not there.

## Fail

- Invents must-fix issues.
- Calls the interval or the split wrong.
