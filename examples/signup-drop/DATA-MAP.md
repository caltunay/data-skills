format: v1
updated: 2026-04-07 09:00

# Data map

Invented example. Shared by the team. Every entry carries `verified: YYYY-MM-DD` and `source: setup` or `source: analyses/<slug>`.
Entries older than 90 days, or contradicted by data, must be re-confirmed before use.

## 1. Sources

| name | type | dialect | access mode | verified | source |
|---|---|---|---|---|---|
| example_files | file (CSV in `data/`) | SQLite (loaded by `examples/run_queries.py`) | connected | 2026-04-02 | setup |

## 2. Tables

| table | one row means (grain) | primary key | key columns | notes | verified | source |
|---|---|---|---|---|---|---|
| signups | one sign-up (an account created). See the gotcha on late updates | signup_id | account_id, signup_ts, channel, platform, plan, country, is_test, updated_ts | signup_ts and updated_ts are UTC | 2026-04-02 | setup |
| daily_spend | one channel on one day | spend_date, channel | spend | paid channels only | 2026-04-02 | setup |
| dashboard_monthly | one calendar month | month | signups | export of the growth dashboard | 2026-04-02 | setup |

## 3. Joins

| left | right | keys | safe or trap | note | check status | verified | source |
|---|---|---|---|---|---|---|---|
| signups (aggregated to day and channel) | daily_spend | signup date = spend_date, channel | safe | aggregate signups first. Joining raw signups to daily_spend repeats spend on every sign-up row | checked | 2026-04-08 | analyses/2026-04-07-signup-drop |

## 4. Metrics

| metric | canonical definition | logic | trusted number (value, period, where from) | verified | source |
|---|---|---|---|---|---|
| signups | Accounts created, test accounts excluded, counted on signup_ts in UTC | count(distinct signup_id) where is_test = 0 | 1,171, February 2026, growth dashboard | 2026-04-02 | setup |
| signups | same | same | 972, March 2026, growth dashboard | checked | 2026-04-08 | analyses/2026-04-07-signup-drop |

## 5. Rules

| rule | applies to | verified | source |
|---|---|---|---|
| Exclude test accounts (is_test = 1) | signups | 2026-04-02 | setup |
| Timestamps are UTC. Months and days are cut in UTC | signups, daily_spend | 2026-04-02 | setup |
| Keep one row per signup_id: the row with the latest updated_ts | signups | 2026-04-08 | analyses/2026-04-07-signup-drop |

## 6. Gotchas

| gotcha | how to avoid | verified | source |
|---|---|---|---|
| signups holds a second row for about 1% of sign-ups, written by a late update. Only updated_ts differs | Dedupe on signup_id before counting. Or count distinct signup_id | checked | 2026-04-08 | analyses/2026-04-07-signup-drop |
| Month totals mislead when months differ in length. February to March 2026 hid a third of the fall | Compare daily averages or full weeks | 2026-04-08 | analyses/2026-04-07-signup-drop |
| The growth dashboard runs up to 0.4% under the table | Use a 1% tolerance when reconciling | 2026-04-08 | analyses/2026-04-07-signup-drop |

## 7. Glossary

| term | means | maps to | verified | source |
|---|---|---|---|---|
| Sign-up | An account created in the subscription app | signups.signup_id | 2026-04-02 | setup |
| Channel | The acquisition channel stored on the sign-up. The attribution rule behind it is not documented | signups.channel | 2026-04-02 | setup |

## 8. Conventions

- SQL style: sqlstyle.guide defaults, with lowercase keywords, leading commas, `where true`, CTEs and full table names.
- Python style: PEP 8.
- Team overrides: none yet.

## 9. Goals

| level | goal | metric | horizon | verified | source |
|---|---|---|---|---|---|
| north star | Grow active subscribers | active_subscribers | this year | 2026-04-02 | setup |
| target | Lift monthly sign-ups | monthly sign-ups | this quarter | 2026-04-02 | setup |

## 10. Funnels

| funnel | step | event or table | step definition | verified | source |
|---|---|---|---|---|---|
| sign-up | 1 account created | signups | One row per `signup_id`, test accounts out | 2026-04-02 | setup |

Only the last step of the funnel is in this example data.

## 11. Key queries

| name | what it returns | when to use it | columns used | verified | source |
|---|---|---|---|---|---|
| daily_signups | Sign-ups per day, one row per `signup_id`, test accounts out | First check of any "sign-ups dropped" ask | signups.signup_ts, signups.signup_id, signups.is_test | 2026-04-02 | setup |

### daily_signups

```sql
select
    substr(signups.signup_ts, 1, 10)  as signup_date
  , count(distinct signups.signup_id) as signups
from
    signups
where true
    and signups.is_test = 0
group by 1
order by 1
;
```

## 12. Ways of working

| item | answer | verified | source |
|---|---|---|---|
| where work lives | chat Projects (one per team or area) | 2026-04-07 | setup |
| file hand-back | downloads | 2026-04-07 | setup |
