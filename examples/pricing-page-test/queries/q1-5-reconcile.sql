-- Q1.5  Rung 5, reconcile. Purpose: compare visitors per arm with the experiment platform's exposure counts.
-- The platform counts internal visitors too, so compare before the internal filter. Expect: within the 0.5% tolerance in the plan.
with
    ours as (
        select
            arm
          , count(*) as visitors_assigned
        from
            assignments
        where true
        group by 1
    )

select
    ours.arm
  , ours.visitors_assigned                                         as our_count
  , platform_counts.visitors_assigned                              as platform_count
  , ours.visitors_assigned - platform_counts.visitors_assigned     as gap
from
    ours
join
    platform_counts
    on platform_counts.arm = ours.arm
where true
order by 1
;
