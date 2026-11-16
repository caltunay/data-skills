---
name: viz
description: Choose, build or check a chart for an analysis in the data-skills flow. Applies when /run-analysis saves a chart to outputs/, /review-analysis checks one, or /storytell suggests one. Covers chart choice by question and a fixed list of chart checks. Not for a one-off chart request outside the flow.
---

# Viz

A chart answers one question. Pick the chart from the question, then run the checks.

Experimental (v0.2).

## Core rule

Choose the chart by the question it answers. The title states the takeaway. Axes carry labels and units. Bars start at zero. Show uncertainty where it exists. No dual axes, no 3D. Colour-blind safe. Same scale when comparing.

## Step 1: what is the question?

| Question | Chart | Notes |
|---|---|---|
| Trend: how did it change over time? | Line | Time on the x-axis, evenly spaced. Up to about 5 lines, then small multiples |
| Comparison: which is bigger? | Bar, sorted | Horizontal bars for long labels. Dot plot when zero is not meaningful |
| Distribution: how is it spread? | Histogram, or box plot across groups | Show the median. Say the bin width |
| Part of whole: what share? | Stacked bar, or one sorted bar chart of shares | Pie only for 2 or 3 parts. Never several pies side by side |
| Relationship: do two measures move together? | Scatter | Add a trend line only with its uncertainty. Many points: lower the opacity or bin |
| Funnel: where do people drop? | Horizontal bars, one per step, in step order | Label each step with its count and its step conversion |
| Cohort: how does behaviour change with age? | Cohort heatmap, or one line per cohort by age | Blank cells for periods a cohort has not reached. Never zero |

One chart, one question. If a chart needs a paragraph to explain it, split it.

## Step 2: checks

Run all of them on every chart, built or reviewed. Log a fail with the fix.

1. **The title states the takeaway.** "Sign-ups fell 15% in March", not "Sign-ups by month". The takeaway stays at or below the claim ceiling of the analysis. No "caused" in a title unless the analysis supports it.
2. **Axes are labelled, with units.** Currency, percent or points, per day or per week. The time zone if it matters.
3. **Bars start at zero.** A bar's length is its value. A line chart may use a non-zero baseline. If it does, say so on the chart.
4. **Uncertainty is shown where it exists.** Error bars or a band for estimates from a sample, a test or a forecast. Say what the band is (95% interval). Exact counts need none.
5. **No dual axes.** Two scales on one chart let the author pick any story. Use two charts, stacked, with a shared x-axis. Or index both series to a baseline.
6. **Colour-blind safe.** Do not rely on red against green. Use a palette built for it (for example Okabe-Ito, or viridis for ordered data). Colour is never the only signal: add direct labels, markers or line styles.
7. **No 3D.** No perspective, no shadows, no gradients that carry no data.
8. **Small multiples over cluttered legends.** More than about 5 series: one small panel per series, same axes. Label lines directly where you can.
9. **Same scale when comparing.** Panels meant to be compared share their axes. If they cannot, say so in the title of each.
10. **Partial periods are marked or cut.** An unfinished last week or month looks like a drop.
11. **The source and the filters are stated.** One line under the chart: the data, the period, the main filters, and n where it matters.
12. **Sorted on purpose.** Bars by value, unless the categories have a natural order (time, funnel steps, age bands).

## Step 3: use the tool file

Read only the file for the tool in use.

- Python (matplotlib or plotly): `python.md`
- Excel: `excel.md`
- Tableau: `tableau.md`
- Power BI: `powerbi.md`
- A dashboard (several charts with filters): `dashboard.md`, then the tool file

Excel, Tableau and Power BI always run in hand-over mode. Give numbered steps. The user builds the chart and pastes or describes what they see. Apply the `run-or-hand-over` skill. Core rule if it does not load: run or save if you can, else offer a download, else print it and wait.

## Where charts go

- `/run-analysis` saves charts under `outputs/` in the analysis folder, only when asked or when the plan names one. File names say what the chart shows (`signups-by-channel-feb-mar.png`).
- Charts show aggregates. Ask before a chart exposes row-level data (one point per customer with an identifier).
- In a chat app, offer the chart as a download and say where it belongs.

## Reviewing a chart

For each chart: name the question it answers, then go down the 12 checks. Report only the fails, each with the fix. If all pass, say "Chart checks pass". Do not invent issues. Do not restyle for taste.

## Wording under a chart

Apply the `question-types` skill. Core rule if it does not load: a claim never goes above what its method supports, and no "caused" without a randomised experiment or a credible causal design that passed its checks. A chart of two lines moving together is not evidence of cause.

## Names and sources

Use only company, product, table and source names the user has said in this conversation. If one is missing, ask. Never call a data tool before the user names the source it applies to.
