-- Q1.1  Rung 1, one entity. Purpose: follow sign-up 101005 end to end.
-- Expect: one row, paid_search, mobile, monthly, GB, 24 Jan 2026 21:32:27, not a test account.
select
    signup_id
  , account_id
  , signup_ts
  , channel
  , platform
  , plan
  , country
  , is_test
  , updated_ts
from
    signups
where true
    and signup_id = 101005
;
