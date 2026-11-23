-- Q3.4  Method card: segment scan (exploratory). Dimension 4 of 4 listed before the scan: plan.
-- Purpose: daily average by plan, February against March, and each segment's share of the total fall.
-- Expect: unknown. Contributions sum to 100%.
with
    by_segment as (
        select
            plan
          , sum(case when signup_month = '2026-02' then 1 else 0 end) / 28.0 as feb_per_day
          , sum(case when signup_month = '2026-03' then 1 else 0 end) / 31.0 as mar_per_day
        from
            signups_clean
        where true
            and signup_month in ('2026-02', '2026-03')
        group by 1
    )

  , total as (
        select
            sum(mar_per_day) - sum(feb_per_day) as total_change
        from
            by_segment
        where true
    )

select
    by_segment.plan
  , round(by_segment.feb_per_day, 2)                                              as feb_per_day
  , round(by_segment.mar_per_day, 2)                                              as mar_per_day
  , round(by_segment.mar_per_day - by_segment.feb_per_day, 2)                     as change_per_day
  , round((by_segment.mar_per_day - by_segment.feb_per_day) * 100.0 / by_segment.feb_per_day, 1) as change_pct
  , round((by_segment.mar_per_day - by_segment.feb_per_day) * 100.0 / total.total_change, 1)     as share_of_fall_pct
from
    by_segment
cross join
    total
where true
order by 6 desc
;
