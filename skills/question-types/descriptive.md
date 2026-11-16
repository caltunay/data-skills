# Descriptive questions

Ceiling: what happened, for the data observed. Not why. Not what will happen.

Every card ends at the same place: reconcile to a trusted number before reporting.

## Before any card

1. **Define the metric.** Numerator, denominator, population, time window, time zone. Match the data map definition.
2. **Is the move real?** Rule out tracking changes, outages, late data, definition changes and one-off days.
3. **Is the period final?** Late-arriving rows make the last days look low.

## Card: counts and rates

- **When to use:** "how many" and "what share". One number or one number per period.
- **Data needed:** one row per entity or event, a status, a timestamp. For a rate: a numerator and a denominator from the same population.
- **Key assumptions:** the key is unique at the stated grain. The denominator holds everyone who could be in the numerator.
- **Checks that must pass:**
  1. Count distinct keys, not rows, unless rows are the grain.
  2. Numerator and denominator share filters, dates and time zone.
  3. The total reconciles to a trusted number within the stated tolerance.
  4. A rate change is given in points, not percent of a percent.
- **Common failure:** a join fans out and doubles the count; the denominator is all customers while the numerator is active customers only.
- **Claim allowed:** "Paid orders were 41,820 in October." "Conversion was 2.6%, down 0.5 points from September."
- **Simplest version first:** one filtered count. Add splits only when asked.
- **Tool notes:** SQL: `count(distinct order_id)`, cast before dividing. Python: `nunique()`, `value_counts(normalize=True)`. Excel: PivotTable with distinct count, or `COUNTA(UNIQUE())`.

## Card: means and medians

- **When to use:** "typical" value of an amount or a duration (order value, days to first order).
- **Data needed:** one row per unit with the value. Know whether zeros are included.
- **Key assumptions:** the unit of the average is the unit the decision cares about (per order or per customer are different numbers).
- **Checks that must pass:**
  1. Look at the distribution first. If it is skewed or has two peaks, report the median and percentiles (p25, p75, p90) too.
  2. State whether zeros and nulls are in or out.
  3. Never average pre-computed averages. Recompute from sums and counts.
  4. Check the top 1% of values by hand. Decide on outliers in writing.
- **Common failure:** a few large orders move the mean; an average of segment averages ignores segment size.
- **Claim allowed:** "Median order value was 38. The mean was 52, pulled up by a small number of large orders."
- **Simplest version first:** median plus mean, side by side.
- **Tool notes:** SQL: `avg`, and `percentile_cont(0.5)` or the dialect's median. Python: `describe()`, `quantile()`. Excel: `MEDIAN`, `PERCENTILE.INC`.

## Card: rolling windows (7-day, 28-day)

- **When to use:** a daily series is noisy or has a weekly pattern, and you need the level or trend.
- **Data needed:** a complete daily series with no missing dates.
- **Key assumptions:** every window holds the same number of each weekday (7 or 28 days, not 30).
- **Checks that must pass:**
  1. Fill missing dates with zero or null on purpose, before the window.
  2. Drop or flag windows that are not full (the first 6 or 27 days).
  3. For a rolling rate, roll the numerator and the denominator separately, then divide.
  4. Say which date the window is anchored on (the last day).
- **Common failure:** a rolling average of daily rates weights quiet days as much as busy days; a 30-day window drifts with weekday mix.
- **Claim allowed:** "The 7-day average of sign-ups was 1,240 on 31 March, down from 1,510 on 28 February."
- **Simplest version first:** 7-day sum or average. Use 28-day only when 7-day is still noisy.
- **Tool notes:** SQL: `sum(x) over (order by day rows between 6 preceding and current row)`. Python: `rolling(7).sum()` on a date-indexed frame after `asfreq("D")`. Excel: `AVERAGE` over a 7-row range.

## Card: week-on-week and year-on-year with seasonality

- **When to use:** "is it up or down" against an earlier period.
- **Data needed:** at least the comparison period. For year-on-year, 13 months or more.
- **Key assumptions:** the two periods are comparable: same length, same weekdays, same definition, both final.
- **Checks that must pass:**
  1. Compare full periods with full periods. Never a partial week with a full one.
  2. Align weekdays (compare to the same weekday 52 weeks back, not the same date).
  3. Note moving events: public holidays, sales, pay days, a leap day.
  4. Show both week-on-week and year-on-year when a seasonal pattern is likely. A fall on last week can be normal for the season.
  5. Check that the definition and tracking were the same in both periods.
- **Common failure:** calling a seasonal dip a problem; comparing a month with 5 weekends to one with 4.
- **Claim allowed:** "Sign-ups were 12% lower than the same four weeks last year, and 3% lower than the previous four weeks."
- **Simplest version first:** same period last year, aligned by weekday.
- **Tool notes:** SQL: self-join on `day - interval '364 days'`, or `lag(x, 52)` on a weekly series. Python: `shift(52)` on weekly data, `pct_change()`. Excel: `XLOOKUP` to the date 364 days earlier.

## Card: cohort tables

- **When to use:** behaviour over a customer's lifetime: retention, repeat purchase, churn by sign-up month.
- **Data needed:** one row per customer with a cohort date, plus dated activity.
- **Key assumptions:** the cohort date is fixed per customer. Activity is measured by age (months since start), not calendar month.
- **Checks that must pass:**
  1. Each customer is in exactly one cohort.
  2. Period 0 is 100% (or the definition says why not).
  3. Cells where the cohort has not yet had the full period are blank, not low.
  4. The cohort sizes sum to the trusted customer count.
  5. State whether retention is "active in period n" or "still active by period n". They differ.
