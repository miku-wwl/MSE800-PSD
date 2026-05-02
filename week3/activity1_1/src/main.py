"""Week 3 - Activity 1.1

最小可运行示例：创建表、插入少量数据、演示查询。
"""

from __future__ import annotations

from pathlib import Path

from db import get_connection, run_sql_file


HERE = Path(__file__).resolve().parent
SQL_DIR = HERE.parent / "sql"


def print_rows(title: str, rows) -> None:
    print("\n==", title)
    for r in rows:
        # sqlite3.Row supports dict() conversion
        print(dict(r))


def main() -> None:
    schema_sql = SQL_DIR / "schema.sql"
    seed_sql = SQL_DIR / "seed.sql"
    queries_sql = SQL_DIR / "queries.sql"

    with get_connection() as conn:
        run_sql_file(conn, schema_sql)
        run_sql_file(conn, seed_sql)

        # Demo: run a few queries directly here (keep it simple)
        students = conn.execute("SELECT * FROM student ORDER BY student_id").fetchall()
        courses = conn.execute("SELECT * FROM course ORDER BY course_id").fetchall()
        enrollments = conn.execute(
            """
            SELECT s.student_id, s.first_name, s.last_name, c.course_code, e.status
            FROM enrollment e
            JOIN student s ON s.student_id = e.student_id
            JOIN course c ON c.course_id = e.course_id
            ORDER BY s.student_id, c.course_code
            """
        ).fetchall()

    print_rows("Students", students)
    print_rows("Courses", courses)
    print_rows("Enrollments", enrollments)

    print("\nSQL files:")
    print("-", schema_sql)
    print("-", seed_sql)
    print("-", queries_sql)


if __name__ == "__main__":
    main()
