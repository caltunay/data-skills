-- Q0.2  Purpose: audit the shape of orders. Expect: order_id unique, statuses paid and cancelled, no negative amounts.
select
    count(*)                                              as row_count
  , count(distinct order_id)                              as distinct_orders
  , count(distinct visitor_id)                            as visitors_with_orders
  , sum(case when status = 'paid' then 1 else 0 end)      as paid_orders
  , sum(case when status = 'cancelled' then 1 else 0 end) as cancelled_orders
  , min(order_ts)                                         as first_order_ts
  , max(order_ts)                                         as last_order_ts
  , min(amount)                                           as min_amount
  , max(amount)                                           as max_amount
from
    orders
where true
;
