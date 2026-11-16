-- Q1.3c  Rung 3 again, after the fix. Purpose: build signups_clean (one row per signup_id, latest update,
-- test accounts excluded) and re-check uniqueness. Expect: row_count equals distinct ids. 3,542 ids before the test filter.
create view signups_clean as
with
    ranked as (
        select
            signups.*
          , row_number() over (
                partition by signup_id
                order by updated_ts desc
            ) as update_rank
        from
            signups
        where true
    )

select
    signup_id
  , account_id
  , signup_ts
  , date(signup_ts)            as signup_date
  , substr(signup_ts, 1, 7)    as signup_month
  , channel
  , platform
  , plan
  , country
from
    ranked
where true
    and update_rank = 1
    and is_test = 0
;

select
    (select count(distinct signup_id) from signups)            as distinct_ids_in_source
  , (select count(distinct signup_id) from signups where is_test = 1) as test_ids_excluded
  , count(*)                                                    as rows_in_clean
  , count(distinct signup_id)                                   as distinct_ids_in_clean
from
    signups_clean
where true
;
