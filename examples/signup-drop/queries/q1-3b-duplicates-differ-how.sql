-- Q1.3b  Purpose: what differs between the duplicate rows? Expect: unknown. This is a look, after rung 3 failed.
select
    count(*)                                                       as duplicated_ids
  , sum(case when ts_values > 1 then 1 else 0 end)                 as ids_where_signup_ts_differs
  , sum(case when channel_values > 1 then 1 else 0 end)            as ids_where_channel_differs
  , sum(case when test_values > 1 then 1 else 0 end)               as ids_where_is_test_differs
  , sum(case when updated_values > 1 then 1 else 0 end)            as ids_where_updated_ts_differs
from (
    select
        signup_id
      , count(distinct signup_ts)  as ts_values
      , count(distinct channel)    as channel_values
      , count(distinct is_test)    as test_values
      , count(distinct updated_ts) as updated_values
    from
        signups
    where true
    group by 1
    having count(*) > 1
)
where true
;
