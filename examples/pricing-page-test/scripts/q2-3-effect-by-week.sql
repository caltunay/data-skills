-- Q2.3  Method card check 9: novelty. Purpose: conversion by arm in each full test week.
-- Expect: if the effect is real and not a novelty spike, the gap has the same sign in both weeks.
select
    test_week
  , arm
  , count(*)                                    as visitors
  , sum(converted)                              as converters
  , round(sum(converted) * 100.0 / count(*), 2) as conversion_pct
from
    visitor_outcomes
where true
group by 1, 2
order by 1, 2
;
