# Case 3: sound query (clean)

Type: clean. Data is invented.

## Input

User runs `/improve-code`: "Anything to improve? BigQuery. Our conventions are in the data map: lowercase, CTEs, leading commas. `signups` is one row per account and is partitioned by `signup_date`."

```sql
with
    march_signups as (
        select
            account_id
          , channel
        from
            signups
        where true
            and signup_date >= date '2026-03-01'
            and signup_date <  date '2026-04-01'
            and is_test = false
    )

select
    channel
  , count(distinct account_id) as signup_count
from
    march_signups
where true
group by 1
;
```

## Simulated answers

None needed.

## Pass

- States the intent in one line.
- Says "No changes needed." The grain is right, the partition filter is there, the range is half-open, the test filter is applied, the style matches the stated conventions.
- At most 2 optional suggestions, labelled optional.
- Shows no diff.

## Fail

- Restyles the query away from the team's conventions.
- Invents a bug.
- Asks for the dialect, which was given.
