-- Q2.1  Method card check 1: sample ratio mismatch. Purpose: external visitors per arm against the planned 50/50 split.
-- Expect: close to 50/50. The chi-square test is computed in stats.py. p < 0.001 would mean the test is broken.
select
    arm
  , count(*)                                                            as visitors
  , round(count(*) * 100.0 / (select count(*) from visitor_outcomes), 2) as share_pct
from
    visitor_outcomes
where true
group by 1
order by 1
;
