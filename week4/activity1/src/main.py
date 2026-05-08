"""Week 4 - Activity 1

Minimal runnable demo:
- Create tables from schema.sql
- Insert optional seed data
- Insert one extra demo order (so you can see CRUD-style inserts)
- Query and print results
"""

from __future__ import annotations

from pathlib import Path

from db import get_connection, run_sql_file


HERE = Path(__file__).resolve().parent
SQL_DIR = HERE.parent / "sql"


def print_rows(title: str, rows) -> None:
    print("\n==", title)
    for row in rows:
        print(dict(row))


def ensure_demo_customer(conn) -> int:
    conn.execute(
        """
        INSERT INTO customer (full_name, email, phone, kyc_status)
        VALUES (?, ?, ?, ?)
        ON CONFLICT(email) DO NOTHING
        """,
        ("Bob Chen", "bob@example.com", "+64-111-222", "pending"),
    )
    customer = conn.execute(
        "SELECT customer_id FROM customer WHERE email = ?", ("bob@example.com",)
    ).fetchone()
    return int(customer["customer_id"])


def main() -> None:
    schema_sql = SQL_DIR / "schema.sql"
    seed_sql = SQL_DIR / "seed.sql"

    with get_connection() as conn:
        run_sql_file(conn, schema_sql)
        run_sql_file(conn, seed_sql)

        # A small extra insert flow (order + execution + payment)
        customer_id = ensure_demo_customer(conn)

        conn.execute(
            """
            INSERT INTO account (customer_id, base_currency_code, balance)
            VALUES (?, ?, ?)
            """,
            (customer_id, "NZD", 250.0),
        )

        rate_cursor = conn.execute(
            """
            INSERT INTO exchange_rate (from_currency_code, to_currency_code, rate, as_of, source)
            VALUES (?, ?, ?, datetime('now'), ?)
            """,
            ("NZD", "USD", 0.60, "demo"),
        )
        rate_id = int(rate_cursor.lastrowid)

        order_cursor = conn.execute(
            """
            INSERT INTO exchange_order (
              customer_id, sell_currency_code, buy_currency_code,
              sell_amount, buy_amount_est, status
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (customer_id, "NZD", "USD", 100.0, 60.0, "created"),
        )
        order_id = int(order_cursor.lastrowid)

        conn.execute(
            """
            INSERT INTO order_execution (
              order_id, rate_id, executed_sell_amount, executed_buy_amount
            )
            VALUES (?, ?, ?, ?)
            """,
            (order_id, rate_id, 100.0, 60.0),
        )

        conn.execute(
            """
            INSERT INTO payment (order_id, method, provider_ref, amount, currency_code, status)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (order_id, "card", "REF-DEMO-BOB-001", 100.0, "NZD", "completed"),
        )

        # Query and print
        orders = conn.execute(
            """
            SELECT
              o.order_id,
              c.full_name AS customer_name,
              o.status,
              o.sell_currency_code,
              o.sell_amount,
              o.buy_currency_code,
              o.buy_amount_est,
              o.created_at
            FROM exchange_order o
            JOIN customer c ON c.customer_id = o.customer_id
            ORDER BY o.order_id
            """
        ).fetchall()

        executions = conn.execute(
            """
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
            ORDER BY e.execution_id
            """
        ).fetchall()

        payments = conn.execute(
            """
            SELECT payment_id, order_id, method, amount, currency_code, status, created_at
            FROM payment
            ORDER BY payment_id
            """
        ).fetchall()

    print_rows("Orders", orders)
    print_rows("Executions", executions)
    print_rows("Payments", payments)


if __name__ == "__main__":
    main()
