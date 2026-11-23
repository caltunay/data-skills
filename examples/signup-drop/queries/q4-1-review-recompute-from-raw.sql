-- Q4.1  Review, independent recompute. Purpose: monthly sign-ups and paid social per day straight from the raw table, without signups_clean.
-- Expect: Jan 1,330, Feb 1,175, Mar 973 (as Q1.4). Paid social per day 15.32 in Feb and 5.42 in Mar (as Q3.1).
select
    substr(signup_ts, 1, 7)                                                as signup_month
  , count(distinct signup_id)                                              as signups
  , count(distinct case when channel = 'paid_social' then signup_id end)   as paid_social_signups
  , round(count(distinct case when channel = 'paid_social' then signup_id end) * 1.0
        / count(distinct substr(signup_ts, 1, 10)), 2)                     as paid_social_per_day
from
    signups
where true
    and is_test = 0
group by 1
order by 1
;
