-- Assessment 1 学习骨架
-- Car Rental System 的最小数据库结构（SQLite）
-- 这是给你参考的起点，不是提交成品。

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS users (
    user_id        INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name      TEXT NOT NULL,
    email          TEXT NOT NULL UNIQUE,
    password_hash  TEXT NOT NULL,
    role           TEXT NOT NULL CHECK (role IN ('customer', 'admin')),
    created_at     TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS cars (
    car_id                INTEGER PRIMARY KEY AUTOINCREMENT,
    make                  TEXT NOT NULL,
    model                 TEXT NOT NULL,
    year                  INTEGER NOT NULL,
    mileage               INTEGER NOT NULL DEFAULT 0,
    available_now         INTEGER NOT NULL DEFAULT 1,
    minimum_rent_period   INTEGER NOT NULL DEFAULT 1,
    maximum_rent_period   INTEGER NOT NULL DEFAULT 30,
    daily_rate            REAL NOT NULL DEFAULT 0,
    created_at            TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS bookings (
    booking_id     INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id        INTEGER NOT NULL,
    car_id         INTEGER NOT NULL,
    start_date     TEXT NOT NULL,
    end_date       TEXT NOT NULL,
    status         TEXT NOT NULL CHECK (status IN ('pending', 'approved', 'rejected')),
    daily_rate     REAL NOT NULL,
    extra_charges  REAL NOT NULL DEFAULT 0,
    created_at     TEXT NOT NULL DEFAULT (datetime('now')),

    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (car_id) REFERENCES cars(car_id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_bookings_user_id ON bookings(user_id);
CREATE INDEX IF NOT EXISTS idx_bookings_car_id ON bookings(car_id);
