"""Car 仓储。"""

from __future__ import annotations

from dataclasses import asdict
import sqlite3

from model import Car


class CarRepository:
    def __init__(self, conn: sqlite3.Connection) -> None:
        self.conn = conn

    def create(self, car: Car) -> Car:
        cursor = self.conn.execute(
            """
            INSERT INTO cars (make, model, year, mileage, available_now, minimum_rent_period, maximum_rent_period)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                car.make,
                car.model,
                car.year,
                car.mileage,
                int(car.available_now),
                car.minimum_rent_period,
                car.maximum_rent_period,
            ),
        )
        return Car(car_id=cursor.lastrowid, **{key: value for key, value in asdict(car).items() if key != "car_id"})

    def list_available(self) -> list[Car]:
        rows = self.conn.execute(
            "SELECT * FROM cars WHERE available_now = 1 ORDER BY car_id"
        ).fetchall()
        return [self._row_to_car(row) for row in rows]

    def find_by_id(self, car_id: int) -> Car | None:
        row = self.conn.execute("SELECT * FROM cars WHERE car_id = ?", (car_id,)).fetchone()
        return self._row_to_car(row) if row else None

    def update(self, car: Car) -> None:
        self.conn.execute(
            """
            UPDATE cars
            SET make = ?, model = ?, year = ?, mileage = ?, available_now = ?,
                minimum_rent_period = ?, maximum_rent_period = ?
            WHERE car_id = ?
            """,
            (
                car.make,
                car.model,
                car.year,
                car.mileage,
                int(car.available_now),
                car.minimum_rent_period,
                car.maximum_rent_period,
                car.car_id,
            ),
        )

    def delete(self, car_id: int) -> None:
        self.conn.execute("DELETE FROM cars WHERE car_id = ?", (car_id,))

    def _row_to_car(self, row: sqlite3.Row) -> Car:
        return Car(
            car_id=row["car_id"],
            make=row["make"],
            model=row["model"],
            year=row["year"],
            mileage=row["mileage"],
            available_now=bool(row["available_now"]),
            minimum_rent_period=row["minimum_rent_period"],
            maximum_rent_period=row["maximum_rent_period"],
        )
