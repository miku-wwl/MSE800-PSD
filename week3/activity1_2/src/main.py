"""Week 3 - Activity 1.2

最小可运行示例：创建 Lecturer/Student/Course/Enrollment 四张表并演示查询。
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

        lecturers = conn.execute(
            """
            SELECT l.lecturer_id, l.full_name, l.email, l.office_room,
                   m.full_name AS manager_name
            FROM lecturer l
            LEFT JOIN lecturer m ON m.lecturer_id = l.manager_lecturer_id
            ORDER BY l.lecturer_id
            """
        ).fetchall()

        courses = conn.execute(
            """
            SELECT c.course_code, c.course_name, c.credits,
                   l.full_name AS lecturer_name
            FROM course c
            JOIN lecturer l ON l.lecturer_id = c.lecturer_id
            ORDER BY c.course_code
            """
        ).fetchall()

    print_rows("Lecturers", lecturers)
    print_rows("Courses (with Lecturer)", courses)


if __name__ == "__main__":
    main()
