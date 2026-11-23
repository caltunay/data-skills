---
name: question-types
description: Name the question type of a data analysis, apply its claim ceiling, and pick the method card to use. Applies inside the data-skills flow when an analysis is framed, planned, run or reviewed, and whenever a conclusion from data is about to be worded as "caused", "drives", "predicts" or "proves".
---

# Question types and claim ceilings

A claim never goes above what its method supports.

## Core rule

Six question types, each with a ceiling. Name the type early. Word every claim at or below the ceiling. Say "caused" only with a randomised experiment or a credible causal design that passed its checks. One file per type holds that type's method cards. Load only the file for the type in use.

## The six types

| Type | Asks | Allowed claims | Not allowed |
|---|---|---|---|
| Descriptive | What happened? | "was", "is", counts, rates for the data observed | Generalising beyond the data; "why" |
| Exploratory | What patterns are there? | "we see", "pattern worth testing" | "drives", "causes", confirmed findings |
| Inferential | Does it hold beyond this sample? | "associated with", with uncertainty | "causes" |
| Predictive | What will happen for a new case? | "predicts", with out-of-sample performance | Explaining why; "causes" |
| Causal | What happens if we change X? | "caused", "effect of" only with a randomised experiment or a credible causal design that passed its checks | Causal language from observational data without a design |
| Mechanistic | How exactly does it work? | Rarely reachable in business work. Flag it. | Most claims |

## Type selector

Ask what the decision needs, then pick the lowest type that answers it.

| The ask sounds like | Type | File |
|---|---|---|
| "How many", "what was", "how did it change", "where is it down" | Descriptive | `descriptive.md` |
| "What is going on", "any patterns", "why is it down" with no design | Exploratory | `exploratory.md` |
| "Is this difference real", "does it hold for all customers", survey or sample to population | Inferential | `inferential.md` |
| "What will", "who is likely to", "forecast" | Predictive | `predictive.md` |
| "Did X work", "what happens if we change X", "impact of" | Causal | `causal.md`, and `experiment.md` for a randomised test |
| "How exactly does X lead to Y" | Mechanistic | `mechanistic.md` |

A "why" question starts as descriptive, then exploratory. It becomes causal only when a design from the causal method selector fits. Say this to the user when you set the type.

Exploratory outputs are hypotheses, never findings.

## Causal method selector

Go down the list. Take the first that fits. Then open `causal.md` (or `experiment.md`) and load that card.

1. Randomised assignment? Use an A/B test: `experiment.md`.
2. Rollout to several units, with a comparison group and a pre-period? Use difference-in-differences.
3. Assignment by a cut-off on a score or threshold? Use regression discontinuity.
4. One treated unit (a region, a market) and several untreated ones? Use synthetic control.
5. One time series with a known change date and no comparison group? Use interrupted time series.
6. A variable that moves treatment but not the outcome directly? Use instrumental variables.
7. Observational data with rich pre-treatment covariates? Use matching or weighting.
8. The question is who to treat, not whether it works? Use uplift.
9. None fits? Say so. Give the ceiling the data supports. Offer the best descriptive path.

When two seem to fit:

- Only one treated unit: not 2. Go to 4.
- Units got the treatment by a score cut-off: not 2. Go to 3.
- Units chose the treatment themselves (they installed, opted in, upgraded): not 2. Go to 6, 7 or 9.
- A randomised nudge exists but the question is about the thing it nudges: 6, not 1.

Pre-post with no control and no long series: at most "Y changed after X". Not "X caused Y". Ask what else changed at the same time.

## Method cards

Plain models know what each method is. They fail at choosing the method, checking its assumptions and overclaiming. The cards cover exactly that.

Full card format: When to use, Data needed, Key assumptions, Checks that must pass, Common failure, Claim allowed, Simplest version first, Tool notes.

Short card format (advanced methods): When to use, Key assumption, Key check, Claim allowed, and sometimes a one-line tool note. Every short card ends with "Get a specialist review before shipping." Treat that line as a requirement and repeat it to the user.

| File | Full cards | Short cards |
|---|---|---|
| `descriptive.md` | counts and rates; means and medians; rolling windows; week-on-week and year-on-year; cohort tables; funnels; segment breakdowns; mix-shift decomposition; index to baseline | |
| `exploratory.md` | segment scan; metric decomposition (driver tree); correlation | clustering; anomaly detection |
| `inferential.md` | confidence intervals; t-test and Mann-Whitney; proportion and chi-square tests; bootstrap; regression for association; multiple-comparison correction | |
| `predictive.md` | naive and seasonal-naive baselines; linear and logistic regression; forecasting (ETS, ARIMA); backtesting and cross-validation; leakage checks; gradient boosting; classification metrics; calibration | |
| `causal.md` | difference-in-differences; interrupted time series | regression discontinuity; synthetic control; instrumental variables; matching and weighting; uplift |
| `experiment.md` | randomised experiment (A/B) | |
| `mechanistic.md` | | one short note |

