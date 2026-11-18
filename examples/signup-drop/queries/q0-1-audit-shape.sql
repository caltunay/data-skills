-- Q0.1  Purpose: audit the shape of signups. Expect: about 3,500 rows, 1 Jan to 31 Mar 2026, no null keys.
select
    count(*)                              as row_count
  , count(distinct signup_id)             as distinct_signup_ids
  , min(signup_ts)                        as first_signup_ts
  , max(signup_ts)                        as last_signup_ts
  , sum(case when signup_id is null or signup_id = '' then 1 else 0 end) as null_ids
  , sum(case when channel = '' then 1 else 0 end)                         as blank_channels
  , sum(is_test)                          as test_rows
from
    signups
where true
;
