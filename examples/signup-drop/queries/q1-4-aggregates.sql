-- Q1.4  Rung 4, aggregates. Purpose: sign-ups per month, with days in month and the daily average.
-- Expect: three full months, 31, 28 and 31 days, no day with zero sign-ups, total equals rows in signups_clean.
select
    signup_month
  , count(*)                                        as signups
  , count(distinct signup_date)                     as days_with_signups
  , round(count(*) * 1.0 / count(distinct signup_date), 2) as signups_per_day
from
    signups_clean
where true
group by 1
order by 1
;
