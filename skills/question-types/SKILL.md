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
| `predictive.md` | naive and seasonal-naive baselines; linear and logistic regression; forecasting (ETS, ARIMA); backtesting and cross-validation; leakage checks | gradient boosting; calibration |
| `causal.md` | difference-in-differences; interrupted time series | regression discontinuity; synthetic control; instrumental variables; matching and weighting; uplift |
| `experiment.md` | randomised experiment (A/B) | |
| `mechanistic.md` | | one short note |

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
- Planning: pick the method with the selectors above. Name the card in the plan. Copy its "Checks that must pass" into the success checks. If the type cannot support the decision, say so now, not at the end.
- Running: load the card. Run every check under "Checks that must pass" and log pass or fail. A failed check lowers the claim allowed.
- Writing claims: every finding gets direction, magnitude, uncertainty, and the ceiling applied. Use the card's "Claim allowed" wording.
- Reviewing: check the analysis against the card's "Checks that must pass". Flag every sentence whose wording is above the ceiling, and quote it.

## Rule of thumb

If the decision needs "why" and the data only supports "what", say that plainly and propose the cheapest way to get a stronger answer, such as a test.

## Names and sources

Use only company, product, table and source names the user has said in this conversation. If one is missing, ask. Never call a data tool before the user names the source it applies to.
