-- Q0.1  Purpose: audit the shape of assignments. Expect: about 7,400 rows, one per visitor, 2 to 15 Feb 2026, two arms.
select
    count(*)                         as row_count
  , count(distinct visitor_id)       as distinct_visitors
  , min(assigned_ts)                 as first_assigned_ts
  , max(assigned_ts)                 as last_assigned_ts
  , count(distinct arm)              as arms
  , sum(is_internal)                 as internal_visitors
  , sum(case when arm = '' or device = '' then 1 else 0 end) as blank_values
from
    assignments
where true
;
