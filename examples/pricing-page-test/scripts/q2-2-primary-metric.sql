-- Q2.2  Primary metric, fixed before the test: share of visitors with a paid order within 7 days of assignment.
-- Analysed per visitor, the unit of randomisation. Expect: unknown. The interval and test are computed in stats.py.
select
    arm
  , count(*)                                   as visitors
  , sum(converted)                             as converters
  , round(sum(converted) * 100.0 / count(*), 2) as conversion_pct
from
    visitor_outcomes
where true
group by 1
order by 1
;
