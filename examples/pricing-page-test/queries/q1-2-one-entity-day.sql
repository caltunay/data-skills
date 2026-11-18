-- Q1.2  Rung 2, one entity-day. Purpose: check the 7-day window on two visitors near its edge.
-- Expect: visitor 502836 has an order 6.85 days after assignment: inside. Visitor 504088 ordered 7.23 days after: outside.
select
    assignments.visitor_id
  , assignments.assigned_ts
  , orders.order_ts
  , orders.status
  , round(julianday(orders.order_ts) - julianday(assignments.assigned_ts), 2) as days_after_assignment
  , case
        when orders.order_ts >= assignments.assigned_ts
         and orders.order_ts <  datetime(assignments.assigned_ts, '+7 days') then 'inside window'
        else 'outside window'
    end as window_check
from
    assignments
join
    orders
    on orders.visitor_id = assignments.visitor_id
where true
    and assignments.visitor_id in (502836, 504088)
order by 1
;
