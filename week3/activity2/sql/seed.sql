-- Week 3 - Activity 2
-- 初始化数据 (可选)

PRAGMA foreign_keys = ON;

INSERT INTO currency (currency_code, currency_name, symbol, decimals, country)
VALUES
('NZD', 'New Zealand Dollar', '$', 2, 'New Zealand'),
('USD', 'US Dollar', '$', 2, 'United States'),
('CNY', 'Chinese Yuan', '¥', 2, 'China');

INSERT INTO customer (full_name, email, phone, kyc_status)
VALUES
('Alice Wang', 'alice@example.com', '+64-000-000', 'verified');

-- Alice accounts
INSERT INTO account (customer_id, base_currency_code, balance)
VALUES
(1, 'NZD', 1000.00),
(1, 'USD', 100.00);

-- Exchange rate snapshots
INSERT INTO exchange_rate (from_currency_code, to_currency_code, rate, as_of, source)
VALUES
('NZD', 'USD', 0.62, datetime('now'), 'demo'),
('USD', 'NZD', 1.61, datetime('now'), 'demo');

-- Create an order: sell NZD -> buy USD
INSERT INTO exchange_order (customer_id, sell_currency_code, buy_currency_code, sell_amount, buy_amount_est, status)
VALUES
(1, 'NZD', 'USD', 500.00, 310.00, 'created');

-- Execute the order using the first rate
INSERT INTO order_execution (order_id, rate_id, executed_sell_amount, executed_buy_amount)
VALUES
(1, 1, 500.00, 310.00);

-- Payment record
INSERT INTO payment (order_id, method, provider_ref, amount, currency_code, status)
VALUES
(1, 'bank_transfer', 'REF-DEMO-001', 500.00, 'NZD', 'completed');
