# Dashboards

A dashboard is several charts that answer a standing question for a named reader. Design it on paper first. Then build it with the tool file (`python.md`, `excel.md`, `tableau.md` or `powerbi.md`).

## Before any chart

Ask, in one round, what you do not know:

1. **Who reads it, and how often?** A weekly exec glance and a daily analyst tool are different pages.
2. **What decision or habit does it serve?** "Monday review of sign-ups and churn." If there is none, a one-off readout is the better output.
3. **Which metrics?** Each needs an agreed definition. Use the Metrics section of the data map. If a definition is missing, settle it first (apply the `metric-design` skill; core rule: a metric needs a formula, grain, population, owner, guardrails and a trusted number).

## Layout

- **Top row:** 3 to 5 headline numbers. Each with its period, its comparison (previous period, same period last year) and the change in the right unit (points for rates).
- **Middle:** one trend per headline metric. Same time axis on all of them.
- **Below:** the 1 or 2 breakdowns the reader asks for most (by channel, by plan). Small multiples over one crowded chart.
- **Bottom or a second page:** detail tables.
- One screen for the main view. Most important top left.
- At most about 8 charts per page. A chart nobody would miss comes off.

## Rules

1. Every chart passes the checks in this skill's `SKILL.md`. Titles on a dashboard name the metric and the period, because the takeaway changes with the data. Put the takeaway in a short text line you update, or leave it out. Never leave a stale takeaway.
2. **Definitions on the page.** Each metric has its definition one click or one line away. Same name as in the data map.
3. **Freshness on the page.** "Data to: <date>. Updated: <time, time zone>." Mark the last period as partial when it is.
4. **Filters are few and visible.** State the default of each. A filter must change every chart it claims to, or say which it does not.
5. **Same scale when comparing.** Panels that sit side by side share axes.
6. **Totals reconcile.** The headline number equals the sum of its breakdown, or the page says why not (an "unknown" group, overlapping segments).
7. **Reconcile before release.** Check each headline number against the trusted number in the data map, for one closed period. Apply the `validation-ladder` skill. Core rule if it does not load: one entity, one entity-day, many entities, aggregates, then reconcile to a trusted number.
8. **No row-level personal data** on a shared dashboard without asking.
9. **Colour means one thing.** One colour per series across the whole page. A good-or-bad colour only where direction is agreed, and never red against green alone.
10. **No causal wording.** An annotation says "price change went live", not "the price change caused this".

## Build

- A self-contained HTML page (Python with plotly): one file, data embedded as aggregates only, filters as dropdowns. Save it under `outputs/` when it belongs to an analysis.
- Excel, Tableau, Power BI: hand-over mode. Give the layout as a numbered build list, one chart at a time, then the checks to run.
- Give the reader a short "how to read this" note: what each number means, how fresh it is, who owns it.

## Review checklist for an existing dashboard

Purpose and reader stated. Definitions and freshness on the page. Headline numbers reconcile. Every chart passes the chart checks. Filters visible and consistent. Partial periods marked. No stale takeaway text. Report only the fails.