## Compact cards (fallback when the type files cannot be opened)

Use these when the type file will not open (for example, a chat with no file access). The full cards in the type files win when they can be read. Every method has one line for each of: when to use, checks that must pass, claim allowed.

### Descriptive

| method | when to use | checks that must pass | claim allowed |
|---|---|---|---|
| counts and rates | "how many", "what share" | distinct keys not rows; numerator and denominator share filters, dates and time zone; total reconciles; rate changes in points | "X was N in the period" |
| means and medians | the typical value of an amount or duration | look at the distribution first; median and percentiles if skewed; zeros and nulls in or out stated; never average averages; top 1% checked | "median was M; mean was N, pulled up by a few large values" |
| rolling windows | a noisy daily series or a weekly pattern | fill missing dates on purpose; flag windows that are not full; roll numerator and denominator separately; state the anchor day | "the 7-day average was N on date D" |
| week-on-week and year-on-year | "is it up or down" against an earlier period | full periods only; align weekdays; note holidays and moving events; show both comparisons when seasonality is likely | "N% lower than the same weeks last year, M% lower than the prior weeks" |
| cohort tables | behaviour over a customer's lifetime | one cohort per customer; period 0 is 100%; unfinished cells blank; cohort sizes sum to the trusted count; "active in" vs "still active by" stated | "month-3 retention was N% for cohort C" |
| funnels | where people drop between ordered steps | each step counts only units from the step before, in a stated window; counts never rise; same unit and entry period at every step; step and overall conversion; recent entrants given time | "N% reached step B, down from M%; the largest drop was between A and B" |
| segment breakdowns | "where is it": split by platform, channel, plan | segments sum to the total, "unknown" shown; size next to each rate; segments chosen before looking; small segments flagged | "the fall was concentrated in segment S" |
| mix-shift decomposition | a blended rate moved: segment rates or segment mix? | blended rate matches the reported rate in both periods; mix and rate effects sum to the change; dimension stated | "rates did not change; the fall is explained by a shift in mix" |
| index to baseline | series of very different sizes, or change since a start | baseline stated and not tiny; real values shown too; a second baseline tried | "indexed to period P (100), A reached N" |

### Exploratory

| method | when to use | checks that must pass | claim allowed |
|---|---|---|---|
| segment scan | a metric moved, where to look, no design | dimensions listed before the scan and counted; size, change and contribution per segment; contributions sum to 100%; mix separated from rate | "we see most of the fall in segment S; a pattern worth testing" |
| metric decomposition (driver tree) | a top-line metric that is a product or sum of parts | components recombine in both periods; change split by a stated method and sums to total; stop at parts the business can act on | "of the N% fall, A points come from part X" |
| correlation | do two things move together | scatter first; Spearman if skewed; interval not only r; correlate changes for time series; one third variable checked | "X and Y move together (r, interval); this does not show cause" |
| clustering (short card) | groups of similar customers, no labels | clusters stable across seeds and a random half; each describable in one sentence | "one useful way to group customers is ...". Specialist review |
| anomaly detection (short card) | flag unusual days or accounts for a person | tested on a past period with known incidents: catches and false alarms counted | "these days were unusual against the last N weeks". Specialist review |

### Inferential

| method | when to use | checks that must pass | claim allowed |
|---|---|---|---|
| confidence intervals | a sample estimate read as true for a wider group | interval at the unit of sampling; Wilson for rates near 0 or 1 or small n; level stated; bias from who is missing named | "an estimated N% (95% interval A to B)" |
| t-test and Mann-Whitney | a continuous outcome in two groups | plot first; Welch not equal variance; Mann-Whitney or bootstrap for skew; paired test for same units; difference with interval | "group A was N higher (interval); an association" |
| proportion and chi-square tests | a rate across two or more groups | units not events in denominators; Fisher for small counts; pairwise follow-up with correction; difference in points with interval | "a N point difference (interval)" |
| bootstrap | an interval with no simple formula | resample whole units; recompute the full statistic each time; 2,000+ resamples with a seed; look at the distribution | "median M (95% bootstrap interval A to B)" |
| regression for association | how an outcome varies with one factor, holding a few fixed | controls listed before results; residuals and influence checked; robust or clustered errors; correlated predictors checked | "holding P fixed, X is associated with N more Y (interval)" |
| multiple-comparison correction | many metrics, segments or pairwise tests | number of tests written down; one primary named in advance; method stated; adjusted values reported | "of N tested, K differ after correction" |

### Predictive

