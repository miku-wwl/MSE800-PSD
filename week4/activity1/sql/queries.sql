-- Week 4 - Activity 1
-- Sample queries

-- 1) Customers
SELECT customer_id, full_name, email, kyc_status, created_at
FROM customer
ORDER BY customer_id;

-- 2) Customer accounts
SELECT
  a.account_id,
  c.full_name,
  a.base_currency_code,
  a.balance,
  a.status,
  a.opened_at
FROM account a
JOIN customer c ON c.customer_id = a.customer_id
ORDER BY a.account_id;

-- 3) Orders (with customer name)
SELECT
  o.order_id,
  c.full_name AS customer_name,
  o.sell_currency_code,
  o.sell_amount,
  o.buy_currency_code,
  o.buy_amount_est,
  o.status,
  o.created_at
FROM exchange_order o
JOIN customer c ON c.customer_id = o.customer_id
ORDER BY o.order_id;

-- 4) Executions (with rate)
SELECT
  e.execution_id,
  e.order_id,
  r.from_currency_code,
  r.to_currency_code,
  r.rate,
  e.executed_sell_amount,
  e.executed_buy_amount,
  e.executed_at
FROM order_execution e
JOIN exchange_rate r ON r.rate_id = e.rate_id
ORDER BY e.execution_id;

-- 5) Payments
SELECT payment_id, order_id, method, provider_ref, amount, currency_code, status, created_at
FROM payment
ORDER BY payment_id;
