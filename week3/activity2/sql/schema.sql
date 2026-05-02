-- Week 3 - Activity 2
-- Finance Money Exchange 软件：数据库表结构 (SQLite)
-- 设计目标：至少 5 个实体，每个实体 >= 5 个属性，并包含 PK/FK；关系类型清晰。

PRAGMA foreign_keys = ON;

-- 币种字典
CREATE TABLE IF NOT EXISTS currency (
    currency_code   TEXT PRIMARY KEY,
    currency_name   TEXT NOT NULL,
    symbol          TEXT,
    decimals        INTEGER NOT NULL DEFAULT 2,
    country         TEXT,
    is_active       INTEGER NOT NULL DEFAULT 1
);

-- 客户
CREATE TABLE IF NOT EXISTS customer (
    customer_id     INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name       TEXT NOT NULL,
    email           TEXT NOT NULL UNIQUE,
    phone           TEXT,
    kyc_status      TEXT NOT NULL DEFAULT 'pending',
    created_at      TEXT NOT NULL DEFAULT (datetime('now'))
);

-- 账户（可理解为多币种钱包账户）
CREATE TABLE IF NOT EXISTS account (
    account_id          INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id         INTEGER NOT NULL,
    base_currency_code  TEXT NOT NULL,
    balance             REAL NOT NULL DEFAULT 0,
    status              TEXT NOT NULL DEFAULT 'active',
    opened_at           TEXT NOT NULL DEFAULT (datetime('now')),

    FOREIGN KEY (customer_id) REFERENCES customer(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (base_currency_code) REFERENCES currency(currency_code)
);

-- 汇率快照（from/to 组合 + 时间点）
CREATE TABLE IF NOT EXISTS exchange_rate (
    rate_id             INTEGER PRIMARY KEY AUTOINCREMENT,
    from_currency_code  TEXT NOT NULL,
    to_currency_code    TEXT NOT NULL,
    rate                REAL NOT NULL,
    as_of               TEXT NOT NULL,
    source              TEXT,

    FOREIGN KEY (from_currency_code) REFERENCES currency(currency_code),
    FOREIGN KEY (to_currency_code) REFERENCES currency(currency_code)
);

-- 换汇订单
CREATE TABLE IF NOT EXISTS exchange_order (
    order_id            INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id         INTEGER NOT NULL,
    sell_currency_code  TEXT NOT NULL,
    buy_currency_code   TEXT NOT NULL,
    sell_amount         REAL NOT NULL,
    buy_amount_est      REAL,
    status              TEXT NOT NULL DEFAULT 'created',
    created_at          TEXT NOT NULL DEFAULT (datetime('now')),

    FOREIGN KEY (customer_id) REFERENCES customer(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (sell_currency_code) REFERENCES currency(currency_code),
    FOREIGN KEY (buy_currency_code) REFERENCES currency(currency_code)
);

-- 订单执行（支持部分成交）
CREATE TABLE IF NOT EXISTS order_execution (
    execution_id            INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id                INTEGER NOT NULL,
    rate_id                 INTEGER NOT NULL,
    executed_sell_amount    REAL NOT NULL,
    executed_buy_amount     REAL NOT NULL,
    executed_at             TEXT NOT NULL DEFAULT (datetime('now')),

    FOREIGN KEY (order_id) REFERENCES exchange_order(order_id) ON DELETE CASCADE,
    FOREIGN KEY (rate_id) REFERENCES exchange_rate(rate_id)
);

-- 支付/结算
CREATE TABLE IF NOT EXISTS payment (
    payment_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id         INTEGER NOT NULL,
    method          TEXT NOT NULL,
    provider_ref    TEXT,
    amount          REAL NOT NULL,
    currency_code   TEXT NOT NULL,
    status          TEXT NOT NULL DEFAULT 'pending',
    created_at      TEXT NOT NULL DEFAULT (datetime('now')),

    FOREIGN KEY (order_id) REFERENCES exchange_order(order_id) ON DELETE CASCADE,
    FOREIGN KEY (currency_code) REFERENCES currency(currency_code)
);
