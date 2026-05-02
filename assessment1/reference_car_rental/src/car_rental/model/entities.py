"""领域模型：用于练习面向对象建模。"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from enum import Enum


class Role(str, Enum):
    CUSTOMER = "customer"
    ADMIN = "admin"


class BookingStatus(str, Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"


@dataclass
class User:
    user_id: int | None
    full_name: str
    email: str
    password_hash: str
    role: Role
    created_at: str | None = None


@dataclass
class Car:
    car_id: int | None
    make: str
    model: str
    year: int
    mileage: int
    available_now: bool
    minimum_rent_period: int
    maximum_rent_period: int


@dataclass
class Booking:
    booking_id: int | None
    user_id: int
    car_id: int
    start_date: date
    end_date: date
    status: BookingStatus
    daily_rate: float
    extra_charges: float = 0.0

    def rental_days(self) -> int:
        """计算租期天数，最少按 1 天算。"""
        return max((self.end_date - self.start_date).days, 1)

    def total_fee(self) -> float:
        """根据天数、日租和额外费用做一个最小版计算。"""
        return round(self.rental_days() * self.daily_rate + self.extra_charges, 2)
