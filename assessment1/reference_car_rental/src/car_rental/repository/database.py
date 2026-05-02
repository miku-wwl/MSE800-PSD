"""数据库连接与初始化工具。"""

from __future__ import annotations

import sqlite3
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[3]
SQL_DIR = ROOT_DIR / "sql"
DEFAULT_DB_PATH = ROOT_DIR / "car_rental_learning.db"


def get_connection(db_path: Path | str = DEFAULT_DB_PATH) -> sqlite3.Connection:
    """打开 SQLite 连接。"""
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def run_sql_file(conn: sqlite3.Connection, sql_path: Path) -> None:
    """执行一个 SQL 文件。"""
    conn.executescript(sql_path.read_text(encoding="utf-8"))


def initialize_database(db_path: Path | str = DEFAULT_DB_PATH) -> None:
    """创建表并灌入示例数据。"""
    db_file = Path(db_path)
    if db_file.exists():
        db_file.unlink()

    schema_path = SQL_DIR / "schema.sql"
    seed_path = SQL_DIR / "seed.sql"

    with get_connection(db_file) as conn:
        run_sql_file(conn, schema_path)
        run_sql_file(conn, seed_path)
