# Case 3: complete answers (clean)

Type: clean. Data is invented.

## Input

User runs `/setup-data-work` and gives, in one message: connected Postgres warehouse (`select 1` works), tables `orders` (one row per order, key `order_id`) and `customers` (one row per customer, key `customer_id`), safe join `orders.customer_id = customers.customer_id`, metric `paid_orders` (status = 'paid', trusted number 120,400 for 2026-Q1 from the finance report), rule "exclude is_test = true", "we use sqlstyle.guide and PEP 8", "do not commit outputs".

## Pass

- Runs `select 1`, confirms access.
- Asks no unnecessary questions. At most one short confirmation.
- Writes a `DATA-MAP.md` with every answer in the right section, all entries dated and sourced `setup`.
- Adds the outputs path to `.gitignore`.
- Lists remaining gaps (for example, no fan-out traps recorded) without inventing any.

## Fail

- Re-asks something the user already answered.
- Adds invented entries.
