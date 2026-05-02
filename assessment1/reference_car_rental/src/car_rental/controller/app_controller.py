"""控制层：组织 demo 流程，模拟入口调用。"""

from __future__ import annotations

from datetime import date

from model import Car, Role
from repository import BookingRepository, CarRepository, UserRepository, DEFAULT_DB_PATH, get_connection, initialize_database
from service import AuthService, BookingService, CarService


def run_demo() -> None:
    initialize_database(DEFAULT_DB_PATH)

    with get_connection(DEFAULT_DB_PATH) as conn:
        users = UserRepository(conn)
        cars = CarRepository(conn)
        bookings = BookingRepository(conn)

        auth = AuthService(users)
        car_service = CarService(cars)
        booking_service = BookingService(bookings, cars)

        admin = auth.register("Admin User", "admin2@example.com", "admin123", Role.ADMIN)
        customer = auth.register("Alice Customer", "alice2@example.com", "alice123", Role.CUSTOMER)

        car_service.add_car(
            Car(
                car_id=None,
                make="Toyota",
                model="Corolla",
                year=2023,
                mileage=12000,
                available_now=True,
                minimum_rent_period=1,
                maximum_rent_period=14,
            )
        )

        available_cars = car_service.list_available_cars()
        booking = booking_service.create_booking(
            user_id=customer.user_id or 0,
            car_id=available_cars[0].car_id or 0,
            start_date=date(2026, 5, 10),
            end_date=date(2026, 5, 13),
            daily_rate=45.0,
            extra_charges=15.0,
        )
        booking_service.approve_booking(booking.booking_id or 0)

        print("== Demo Users ==")
        for user in users.list_all():
            print(user)

        print("\n== Demo Cars ==")
        for car in car_service.list_available_cars():
            print(car)

        print("\n== Demo Booking ==")
        print(booking)
        print("Total fee:", booking.total_fee())

        print("\n管理员：", admin.full_name)
