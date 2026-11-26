-- Q3.6  Purpose: line up the timing. Paid social sign-ups and paid social spend per full week.
-- Expect: unknown. Matching dates are a lead, not a cause.
with
    weekly_signups as (
        select
            date(signup_date, '-' || ((cast(strftime('%w', signup_date) as integer) + 6) % 7) || ' days') as week_start
          , count(*) as paid_social_signups
        from
            signups_clean
        where true
            and channel = 'paid_social'
            and signup_date >= '2026-02-02'
            and signup_date <  '2026-03-30'
        group by 1
    )

  , weekly_spend as (
        select
            date(spend_date, '-' || ((cast(strftime('%w', spend_date) as integer) + 6) % 7) || ' days') as week_start
          , round(sum(spend), 0) as paid_social_spend
        from
            daily_spend
        where true
            and channel = 'paid_social'
            and spend_date >= '2026-02-02'
            and spend_date <  '2026-03-30'
        group by 1
    )

select
    weekly_signups.week_start
  , weekly_signups.paid_social_signups
  , weekly_spend.paid_social_spend
from
    weekly_signups
join
    weekly_spend
    on weekly_spend.week_start = weekly_signups.week_start
where true
order by 1
;
