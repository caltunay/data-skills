-- Q1.4  Rung 4, aggregates. Purpose: visitors per arm and per day. Expect: 14 days, every day has both arms, no empty day.
select
    arm
  , count(*)                        as visitors
  , count(distinct assigned_date)   as days
  , min(assigned_date)              as first_day
  , max(assigned_date)              as last_day
  , sum(converted)                  as converters
  , sum(paid_orders)                as paid_orders
from
    visitor_outcomes
where true
group by 1
order by 1
;
