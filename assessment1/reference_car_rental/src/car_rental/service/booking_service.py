"""预订业务。"""

from __future__ import annotations

from datetime import date

from model import Booking, BookingStatus
from repository import BookingRepository, CarRepository


class BookingService:
    def __init__(self, bookings: BookingRepository, cars: CarRepository) -> None:
        self.bookings = bookings
        self.cars = cars

    def create_booking(
        self,
        user_id: int,
        car_id: int,
        start_date: date,
        end_date: date,
        daily_rate: float,
        extra_charges: float = 0.0,
    ) -> Booking:
        car = self.cars.find_by_id(car_id)
        if car is None:
            raise ValueError("车辆不存在")
        if not car.available_now:
            raise ValueError("车辆当前不可用")

        booking = Booking(
            booking_id=None,
            user_id=user_id,
            car_id=car_id,
            start_date=start_date,
            end_date=end_date,
            status=BookingStatus.PENDING,
            daily_rate=daily_rate,
            extra_charges=extra_charges,
        )
        return self.bookings.create(booking)

    def approve_booking(self, booking_id: int) -> None:
        self.bookings.update_status(booking_id, BookingStatus.APPROVED)

    def reject_booking(self, booking_id: int) -> None:
        self.bookings.update_status(booking_id, BookingStatus.REJECTED)
