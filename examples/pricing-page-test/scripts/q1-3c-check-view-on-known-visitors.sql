-- Q1.3c  Purpose: check visitor_outcomes on the three visitors followed by hand in Q1.1 and Q1.2.
-- Expect: 500060 converted with 2 paid orders and revenue 76.56. 502836 converted with 2 paid orders (both seen in Q1.2) and revenue 89.00. 504088 not converted.
select
    visitor_id
  , arm
  , converted
  , paid_orders
  , round(revenue, 2) as revenue
from
    visitor_outcomes
where true
    and visitor_id in (500060, 502836, 504088)
order by 1
;
