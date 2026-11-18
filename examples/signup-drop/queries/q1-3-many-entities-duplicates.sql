-- Q1.3  Rung 3, many entities. Purpose: is signup_id unique? Expect: zero ids with more than one row.
select
    count(*)                              as ids_with_more_than_one_row
  , coalesce(sum(row_count), 0)           as rows_on_those_ids
  , coalesce(max(row_count), 0)           as most_rows_on_one_id
from (
    select
        signup_id
      , count(*) as row_count
    from
        signups
    where true
    group by 1
    having count(*) > 1
)
where true
;
