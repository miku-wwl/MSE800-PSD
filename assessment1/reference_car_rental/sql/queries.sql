-- Assessment 1 学习骨架
-- 常见查询参考

PRAGMA foreign_keys = ON;

-- 1. 查看所有可用车辆
SELECT *
FROM cars
WHERE available_now = 1
ORDER BY daily_rate;

-- 2. 查看所有预订及对应客户、车辆信息
SELECT
    b.booking_id,
    u.full_name AS customer_name,
    u.email AS customer_email,
    c.make,
    c.model,
    b.start_date,
    b.end_date,
    b.status,
    b.daily_rate,
    b.extra_charges,
    (julianday(b.end_date) - julianday(b.start_date)) AS raw_days
FROM bookings b
JOIN users u ON u.user_id = b.user_id
JOIN cars c ON c.car_id = b.car_id
ORDER BY b.booking_id;

-- 3. 查某个客户的全部订单
-- 把 2 换成你自己的 user_id
SELECT *
FROM bookings
WHERE user_id = 2
ORDER BY created_at DESC;

-- 4. 查某台车的历史预订
-- 把 1 换成你要看的 car_id
SELECT *
FROM bookings
WHERE car_id = 1
ORDER BY start_date;
