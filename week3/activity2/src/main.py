"""Week 3 - Activity 2

最小可运行示例：建表 + 插入示例数据 + 演示订单查询。

注意：这是为了展示 ER 设计如何落到 SQL/代码，不是完整业务系统。
"""

from __future__ import annotations

from pathlib import Path

from db import get_connection, run_sql_file


HERE = Path(__file__).resolve().parent
SQL_DIR = HERE.parent / "sql"


def print_rows(title: str, rows) -> None:
    print("\n==", title)
    for r in rows:
        print(dict(r))


def main() -> None:
    schema_sql = SQL_DIR / "schema.sql"
    seed_sql = SQL_DIR / "seed.sql"

    with get_connection() as conn:
        run_sql_file(conn, schema_sql)
        run_sql_file(conn, seed_sql)

        orders = conn.execute(
            """
            SELECT
              o.order_id,
              o.status,
              o.sell_currency_code,
              o.sell_amount,
              o.buy_currency_code,
              o.buy_amount_est,
              c.full_name AS customer_name,
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

    print_rows("Orders", orders)
    print_rows("Executions", executions)


if __name__ == "__main__":
    main()
