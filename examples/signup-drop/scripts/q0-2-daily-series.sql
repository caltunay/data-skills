-- Q0.2  Floor check 4, daily series. Purpose: sign-ups per day across the full window, from the raw table, test accounts out.
-- Expect: 90 days from 1 Jan to 31 Mar, no day with zero sign-ups, no single-day spike or gap. A step, if any, shows as a level change.
with
    daily as (
        select
            substr(signup_ts, 1, 10)      as signup_date
          , count(distinct signup_id)     as signups
        from
            signups
        where true
            and is_test = 0
        group by 1
    )

select
    count(*)                              as days_with_signups
  , min(signup_date)                      as first_day
  , max(signup_date)                      as last_day
  , min(signups)                          as lowest_day
  , max(signups)                          as highest_day
from
    daily
;
