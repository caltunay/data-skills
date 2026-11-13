# Descriptive questions

Ceiling: what happened. Not why.

## Method notes

1. **Define the metric.** Numerator, denominator, population, time window, time zone. Match the data map definition.
2. **Is the move real?** Rule out instrumentation changes, tracking outages, late data, definition changes, one-off days.
3. **Decompose.** rate = numerator / denominator. Which one moved?
4. **Segment.** By platform, country, channel, new vs returning. Is the move broad or in one place?
5. **Mix shift.** Did the segment mix change while each segment's rate stayed flat? That is Simpson's paradox. Compute the blended rate from the segment rates and shares to test it.
6. **Timing.** When did it start? Line it up with releases, campaigns, holidays, price changes. Matching dates are a lead, not a cause.
7. **Seasonality.** Compare with the same period last year, not only last week.
8. **Reconcile** to a trusted number.

## Worked example (invented)

Checkout conversion fell from 3.1% to 2.6% in October. Desktop stayed at 4.1% and mobile at 2.1%. Mobile share rose from 52% to 75% after a campaign. Blended: 0.52 x 2.1% + 0.48 x 4.1% = 3.1%. Then 0.75 x 2.1% + 0.25 x 4.1% = 2.6%. The drop is mix, not a change in either device.

## Allowed wording

- "Conversion was 2.6% in October, down from 3.1% in September."
- "The fall is explained by a shift toward mobile sessions."

## Not allowed

- "The new page caused the drop." (cause)
- "Conversion will keep falling." (prediction)
- "This holds for all customers." (beyond the data)

## Common traps

- Comparing a partial period with a full one.
- Percent of a percent: say points, not percent, for rate changes.
- Averages hiding a bimodal distribution. Look at the distribution.
- Survivorship: only entities that still exist are counted.
