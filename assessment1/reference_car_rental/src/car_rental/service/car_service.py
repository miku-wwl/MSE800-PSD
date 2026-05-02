"""车辆业务。"""

from __future__ import annotations

from model import Car
from repository import CarRepository


class CarService:
    def __init__(self, cars: CarRepository) -> None:
        self.cars = cars

    def add_car(self, car: Car) -> Car:
        return self.cars.create(car)

    def update_car(self, car: Car) -> None:
        if car.car_id is None:
            raise ValueError("car_id 不能为空")
        self.cars.update(car)

    def remove_car(self, car_id: int) -> None:
        self.cars.delete(car_id)

    def list_available_cars(self) -> list[Car]:
        return self.cars.list_available()
