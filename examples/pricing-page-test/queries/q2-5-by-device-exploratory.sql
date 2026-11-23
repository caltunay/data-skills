-- Q2.5  Exploratory only. Purpose: conversion by arm and device. Not a result: found by slicing, one of 1 slice looked at.
-- Expect: unknown. Any difference between devices is a hypothesis for a later test.
select
    device
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
