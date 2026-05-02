-- Assessment 1 学习骨架
-- 示例数据：方便你自己跑 demo 和观察表结构

PRAGMA foreign_keys = ON;

INSERT INTO users (full_name, email, password_hash, role)
VALUES
('Demo Admin', 'admin@example.com', 'admin-demo-hash', 'admin'),
('Demo Customer', 'customer@example.com', 'customer-demo-hash', 'customer');

INSERT INTO cars (make, model, year, mileage, available_now, minimum_rent_period, maximum_rent_period, daily_rate)
VALUES
('Toyota', 'Corolla', 2023, 12000, 1, 1, 14, 45.0),
('Honda', 'CR-V', 2022, 25000, 1, 2, 21, 78.0),
('Mazda', 'CX-5', 2024, 6000, 0, 1, 30, 92.5);

INSERT INTO bookings (user_id, car_id, start_date, end_date, status, daily_rate, extra_charges)
VALUES
(2, 1, '2026-05-10', '2026-05-13', 'pending', 45.0, 15.0);
