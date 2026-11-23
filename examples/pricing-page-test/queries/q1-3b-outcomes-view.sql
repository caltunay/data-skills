-- Q1.3b  Purpose: build visitor_outcomes, one row per visitor, by aggregating orders to the visitor before joining.
-- Paid orders only, inside 7 days of assignment. Internal visitors excluded.
-- Expect: one row per external visitor. Row count = assignments less internal visitors.
create view visitor_outcomes as
with
    orders_in_window as (
        select
            assignments.visitor_id
          , count(*)                   as paid_orders
          , sum(orders.amount)         as revenue
          , sum(orders.is_returned)    as returned_orders
        from
            assignments
        join
            orders
            on  orders.visitor_id = assignments.visitor_id
            and orders.status     = 'paid'
            and orders.order_ts  >= assignments.assigned_ts
            and orders.order_ts  <  datetime(assignments.assigned_ts, '+7 days')
        where true
        group by 1
    )

select
    assignments.visitor_id
  , assignments.arm
  , assignments.device
  , date(assignments.assigned_ts)                                             as assigned_date
  , case when date(assignments.assigned_ts) < '2026-02-09' then 'week 1' else 'week 2' end as test_week
  , case when orders_in_window.visitor_id is not null then 1 else 0 end       as converted
  , coalesce(orders_in_window.paid_orders, 0)                                 as paid_orders
  , coalesce(orders_in_window.revenue, 0)                                     as revenue
  , coalesce(orders_in_window.returned_orders, 0)                             as returned_orders
from
    assignments
left join
    orders_in_window
    on orders_in_window.visitor_id = assignments.visitor_id
where true
    and assignments.is_internal = 0
;

select
    (select count(*) from assignments where is_internal = 0) as external_visitors
  , count(*)                                                 as rows_in_view
  , count(distinct visitor_id)                               as distinct_visitors_in_view
from
    visitor_outcomes
where true
;
