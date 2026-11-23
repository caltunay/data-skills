-- Q3.5  Segment scan, second cut. Purpose: does the channel pattern hold inside each platform?
-- Expect: if the pattern is real, paid_social falls on both mobile and desktop, and other channels stay flat on both.
select
    case when channel = 'paid_social' then 'paid_social' else 'all other channels' end as channel_group
  , platform
  , round(sum(case when signup_month = '2026-02' then 1 else 0 end) / 28.0, 2) as feb_per_day
  , round(sum(case when signup_month = '2026-03' then 1 else 0 end) / 31.0, 2) as mar_per_day
  , round((sum(case when signup_month = '2026-03' then 1 else 0 end) / 31.0
         - sum(case when signup_month = '2026-02' then 1 else 0 end) / 28.0) * 100.0
         / (sum(case when signup_month = '2026-02' then 1 else 0 end) / 28.0), 1) as change_pct
from
    signups_clean
where true
    and signup_month in ('2026-02', '2026-03')
group by 1, 2
order by 1, 2
;
