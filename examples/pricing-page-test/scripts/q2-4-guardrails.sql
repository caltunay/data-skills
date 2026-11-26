-- Q2.4  Method card check 8: guardrails, fixed before the test. Purpose: revenue per visitor, order value and return rate by arm.
-- Expect: order value and return rate are not worse in the variant. Intervals are computed in stats.py.
select
    arm
  , count(*)                                                          as visitors
  , round(sum(revenue) / count(*), 3)                                 as revenue_per_visitor
  , round(sum(revenue * revenue) / count(*), 3)                       as mean_squared_revenue
  , sum(paid_orders)                                                  as paid_orders
  , round(sum(revenue) / sum(paid_orders), 2)                         as average_order_value
  , sum(returned_orders)                                              as returned_orders
  , round(sum(returned_orders) * 100.0 / sum(paid_orders), 2)         as return_rate_pct
from
    visitor_outcomes
where true
group by 1
order by 1
;
