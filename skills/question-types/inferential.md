# Inferential questions

Ceiling: "associated with", with uncertainty, for the population the sample represents. Never "causes".

## Before any card

- **Population:** who do you want to speak about?
- **Sample:** how were these rows chosen? A survey of people who replied, or customers who stayed, is not a random sample. Say who is missing.
- **Unit:** one row per independent unit. Many rows per customer are not independent.

For the choice of test by data type, also apply the `stats-tests` skill. Core rule if it does not load: choose the test by data type and design, state its assumptions, report direction, magnitude and uncertainty.

## Card: confidence intervals

- **When to use:** any estimate from a sample that will be read as true for a wider group: a rate, a mean, a difference.
- **Data needed:** the sample at unit grain, and how it was drawn.
- **Key assumptions:** the sample is random or close to it. Units are independent.
- **Checks that must pass:**
  1. The interval is computed at the unit of sampling (customers, not order rows).
  2. For a rate near 0 or 1, or a small n, use a Wilson interval, not the normal approximation.
  3. The confidence level is stated (95% by default).
  4. The reader is told what the interval does not cover: bias from who is missing.
- **Common failure:** an interval on a full census (there is no sampling error, the uncertainty is elsewhere); reading it as "95% of customers fall in this range".
- **Claim allowed:** "An estimated 23% of subscribers use the feature (95% interval 20% to 26%), based on a random sample of 800."
- **Simplest version first:** estimate plus or minus 1.96 standard errors, when n is large.
- **Tool notes:** SQL: compute p and n, then `1.96 * sqrt(p * (1 - p) / n)`. Python: `statsmodels.stats.proportion.proportion_confint(method="wilson")`, `scipy.stats.t.interval`. Excel: `CONFIDENCE.T`, or the formula by hand.

## Card: t-test and Mann-Whitney

- **When to use:** compare a continuous outcome between two independent groups (order value for two plans).
- **Data needed:** one value per unit, and the group.
- **Key assumptions:** units are independent. For the t-test: means are a fair summary, and n is not tiny. For Mann-Whitney: the question is about a shift in the whole distribution.
- **Checks that must pass:**
  1. Plot both distributions first.
  2. Use Welch's t-test, not the equal-variance version.
  3. Heavy tails or strong skew: use Mann-Whitney, or bootstrap the difference in means. Say which question each answers (ranks or means).
  4. Before and after on the same units: use a paired test.
  5. Report the difference and its interval, not only p.
- **Common failure:** many rows per customer treated as independent; Mann-Whitney result reported as a difference in means; groups that differ in other ways read as a group effect.
- **Claim allowed:** "Annual-plan customers spent 6.20 more per month on average (95% interval 3.10 to 9.30). This is an association: the groups differ in other ways."
- **Simplest version first:** Welch's t-test with an interval.
- **Tool notes:** SQL: get n, mean and variance per group, then compute by hand. Python: `scipy.stats.ttest_ind(equal_var=False)`, `mannwhitneyu`. Excel: `T.TEST(range1, range2, 2, 3)`.

## Card: proportion and chi-square tests

- **When to use:** compare a rate between two or more groups (churned or not, converted or not).
- **Data needed:** counts of successes and totals per group, at unit grain.
- **Key assumptions:** each unit is counted once. Expected counts are at least 5 per cell.
- **Checks that must pass:**
  1. The denominators are units, not events.
  2. Small counts: use Fisher's exact test.
  3. More than two groups: a chi-square test says "some difference". Follow up with pairwise comparisons and a correction.
  4. Report the difference in points with an interval.
- **Common failure:** testing rates built from sessions when customers repeat; a significant chi-square read as "group A is best".
- **Claim allowed:** "Churn was 4.1% on the monthly plan and 2.9% on the annual plan, a 1.2 point difference (95% interval 0.6 to 1.8)."
- **Simplest version first:** a two-proportion z-test with an interval for the difference.
- **Tool notes:** SQL: counts per group. Python: `statsmodels.stats.proportion.proportions_ztest`, `confint_proportions_2indep`, `scipy.stats.chi2_contingency`, `fisher_exact`. Excel: `CHISQ.TEST`.

