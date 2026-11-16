# Exploratory questions

Ceiling: "we see", "a pattern worth testing". Exploratory outputs are hypotheses, never findings.

## Rules for every card

- Count the slices you look at. Write the number down. Twenty looks will show one "interesting" result by chance.
- Say before you look what would count as a pattern worth testing (size and consistency).
- End with a list of hypotheses and, for each, the cheapest way to test it.
- Do not use "drives", "causes", "because of" or "confirmed".

## Card: segment scan

- **When to use:** a metric moved and you need to know where to look. "Why are sign-ups down?" with no design.
- **Data needed:** the metric at unit grain for two periods, with 3 to 10 segment dimensions.
- **Key assumptions:** segment definitions are the same in both periods. The descriptive checks (definition, final period, tracking) already passed.
- **Checks that must pass:**
  1. The dimensions were listed before the scan. The number of dimensions and segments looked at is written down.
  2. Each segment shows its size, its change, and its contribution to the total change (segment change divided by total change).
  3. Contributions sum to 100% within each dimension.
  4. Mix shift is separated from rate change (see the mix-shift card in `descriptive.md`).
  5. The top pattern holds in a second cut (another week, or one more dimension). If not, drop it.
- **Common failure:** reporting the largest percent change in a tiny segment; stopping at the first dimension that shows a gap; telling the timing story as the cause.
- **Claim allowed:** "We see 80% of the fall in one segment: paid social sign-ups on mobile. This is a pattern worth testing, not a confirmed cause."
- **Simplest version first:** one dimension at a time, ranked by contribution to the change.
- **Tool notes:** SQL: one query per dimension with period totals side by side, or `grouping sets`. Python: loop `groupby` over the dimension list and stack the results. Excel: one PivotTable per dimension.

## Card: metric decomposition (driver tree)

- **When to use:** a top-line metric moved and it is a product or sum of parts (revenue = customers x orders per customer x order value).
- **Data needed:** every component for both periods, from the same rows as the top-line metric.
- **Key assumptions:** the formula is exact, not a rough model. The parts multiply or add up to the total.
- **Checks that must pass:**
  1. The components recombine to the reported metric in both periods.
  2. The change is split across components with a stated method (for a product: change one factor at a time in a fixed order, or use logs). The parts sum to the total change.
  3. The tree stops at components the business can act on.
  4. Each branch that moved gets a segment scan before any story.
- **Common failure:** a tree whose parts do not sum; reading the tree as cause ("order value drove revenue") when it is arithmetic.
- **Claim allowed:** "Of the 9% fall in revenue, about 7 points come from fewer active customers and 2 points from lower order value. Orders per customer were flat."
- **Simplest version first:** two or three components, one level deep.
- **Tool notes:** SQL: one row per period with each component, then the recombined product as a check column. Python: a small frame, `np.log` differences for a product split. Excel: one column per component, a check cell for the product.

## Card: correlation

- **When to use:** "do these two things move together" across customers or over time.
- **Data needed:** paired values at one grain. At least 30 pairs. For time series, the series themselves and their changes.
- **Key assumptions:** units are independent. The relation is roughly monotonic. No shared trend is doing the work.
- **Checks that must pass:**
  1. Plot it. A scatter first, the number second.
  2. Use Spearman when either variable is skewed or has outliers.
  3. Give an interval, not only r.
  4. For two time series, correlate the changes (differences), not the levels. Two series that both grow will correlate at 0.9 for no reason.
  5. Check one obvious third variable (customer age, plan, season).
  6. Count how many pairs of variables were tried.
- **Common failure:** correlation told as cause; a trend in both series; one outlier making the whole result; a range restricted to survivors.
- **Claim allowed:** "Customers who use the app more weeks per month have higher 6-month retention (Spearman 0.34, 95% interval 0.29 to 0.39). This does not show that usage causes retention."
- **Simplest version first:** one scatter and Spearman's rank correlation.
- **Tool notes:** SQL: `corr(x, y)` gives Pearson in most dialects. Python: `scipy.stats.spearmanr`, `pearsonr` (with `confidence_interval()`), `df.diff()` for changes. Excel: `CORREL`, and `RANK.AVG` first for Spearman.

## Short card: clustering

- **When to use:** you want groups of similar customers and have no labels. For ideas and naming, not for proof.
- **Key assumption:** the features and their scaling define "similar". Change them and the clusters change.
- **Key check:** the clusters are stable: rerun with another seed and on a random half. Do the same groups come back? Can each be described in one plain sentence that the business recognises?
- **Claim allowed:** "One useful way to group customers is ...". Not "there are four types of customer".

Get a specialist review before shipping.

## Short card: anomaly detection

- **When to use:** flag unusual days or accounts for a person to look at.
- **Key assumption:** "normal" is well described by the history used, including weekday and season.
- **Key check:** run it on a past period where the true incidents are known. How many did it catch, and how many false alarms per week did it raise?
- **Claim allowed:** "These 6 days were unusual against the last 12 weeks." Not "something went wrong on these days".

Get a specialist review before shipping.
