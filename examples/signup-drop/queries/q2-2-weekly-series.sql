-- Q2.2  Method card: rolling windows and full periods. Purpose: sign-ups per full week (Monday start), to see when the fall began.
-- Expect: a step down in one week, not a slow slide. Partial weeks at both ends are left out.
select
    date(signup_date, '-' || ((cast(strftime('%w', signup_date) as integer) + 6) % 7) || ' days') as week_start
  , count(*)                    as signups
  , count(distinct signup_date) as days
from
    signups_clean
where true
    and signup_date >= '2026-01-05'
    and signup_date <  '2026-03-30'
group by 1
order by 1
;
