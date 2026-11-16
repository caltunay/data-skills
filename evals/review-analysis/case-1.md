# Case 1: causal claim from timing (planted flaws)

Type: planted flaws. Adapted from an earlier design. Data is invented.

## Input

User runs `/review-analysis` on:

> **Checkout conversion dropped from 3.1% to 2.6% in October.** Claim: the new payment page, released 8 Oct, caused a 0.5 point drop. Recommend rolling it back.
> Sessions: Sept 1,820,000, Oct 2,150,000. Orders: Sept 56,420, Oct 55,900. The drop started the week of 8 Oct. Nothing else in the release log touched checkout. Lost orders at September's rate: 10,750, about 450k per month.
> Notes: a mobile campaign ran in October. A new session tracking SDK shipped 7 Oct.

Hidden facts: desktop conversion 4.1% and mobile 2.1% did not change. Mobile share rose from 52% to 75%.

## Pass

- Verdict: `needs rework` or `ready with caveats` at most. Not `ready`.
- Finds the mix shift: blended 0.52 x 2.1 + 0.48 x 4.1 = 3.1%, and 0.75 x 2.1 + 0.25 x 4.1 = 2.6%. Asks for the split by device.
- Finds the session SDK change on 7 Oct, so the denominator is not comparable.
- Flags "caused" as above the ceiling. Allowed: "conversion changed after 8 Oct".
- Flags the 450k figure as using the wrong baseline.
- Gives the exact checks to run.

## Fail

- Accepts the causal claim.
- Raises order status filters or generic seasonality as the main point.
