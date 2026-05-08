from __future__ import annotations

import sqlite3
from pathlib import Path

from .config import DEFAULT_DB_PATH, SQL_DIR


def get_connection(db_path: Path | str = DEFAULT_DB_PATH) -> sqlite3.Connection:
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def run_sql_file(conn: sqlite3.Connection, sql_path: Path) -> None:
    conn.executescript(sql_path.read_text(encoding="utf-8"))


def initialize_database(db_path: Path | str = DEFAULT_DB_PATH, *, force: bool = False) -> None:
    db_file = Path(db_path)
    if force and db_file.exists():
        db_file.unlink()

    if db_file.exists():
        return

    db_file.parent.mkdir(parents=True, exist_ok=True)

    with get_connection(db_file) as conn:
        run_sql_file(conn, SQL_DIR / "schema.sql")
        run_sql_file(conn, SQL_DIR / "seed.sql")
