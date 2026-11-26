-- Q1.5  Rung 5, reconcile. Purpose: compare monthly sign-ups with the growth dashboard (the trusted number).
-- Expect: every month within the 1% tolerance set in the plan.
with
    monthly as (
        select
            signup_month
          , count(*) as signups
        from
            signups_clean
        where true
        group by 1
    )

select
    monthly.signup_month
  , monthly.signups                                              as our_count
  , dashboard_monthly.signups                                    as dashboard_count
  , monthly.signups - dashboard_monthly.signups                  as gap
  , round((monthly.signups - dashboard_monthly.signups) * 100.0 / dashboard_monthly.signups, 2) as gap_pct
from
    monthly
join
    dashboard_monthly
    on dashboard_monthly.month = monthly.signup_month
where true
order by 1
;
