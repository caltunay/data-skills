format: v1

# Data map

Shared by the team. Every entry carries `verified: YYYY-MM-DD` and `source: setup` or `source: analyses/<slug>`.
Entries older than 90 days, or contradicted by data, must be re-confirmed before use.

## 1. Sources

| name | type | dialect | access mode | verified | source |
|---|---|---|---|---|---|
| example_warehouse | warehouse | Postgres | connected | 2026-01-01 | setup |

Type: warehouse, lake, sheet, file, API, cube. Access mode: connected or hand-over.

## 2. Tables

| table | one row means (grain) | primary key | key columns | notes | verified | source |
|---|---|---|---|---|---|---|
| orders | one order | order_id | customer_id, order_ts, status, amount | amount is gross | 2026-01-01 | setup |

## 3. Joins

| left | right | keys | safe or trap | note | verified | source |
|---|---|---|---|---|---|---|
| orders | customers | orders.customer_id = customers.customer_id | safe | many to one | 2026-01-01 | setup |
| orders | order_items | order_id | trap | one to many. Fans out order-level amounts | 2026-01-01 | setup |

## 4. Metrics

| metric | canonical definition | logic | trusted number (value, period, where from) | verified | source |
|---|---|---|---|---|---|
| paid_orders | Orders with status paid | count(distinct order_id) where status = 'paid' | 120,400, 2026-Q1, finance report | 2026-01-01 | setup |

## 5. Rules

| rule | applies to | verified | source |
|---|---|---|---|
| Exclude test accounts (is_test = true) | all customer tables | 2026-01-01 | setup |
| Timestamps are UTC | all event tables | 2026-01-01 | setup |

## 6. Gotchas

| gotcha | how to avoid | verified | source |
|---|---|---|---|
| Orders table gets late updates for 3 days | Wait 3 days before reading a day as final | 2026-01-01 | setup |

## 7. Glossary

| term | means | maps to | verified | source |
|---|---|---|---|---|
| Active customer | Ordered in the last 90 days | orders.customer_id, order_ts | 2026-01-01 | setup |

## 8. Conventions

- SQL style: sqlstyle.guide defaults, unless overridden here.
- Python style: PEP 8, unless overridden here.
- Team overrides: none yet.
