"""Booking 仓储。"""

from __future__ import annotations

from datetime import date
import sqlite3

from model import Booking, BookingStatus


class BookingRepository:
    def __init__(self, conn: sqlite3.Connection) -> None:
        self.conn = conn

    def create(self, booking: Booking) -> Booking:
        cursor = self.conn.execute(
            """
            INSERT INTO bookings (user_id, car_id, start_date, end_date, status, daily_rate, extra_charges)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                booking.user_id,
                booking.car_id,
                booking.start_date.isoformat(),
                booking.end_date.isoformat(),
                booking.status.value,
                booking.daily_rate,
                booking.extra_charges,
            ),
        )
        return Booking(
            booking_id=cursor.lastrowid,
            user_id=booking.user_id,
            car_id=booking.car_id,
            start_date=booking.start_date,
            end_date=booking.end_date,
            status=booking.status,
            daily_rate=booking.daily_rate,
            extra_charges=booking.extra_charges,
        )

    def list_all(self) -> list[Booking]:
        rows = self.conn.execute("SELECT * FROM bookings ORDER BY booking_id").fetchall()
        return [self._row_to_booking(row) for row in rows]

    def update_status(self, booking_id: int, status: BookingStatus) -> None:
        self.conn.execute(
            "UPDATE bookings SET status = ? WHERE booking_id = ?",
            (status.value, booking_id),
        )

    def _row_to_booking(self, row: sqlite3.Row) -> Booking:
        return Booking(
            booking_id=row["booking_id"],
            user_id=row["user_id"],
            car_id=row["car_id"],
            start_date=date.fromisoformat(row["start_date"]),
            end_date=date.fromisoformat(row["end_date"]),
            status=BookingStatus(row["status"]),
            daily_rate=row["daily_rate"],
            extra_charges=row["extra_charges"],
        )
