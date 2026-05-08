PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS products (
    product_id  INTEGER PRIMARY KEY AUTOINCREMENT,
    name        TEXT NOT NULL,
    sku         TEXT NOT NULL UNIQUE,
    description TEXT NOT NULL DEFAULT '',
    quantity    INTEGER NOT NULL DEFAULT 0 CHECK (quantity >= 0),
    price       REAL NOT NULL DEFAULT 0 CHECK (price >= 0),
    created_at  TEXT NOT NULL DEFAULT (datetime('now'))
);
