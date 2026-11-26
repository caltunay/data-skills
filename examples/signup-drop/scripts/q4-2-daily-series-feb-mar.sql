-- Q4.2  Chart data. Purpose: sign-ups per day in February and March, from signups_clean, for the readout chart.
-- Expect: 59 rows. Daily values near 42 in February and near 31 in March, with the step at 2 March.
select
    signup_date
  , count(*)        as signups
from
    signups_clean
where true
    and signup_date >= '2026-02-01'
group by 1
order by 1
;
