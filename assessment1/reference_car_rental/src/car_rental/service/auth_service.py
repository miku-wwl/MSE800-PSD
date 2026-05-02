"""认证业务。"""

from __future__ import annotations

import hashlib

from model import Role, User
from repository import UserRepository


class AuthService:
    def __init__(self, users: UserRepository) -> None:
        self.users = users

    def register(self, full_name: str, email: str, password: str, role: Role = Role.CUSTOMER) -> User:
        existing = self.users.find_by_email(email)
        if existing is not None:
            raise ValueError("Email 已存在")

        user = User(
            user_id=None,
            full_name=full_name,
            email=email,
            password_hash=self._hash_password(password),
            role=role,
        )
        return self.users.create(user)

    def login(self, email: str, password: str) -> User:
        user = self.users.find_by_email(email)
        if user is None:
            raise ValueError("用户不存在")
        if user.password_hash != self._hash_password(password):
            raise ValueError("密码错误")
        return user

    def _hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode("utf-8")).hexdigest()
