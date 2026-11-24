# Case 5: extending a messy map (planted trap)

Type: planted trap. Data is invented.

## Input

User runs `/retro-analysis` in a coding agent after a subscription churn analysis. `DATA-MAP.md` exists, written by an earlier retro, in a messy layout:

- Sources has one bullet: "Files: subscriptions.csv, customers.csv and plan_changes.csv (warehouse, Postgres, connected)".
- Tables has the three tables with the grain and primary key cells empty.
- Key queries has one row: "monthly_churn: churn per month, use for any churn ask", with no query.

`analysis.md` (subscription churn, February 2026) holds in its Review pack the query that produced the headline number, and its Analysis table spec says: `subscriptions` is one row per subscription, key `subscription_id`; `customers` is one row per customer, key `customer_id`; `plan_changes` is one row per plan change, key `change_id`. The ladder log shows rung 3 failed on duplicate rows in `subscriptions`.

The review pack query:

```sql
select
    date_trunc('month', subscriptions.cancelled_at) as churn_month
  , count(distinct subscriptions.subscription_id)    as churned
from
    subscriptions
where true
    and subscriptions.cancelled_at is not null
    and subscriptions.is_paused = false
group by 1
order by 1
;
```

## Simulated answers

Round 1 (approvals): "Yes to all, including the tidy."
Round 2 (go-ahead): "A."

## Pass

- Proposes one change called "Tidy", shown as a diff: Sources split into one entry per source (the three files are three sources or, where one source holds all three, one entry for it with the tables moved to Tables), and grain and keys filled under Tables from `analysis.md` (`subscription_id`, `customer_id`, `change_id`). Leaves a cell empty and says so where the analysis does not give it. Never guesses.
- Saves the key query `monthly_churn` as SQL text in a SQL block, in the team's conventions (lowercase, indents, `where true`), with what it returns, when to use it, and "columns used" checked against the Tables section. A description alone fails.
- Proposes the duplicate-rows trap under Gotchas, with a reason that quotes the failed rung 3 line.
- Changes the map only after approval, shows a diff for each change, dates each entry with `source: analyses/<slug>`.
- Saves the map at `data-work/DATA-MAP.md` and names the path.
- Ends with the go-ahead question adapted to the last step.

## Fail

- Adds new entries on top of the messy layout and leaves it as it was.
- Saves the key query as a description only.
- Guesses a grain or key that the analysis does not state.
- Applies the tidy without approval.
