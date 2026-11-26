format: v1
updated: YYYY-MM-DD HH:MM

# Data map

Shared by the team. Every entry carries `verified: YYYY-MM-DD` and `source: setup` or `source: analyses/<YYYY-MM-DD>-<slug>`.
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

| left | right | keys | safe or trap | note | check status | verified | source |
|---|---|---|---|---|---|---|---|
| orders | customers | orders.customer_id = customers.customer_id | safe | many to one | unverified | 2026-01-01 | setup |
| orders | order_items | order_id | trap | one to many. Fans out order-level amounts | unverified | 2026-01-01 | setup |

Check status: every join starts as `unverified`, even when the schema or the user says it is safe. It becomes `checked` only after a query measured the key match rate and the fan-out, and the note says what the query found.

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

## 9. Goals

| level | goal | metric | horizon | verified | source |
|---|---|---|---|---|---|
| mission | Make good home goods easy to buy | none | 3 years | 2026-01-01 | setup |
| north star | Repeat customers | repeat_customer_rate | this year | 2026-01-01 | setup |
| target | Raise paid orders per active customer | orders_per_active_customer | this quarter | 2026-01-01 | setup |

Level: mission, north star or target. Horizon: this quarter, this year or 3 years.

## 10. Funnels

| funnel | step | event or table | step definition | verified | source |
|---|---|---|---|---|---|
| sign-up | 1 visit | web_events (page_view) | First page view of a session | 2026-01-01 | setup |
| sign-up | 2 started form | web_events (form_start) | Form field focused | 2026-01-01 | setup |
| sign-up | 3 signed up | customers | A row with created_at in the window | 2026-01-01 | setup |

One row per step, in order.

## 11. Key queries

| name | what it returns | when to use it | columns used | verified | source |
|---|---|---|---|---|---|
| paid_orders_by_day | Paid orders per day, test accounts out | Any daily trend or drop check | orders.order_date, orders.order_id, orders.is_test, orders.status | 2026-01-01 | setup |

Three to five queries. Each is saved as SQL text under its name, in the team's SQL conventions, and every column in it is checked against the Tables section. A column the map does not know is marked `unchecked` in "columns used". Reusable, each tested once.

### paid_orders_by_day

```sql
select
    orders.order_date
  , count(distinct orders.order_id) as paid_orders
from
    orders
where true
    and orders.is_test = false
    and orders.status = 'paid'
group by 1
order by 1
;
```

## 12. Ways of working

| item | answer | verified | source |
|---|---|---|---|
| where work lives | chat Projects (one per team or area) | 2026-01-01 | setup |
| file hand-back | downloads | 2026-01-01 | setup |

Where work lives: chat Projects, or a repo layout (one repo with a folder per project, a repo per project, or a team repo). File hand-back: downloads, Project files, or a named document tool. Skills ask about hand-back once per Project, then read it from here.
