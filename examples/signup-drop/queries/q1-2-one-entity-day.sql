-- Q1.2  Rung 2, one entity-day. Purpose: check the month boundary in UTC around midnight on 1 March.
-- Expect: every row before 2026-03-01 00:00:00 falls in 2026-02, every row from then on in 2026-03.
select
    substr(signup_ts, 1, 7)               as signup_month
  , min(signup_ts)                        as first_ts
  , max(signup_ts)                        as last_ts
  , count(*)                              as row_count
from
    signups
where true
    and signup_ts >= '2026-02-28 22:00:00'
    and signup_ts <  '2026-03-01 02:00:00'
group by 1
order by 1
;
