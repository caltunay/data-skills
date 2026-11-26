-- Q1.1  Rung 1, one entity. Purpose: follow visitor 500060 end to end, assignment and orders.
-- Expect: one assignment row (variant, mobile, 2 Feb 09:19:51, not internal) and two paid orders, 34.09 and 42.47, both inside 7 days.
select
    assignments.visitor_id
  , assignments.arm
  , assignments.device
  , assignments.assigned_ts
  , assignments.is_internal
  , orders.order_id
  , orders.order_ts
  , orders.status
  , orders.amount
  , round(julianday(orders.order_ts) - julianday(assignments.assigned_ts), 2) as days_after_assignment
from
    assignments
left join
    orders
    on orders.visitor_id = assignments.visitor_id
where true
    and assignments.visitor_id = 500060
order by orders.order_ts
;
