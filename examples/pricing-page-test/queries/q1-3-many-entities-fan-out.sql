-- Q1.3  Rung 3, many entities. Purpose: is visitor_id unique in assignments, and does a join to orders fan out?
-- Expect: assignments is unique. The join returns more rows than visitors with orders, because some visitors order twice.
select
    (select count(*) from assignments)                                            as assignment_rows
  , (select count(distinct visitor_id) from assignments)                          as distinct_visitors
  , (select count(*) from assignments join orders on orders.visitor_id = assignments.visitor_id) as rows_after_join_to_orders
  , (select count(distinct orders.visitor_id) from orders)                        as visitors_with_any_order
  , (select count(*) from (select visitor_id from orders where true group by 1 having count(*) > 1)) as visitors_with_more_than_one_order
where true
;
