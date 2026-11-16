-- Q2.1  Method card: counts and rates; week-on-week with like-for-like periods.
-- Purpose: the headline. February against March, as totals and as daily averages.
-- Expect: March lower on both. The daily average falls more, because March is 3 days longer.
with
    monthly as (
        select
            signup_month
          , count(*)                    as signups
          , count(distinct signup_date) as days
        from
            signups_clean
        where true
            and signup_month in ('2026-02', '2026-03')
        group by 1
    )

select
    max(case when signup_month = '2026-02' then signups end)                         as feb_signups
  , max(case when signup_month = '2026-03' then signups end)                         as mar_signups
  , round((max(case when signup_month = '2026-03' then signups end)
         - max(case when signup_month = '2026-02' then signups end)) * 100.0
         / max(case when signup_month = '2026-02' then signups end), 1)              as total_change_pct
  , round(max(case when signup_month = '2026-02' then signups * 1.0 / days end), 2)  as feb_per_day
  , round(max(case when signup_month = '2026-03' then signups * 1.0 / days end), 2)  as mar_per_day
  , round((max(case when signup_month = '2026-03' then signups * 1.0 / days end)
         - max(case when signup_month = '2026-02' then signups * 1.0 / days end)) * 100.0
         / max(case when signup_month = '2026-02' then signups * 1.0 / days end), 1) as per_day_change_pct
from
    monthly
where true
;
