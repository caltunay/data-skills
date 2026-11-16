format: v1

# Data map

Invented example. Shared by the team. Every entry carries `verified: YYYY-MM-DD` and `source: setup` or `source: analyses/<slug>`.
Entries older than 90 days, or contradicted by data, must be re-confirmed before use.

## 1. Sources

| name | type | dialect | access mode | verified | source |
|---|---|---|---|---|---|
| example_files | file (CSV in `data/`) | SQLite (loaded by `examples/run_queries.py`) | connected | 2026-01-26 | setup |

## 2. Tables

| table | one row means (grain) | primary key | key columns | notes | verified | source |
|---|---|---|---|---|---|---|
| assignments | one visitor assigned to a test arm | visitor_id | arm, assigned_ts, device, is_internal | assigned_ts is UTC. Assignment is random, 50/50, by visitor | 2026-01-26 | setup |
| orders | one order | order_id | visitor_id, order_ts, amount, status, is_returned | status is paid or cancelled. amount is gross | 2026-01-26 | setup |
| platform_counts | one test arm | arm | visitors_assigned | export of the experiment platform's exposure counts. Includes internal visitors | 2026-01-26 | setup |

## 3. Joins

| left | right | keys | safe or trap | note | verified | source |
|---|---|---|---|---|---|---|
| assignments | orders | visitor_id | trap | one to many. 166 of 961 ordering visitors have more than one order. Aggregate orders to the visitor first | 2026-02-25 | analyses/2026-02-24-pricing-page-test |

## 4. Metrics

| metric | canonical definition | logic | trusted number (value, period, where from) | verified | source |
|---|---|---|---|---|---|
| visitors_assigned | Visitors given an arm, internal visitors included | count(distinct visitor_id) | control 3,727 and variant 3,779, 2 to 15 Feb 2026, experiment platform | 2026-02-25 | analyses/2026-02-24-pricing-page-test |
| conversion_7d | Share of external visitors with a paid order within 7 days of assignment | visitors with 1 or more paid orders where order_ts >= assigned_ts and order_ts < assigned_ts + 7 days, divided by visitors | about 10%, pricing page visitors, January 2026, product analytics | 2026-01-26 | setup |

## 5. Rules

| rule | applies to | verified | source |
|---|---|---|---|
| Exclude internal visitors (is_internal = 1) from test readouts | assignments | 2026-01-26 | setup |
| Count paid orders only (status = 'paid') | orders | 2026-01-26 | setup |
| Timestamps are UTC | assignments, orders | 2026-01-26 | setup |
| Analyse a test at the unit it was randomised on (the visitor) | all test readouts | 2026-02-25 | analyses/2026-02-24-pricing-page-test |

## 6. Gotchas

| gotcha | how to avoid | verified | source |
|---|---|---|---|
| Joining assignments to orders before aggregating repeats visitors who ordered more than once | Build one row per visitor first | 2026-02-25 | analyses/2026-02-24-pricing-page-test |
| The 7-day window closes 7 days after the last assignment | Do not read a test before the last window has closed (22 Feb for a test ending 15 Feb) | 2026-02-25 | analyses/2026-02-24-pricing-page-test |

## 7. Glossary

| term | means | maps to | verified | source |
|---|---|---|---|---|
| External visitor | A visitor who is not staff | assignments.is_internal = 0 | 2026-01-26 | setup |
| Variant | The new pricing page layout | assignments.arm = 'variant' | 2026-01-26 | setup |

## 8. Conventions

- SQL style: sqlstyle.guide defaults, with lowercase keywords, leading commas, `where true`, CTEs and full table names.
- Python style: PEP 8.
- Team overrides: none yet.
