from abc import ABC, abstractmethod
import datetime


# Base Vehicle class
class Vehicle(ABC):
    def __init__(self, make, model, year, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.status = 'available'  # default status

    @abstractmethod
    def display_info(self):
        pass

    def update_status(self, new_status):
        self.status = new_status
        VehicleLogger.log_status_change(self)

    def log_mileage(self, miles):
        self.mileage += miles
        VehicleLogger.log_mileage(self)


# Derived classes for specific vehicle types
class Truck(Vehicle):
    def __init__(self, make, model, year, mileage, load_capacity):
        super().__init__(make, model, year, mileage)
        self.load_capacity = load_capacity

    def display_info(self):
        print(f"Truck: {self.make} {self.model}, Capacity: {self.load_capacity} tons")


class Van(Vehicle):
    def __init__(self, make, model, year, mileage, passenger_capacity):
        super().__init__(make, model, year, mileage)
        self.passenger_capacity = passenger_capacity

    def display_info(self):
        print(f"Van: {self.make} {self.model}, Passengers: {self.passenger_capacity}")


class Car(Vehicle):
    def __init__(self, make, model, year, mileage, employee):
        super().__init__(make, model, year, mileage)
        self.employee = employee

    def display_info(self):
        print(f"Car: {self.make} {self.model}, Assigned to: {self.employee}")


# Logger class for tracking vehicle events
class VehicleLogger:
    @staticmethod
    def log_status_change(vehicle):
        print(f"Vehicle status updated: {vehicle.make} {vehicle.model} is now {vehicle.status}")

    @staticmethod
    def log_mileage(vehicle):
        print(f"Vehicle mileage updated: {vehicle.make} {vehicle.model} has {vehicle.mileage} miles")


# Maintenance scheduler class
class MaintenanceScheduler:
    MAINTENANCE_INTERVAL = 10000  # miles

    @staticmethod
    def check_maintenance(vehicle):
        if vehicle.mileage >= MaintenanceScheduler.MAINTENANCE_INTERVAL:
            print(f"Vehicle {vehicle.make} {vehicle.model} is due for maintenance.")


# Example usage
if __name__ == '__main__':
    truck = Truck("Volvo", "FH16", 2020, 8000, 20)
    van = Van("Ford", "Transit", 2019, 12000, 12)
    car = Car("Toyota", "Corolla", 2018, 5000, "Alice Smith")

    vehicles = [truck, van, car]

    # Display vehicle info
    for vehicle in vehicles:
        vehicle.display_info()

    # Log mileage and check maintenance
    for vehicle in vehicles:
        vehicle.log_mileage(500)
        MaintenanceScheduler.check_maintenance(vehicle)

    # Update and log vehicle status
    truck.update_status('on job')
    van.update_status('under maintenance')
    car.update_status('available')