## Card: bootstrap

- **When to use:** you need an interval for something with no simple formula: a median, a ratio of sums, a percentile, revenue per customer with heavy tails.
- **Data needed:** the sample at the unit of sampling. A few hundred units or more.
- **Key assumptions:** the sample represents the population. Units are independent.
- **Checks that must pass:**
  1. Resample whole units (customers), not rows.
  2. Recompute the full statistic in every resample, including numerator and denominator.
  3. Use 2,000 resamples or more for an interval. Set a seed.
  4. Use the percentile interval by default. Look at the bootstrap distribution: if it is lumpy, the result leans on a few units.
- **Common failure:** resampling order rows when customers have many orders; using it on 30 units and trusting the result.
- **Claim allowed:** "Median days to second order was 19 (95% bootstrap interval 17 to 22)."
- **Simplest version first:** percentile bootstrap of one statistic.
- **Tool notes:** SQL: not a good fit. Export the unit-level table. Python: `scipy.stats.bootstrap`, or `rng.choice` in a loop with `np.percentile`. Excel: only for small cases, with a data table of resamples.

## Card: regression for association

- **When to use:** describe how an outcome varies with one factor while holding a few others fixed. Not for cause.
- **Data needed:** one row per unit, the outcome, the factor, and a short list of controls chosen before fitting.
- **Key assumptions:** units are independent. The form is roughly right (linear, or logistic for a yes or no outcome). No control is a result of the factor.
- **Checks that must pass:**
  1. The controls were chosen before looking at results, and listed.
  2. Plot residuals. Check for a few rows with outsized influence.
  3. Use robust standard errors. Cluster them when units repeat (many rows per customer).
  4. Check for strongly correlated predictors before reading single coefficients.
  5. Report the coefficient in plain units with an interval. For logistic regression, turn it into a difference in probability at typical values.
  6. Every coefficient is worded as "associated with".
- **Common failure:** reading a coefficient as the effect of changing the factor; adding controls until the result looks right; controlling for something the factor itself changes.
- **Claim allowed:** "Holding plan and sign-up month fixed, customers with the app installed are associated with 1.4 more orders per quarter (95% interval 1.1 to 1.7)."
- **Simplest version first:** the outcome on the factor alone, then add the listed controls once.
- **Tool notes:** SQL: build the unit-level table only. Python: `statsmodels.formula.api.ols(...).fit(cov_type="HC3")`, `logit`, `cov_type="cluster"`. Excel: `LINEST` or the Analysis ToolPak, for a first look only.

## Card: multiple-comparison correction

- **When to use:** more than one test in the same analysis: many metrics, many segments, many pairwise comparisons.
- **Data needed:** the full list of tests run, including the ones that showed nothing, and their p-values.
- **Key assumptions:** the list is complete. Hidden tests break the correction.
- **Checks that must pass:**
  1. The number of tests is written down.
  2. One primary comparison is named in advance and needs no correction. All others are corrected or labelled exploratory.
  3. Method stated: Bonferroni (simple, strict, for a few tests) or Benjamini-Hochberg (controls the false discovery rate, for many).
  4. Report adjusted p-values or adjusted thresholds.
- **Common failure:** 20 segments tested, one reported; correcting only the tests that made it into the readout.
- **Claim allowed:** "Of 12 segments tested, 2 differ after Benjamini-Hochberg correction at 5%. The others show no clear difference."
- **Simplest version first:** Bonferroni: divide alpha by the number of tests.
- **Tool notes:** SQL: none. Python: `statsmodels.stats.multitest.multipletests(method="fdr_bh")`. Excel: sort p-values, compare each to rank / m x alpha.

## Allowed wording

- "is associated with", "is higher among", "differs by", with an interval.
- "No clear difference. The data could detect a difference of X or more."

## Not allowed

- "causes", "leads to", "drives", "the effect of".
- "No difference." (when the interval is wide)
- "Significant" with no size.
