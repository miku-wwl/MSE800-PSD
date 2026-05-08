# Week 4 - Activity 1: SQLite3 Database (Money Exchange)

## Task

Develop a database using SQLite3 based on your ER design from **W3-A2** (finance money exchange application).

In this README, I describe how many tables were created and justify why each table is necessary.

## Deliverables

- SQL:
  - `sql/schema.sql` (tables + constraints)
  - `sql/seed.sql` (optional demo data)
  - `sql/queries.sql` (sample queries)
- Source code:
  - `src/db.py`
  - `src/main.py`

Running `src/main.py` will create/update the database file:

- `money_exchange.db`

## How Many Tables?

This design creates **7 tables**:

1. `currency`
2. `customer`
3. `account`
4. `exchange_rate`
5. `exchange_order`
6. `order_execution`
7. `payment`

## Why Each Table Is Necessary

### 1) `currency`

Central “dictionary” of supported currencies (code, name, decimals). It avoids hard-coded currency strings scattered across other tables and ensures referential integrity.

### 2) `customer`

Stores customer identity/contact + basic compliance state (`kyc_status`). Orders and accounts must be linked to a customer.

### 3) `account`

Represents a customer wallet/balance in a base currency (multi-currency wallets become multiple rows). It is required to track balances separately per customer and currency.

### 4) `exchange_rate`

Stores rate snapshots (`from/to`, `rate`, `as_of`, `source`). Orders need an auditable snapshot of the rate used at execution time.

### 5) `exchange_order`

Represents the intent to exchange (sell currency, buy currency, amounts, status, created time). It is the core business entity for the money exchange workflow.

### 6) `order_execution`

Represents one or more executions for an order (supports partial fills). It links to a specific `exchange_rate` snapshot to preserve traceability.

### 7) `payment`

Tracks settlement/payment events for an order (method, provider reference, amount, currency, status). Payments are separated from orders to support multiple settlement events and payment channels.

## Run (optional)

```powershell
cd d:\workshop\MSE800-PSD\week4\activity1\src
python main.py
```

If you want a clean run, delete `money_exchange.db` and run again.

## GitHub Submission

Once you are ready:

1. Push this repo (or a separate repo) to GitHub
2. Share the repository link