- **Common failure:** young cohorts look worse because their last period is incomplete; reactivated customers counted twice.
- **Claim allowed:** "Month-3 retention was 41% for the January cohort and 36% for the February cohort."
- **Simplest version first:** monthly cohorts, months 0 to 6, one metric.
- **Tool notes:** SQL: compute `age_month` from cohort date and activity date, then `count(distinct customer_id)` by cohort and age. Python: `pivot_table(index="cohort", columns="age_month")`. Excel: PivotTable with cohort in rows and age in columns.

## Card: funnels

- **When to use:** where do people drop between ordered steps (visit, sign-up, first order).
- **Data needed:** one row per unit with a timestamp for each step reached.
- **Key assumptions:** the steps have an order. The unit is the same at every step (customer or session, not a mix).
- **Checks that must pass:**
  1. Each step counts only units that reached the step before it, within a stated time window.
  2. Counts never rise from one step to the next. If they do, the definition is wrong.
  3. The same unit and the same entry period are used at every step.
  4. State both step conversion and overall conversion.
  5. Recent entrants have had less time to convert. Cut the entry period so all have had the full window.
- **Common failure:** mixing sessions and customers; reading a drop as "the step is broken" (that is a causal claim).
- **Claim allowed:** "62% of sign-ups in March placed a first order within 14 days, down from 68% in February. The largest drop was between sign-up and first basket."
- **Simplest version first:** three or four steps, one entry cohort, one window.
- **Tool notes:** SQL: one CTE per step, each joined to the step before on the unit key with a time condition. Python: boolean columns per step, then `mean()`. Excel: `COUNTIFS` per step.

## Card: segment breakdowns

- **When to use:** "where is it": split a metric by platform, country, channel, plan, new or returning.
- **Data needed:** the metric at unit grain with segment columns. Segment values as they were at the time, not as they are now.
- **Key assumptions:** segments do not overlap and cover everyone.
- **Checks that must pass:**
  1. Segment counts sum to the total. An "unknown" segment is shown, not dropped.
  2. Each segment shows its size next to its rate.
  3. Segments were chosen before looking, or the result is labelled exploratory.
  4. Small segments are flagged (wide uncertainty).
- **Common failure:** picking the one segment that moved after trying twenty; a segment attribute that changed over time.
- **Claim allowed:** "The fall was concentrated in paid social sign-ups: down 31%. Other channels were within 3% of February."
- **Simplest version first:** one dimension at a time, largest segments first.
- **Tool notes:** SQL: `group by` with `count` and the rate, plus a total row from a second query. Python: `groupby().agg()`. Excel: PivotTable with "show values as % of column total".

## Card: mix-shift decomposition

- **When to use:** an overall rate moved. Did the segments change, or did the mix of segments change?
- **Data needed:** for two periods, each segment's size (share) and rate.
- **Key assumptions:** the segments cover everyone in both periods with the same definition.
- **Checks that must pass:**
  1. The blended rate from shares and segment rates equals the reported overall rate in both periods.
  2. Split the change into: mix effect (share change x old rate), rate effect (rate change x new share). The parts sum to the total change.
  3. Say which segment dimension was used. Another dimension can tell another story.
- **Common failure:** Simpson's paradox: every segment is flat or up while the total is down. Reporting the total as a performance drop.
- **Claim allowed:** "Conversion fell from 3.1% to 2.6%. Device rates did not change. The fall is explained by a shift toward mobile sessions, from 52% to 75%."
- **Simplest version first:** two segments, two periods, by hand: 0.52 x 2.1% + 0.48 x 4.1% = 3.1%, then 0.75 x 2.1% + 0.25 x 4.1% = 2.6%.
- **Tool notes:** SQL: one row per segment and period with share and rate, then compute the two effects. Python: a small frame with `share` and `rate` columns. Excel: `SUMPRODUCT(shares, rates)`.

## Card: index to baseline

- **When to use:** compare series of very different sizes on one chart, or show change since a start point.
- **Data needed:** each series with a value at the baseline period.
- **Key assumptions:** the baseline period is typical, not a spike or a dip.
- **Checks that must pass:**
  1. State the baseline period and why it was chosen.
  2. The baseline value is not tiny (a small base makes huge index moves).
  3. Show the real values somewhere, not only the index.
  4. Try one other baseline. If the story flips, say so.
- **Common failure:** choosing the baseline that makes the story; reading index 150 against index 120 as "bigger" when the real sizes are 30 and 12,000.
- **Claim allowed:** "Indexed to January (100), annual-plan sign-ups reached 138 in March and monthly-plan sign-ups 92."
- **Simplest version first:** index = value / baseline value x 100, one baseline.
- **Tool notes:** SQL: `x / first_value(x) over (partition by series order by period) * 100`. Python: `df / df.iloc[0] * 100`. Excel: divide by an absolute reference to the baseline cell.

## Allowed wording

- "Conversion was 2.6% in October, down from 3.1% in September."
- "The fall is explained by a shift toward mobile sessions."

## Not allowed

- "The new page caused the drop." (cause)
- "Conversion will keep falling." (prediction)
- "This holds for all customers." (beyond the data)

Matching dates are a lead, not a cause. Line the timing up with releases, campaigns and price changes, then say "started the same week as", never "because of".
