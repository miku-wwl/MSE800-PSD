"""User 仓储。"""

from __future__ import annotations

import sqlite3

from model import Role, User


class UserRepository:
    def __init__(self, conn: sqlite3.Connection) -> None:
        self.conn = conn

    def create(self, user: User) -> User:
        cursor = self.conn.execute(
            """
            INSERT INTO users (full_name, email, password_hash, role)
            VALUES (?, ?, ?, ?)
            """,
            (user.full_name, user.email, user.password_hash, user.role.value),
        )
        return User(
            user_id=cursor.lastrowid,
            full_name=user.full_name,
            email=user.email,
            password_hash=user.password_hash,
            role=user.role,
        )

    def find_by_email(self, email: str) -> User | None:
        row = self.conn.execute(
            "SELECT * FROM users WHERE email = ?",
            (email,),
        ).fetchone()
        return self._row_to_user(row) if row else None

    def list_all(self) -> list[User]:
        rows = self.conn.execute("SELECT * FROM users ORDER BY user_id").fetchall()
        return [self._row_to_user(row) for row in rows]

    def _row_to_user(self, row: sqlite3.Row) -> User:
        return User(
            user_id=row["user_id"],
            full_name=row["full_name"],
            email=row["email"],
            password_hash=row["password_hash"],
            role=Role(row["role"]),
            created_at=row["created_at"],
        )