| method | when to use | checks that must pass | claim allowed |
|---|---|---|---|
| naive and seasonal-naive baselines | always first, the bar every model must beat | scored on the same held-out periods; error metric stated; for yes or no, base rate and the current rule | "the baseline error is N%; any model must beat it" |
| linear and logistic regression | the first real model | split by time; leakage checks pass; beats the baseline on held-out data; precision and recall at the chosen threshold; coefficients not read as causes | "predicts Y with held-out score S, against B for the current rule" |
| forecasting (ETS, ARIMA) | a regular series several periods ahead | rolling-origin backtest at the needed horizon; beats seasonal-naive; residuals show no pattern; prediction interval coverage checked | "we forecast N (80% interval A to B); backtest error E" |
| backtesting and cross-validation | every time a model score is reported | time-ordered splits; one customer on one side; preprocessing fitted inside each fold; final holdout touched once | "across K backtests, error was A to B" |
| leakage checks | before trusting any model score | no feature restates the outcome; every feature dated before prediction time; split by time; no fitting on the holdout | none alone; allows the held-out score to be reported |
| gradient boosting | many features, interactions, after a simple model | leakage checks pass; beats the simple model on a time-ordered holdout by a margin that matters; tuning on folds only | "predicts Y with held-out score S"; importance is not cause |
| classification metrics | any yes or no model, before choosing a threshold | base rate next to every metric; precision and recall at the threshold with counts; PR-AUC for rare outcomes; threshold from cost | "flags N%; precision P, recall R; base rate B" |
| calibration | the predicted probability itself is used | reliability curve on held-out data; Brier or calibration error against the base-rate baseline; any recalibration fitted on separate data; rechecked when the base rate shifts and by key segment | "a score of 0.3 means about a 30% chance", only after the curve passes |

### Causal and experiment

| method | when to use | checks that must pass | claim allowed |
|---|---|---|---|
| randomised experiment (A/B) | the change can be assigned at random | sample ratio mismatch test; design held (metric, size, run length); no peeking; power for the MDE; unit of analysis equals unit of randomisation; full weekly cycles; one primary metric, others corrected; guardrails; novelty by week | "the variant increased Y by N (interval) in this test, for these customers, in this period" |
| difference-in-differences | rollout to some units, comparison group and pre-period | parallel pre-trends; placebo date near zero; placebo outcome near zero; other events listed and checked; errors clustered by unit; staggered rollout handled | "increased Y by N (interval), assuming parallel trends" |
| interrupted time series | one series, a known change date, no comparison | plot with projected pre-trend; other events listed and checked; seasonality handled; autocorrelation handled; placebo date shows no jump; lag stated in advance | "Y rose N against the pre-trend; another cause cannot be ruled out" |
| regression discontinuity (short card) | treatment by a cut-off on a score | plot at the cut-off; no bunching; covariates do not jump; stable across bandwidths | "caused", near the cut-off only. Specialist review |
| synthetic control (short card) | one treated unit, several untreated, long pre-period | close pre-period fit; placebo runs show the gap is unusual; robust to dropping the top donor | "caused" for that unit, with the placebo rank. Specialist review |
| instrumental variables (short card) | a random nudge moves the treatment | strong first stage (F well above 10); no other path argued and attacked | "caused" for compliers only. Specialist review |
| matching and weighting (short card) | observational data with rich pre-treatment covariates | balance after matching (SMD under 0.1); overlap; no extreme weights; sensitivity analysis | "estimated effect, assuming no unmeasured confounding". Specialist review |
| uplift (short card) | who to treat, not whether it works | average effect first; scored on a held-out randomised sample; segments re-tested | "ranks customers by predicted response". Specialist review |

### Mechanistic

| method | when to use | checks that must pass | claim allowed |
|---|---|---|---|
| mechanistic note | "how exactly does X lead to Y" | every link needs its own causal evidence; usually not reachable, so flag it and fall back | the fallback type's claim, plus "one possible explanation, not tested". Specialist review |

## Must-answer questions by type

Ask these before work starts, and check them in review.

- Descriptive: what is the exact definition and population? Is the period final? What is the trusted number to reconcile to?
- Exploratory: how many slices were tried? What would count as a pattern worth testing?
- Inferential: what is the population, and how was the sample drawn? What is the interval?
- Predictive: what is the holdout? What beats the simple baseline? What does an error cost?
- Causal: what is the control? Was assignment random? What else changed at the same time?
- Mechanistic: can the mechanism be observed directly, or only inferred? If only inferred, drop the claim.

## Using it in each step

- Grilling: confirm the type with the user. Write it into the Meta section of `analysis.md`.
- Planning: pick the method with the selectors above. Name the card in the plan. Copy its "Checks that must pass" into the success checks now, at plan time, word for word. Never defer them to the run. If the type file will not open, copy them from the compact cards above. If the type cannot support the decision, say so now, not at the end.
- Running: load the card. Run every check under "Checks that must pass" and log pass or fail. A failed check lowers the claim allowed.
- Writing claims: every finding gets direction, magnitude, uncertainty, and the ceiling applied. Use the card's "Claim allowed" wording.
- Reviewing: check the analysis against the card's "Checks that must pass". Flag every sentence whose wording is above the ceiling, and quote it.

## Rule of thumb

If the decision needs "why" and the data only supports "what", say that plainly and propose the cheapest way to get a stronger answer, such as a test.

## Names and sources

Use only company, product, table and source names the user has said in this conversation. If one is missing, ask. Never call a data tool before the user names the source it applies to.
