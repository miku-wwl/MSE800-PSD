"""Week 3 - Activity 1.1

学生与课程数据库：SQLite 工具层。
"""

from __future__ import annotations

import sqlite3
from pathlib import Path


DB_PATH = Path(__file__).resolve().parent.parent / "students_courses.db"


def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def run_sql_file(conn: sqlite3.Connection, sql_file: Path) -> None:
    sql_text = sql_file.read_text(encoding="utf-8")
    conn.executescript(sql_text)
