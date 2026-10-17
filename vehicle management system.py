from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, vehicle_id, brand, rate):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.rate = rate
        self.available = True

    @abstractmethod
    def display(self):
        pass

    def calculate_rent(self, days):
        return self.rate * days


class Car(Vehicle):
    def display(self):
        print(f"Car: {self.vehicle_id} | {self.brand} "
              f"| Rate: {self.rate}/day | Available: {self.available}")


class Bike(Vehicle):
    def display(self):
        print(f"Bike: {self.vehicle_id} | {self.brand} "
              f"| Rate: {self.rate}/day | Available: {self.available}")


class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name


class RentalService:
    def __init__(self):
        self.vehicles = []
        self.customers = []
        self.rentals = {}

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        print("Vehicle added successfully.")

    def register_customer(self, customer):
        self.customers.append(customer)
        print("Customer registered successfully.")

    def show_vehicles(self):
        for vehicle in self.vehicles:
            vehicle.display()

    def rent_vehicle(self, vehicle_id, customer_id, days):
        vehicle = next(
            (v for v in self.vehicles
             if v.vehicle_id == vehicle_id), None
        )
        customer = next(
            (c for c in self.customers
             if c.customer_id == customer_id), None
        )

        if not vehicle or not customer:
            print("Invalid vehicle or customer ID.")
        elif not vehicle.available:
            print("Vehicle is already rented.")
        elif days <= 0:
            print("Days must be greater than zero.")
        else:
            vehicle.available = False
            self.rentals[vehicle_id] = (customer_id, days)
            print("Rental successful.")

    def return_vehicle(self, vehicle_id):
        vehicle = next(
            (v for v in self.vehicles
             if v.vehicle_id == vehicle_id), None
        )

        if vehicle and vehicle_id in self.rentals:
            customer_id, days = self.rentals.pop(vehicle_id)
            bill = vehicle.calculate_rent(days)
            vehicle.available = True
            print(f"Vehicle returned. Rental charge: Rs.{bill}")
        else:
            print("No active rental found.")


service = RentalService()

while True:
    print("""
1. Add Car
2. Add Bike
3. Register Customer
4. Display Vehicles
5. Rent Vehicle
6. Return Vehicle
7. Exit
""")
    choice = input("Enter choice: ")

    if choice in ("1", "2"):
        vid = input("Vehicle ID: ")
        brand = input("Brand: ")
        rate = float(input("Rent per day: "))
        if rate <= 0:
            print("Rate must be positive.")
            continue
        vehicle = Car(vid, brand, rate) if choice == "1" \
            else Bike(vid, brand, rate)
        if any(v.vehicle_id == vid for v in service.vehicles):
            print("Vehicle ID already exists.")
        else:
            service.add_vehicle(vehicle)

    elif choice == "3":
        cid = input("Customer ID: ")
        name = input("Customer name: ")
        if any(c.customer_id == cid for c in service.customers):
            print("Customer ID already exists.")
        else:
            service.register_customer(Customer(cid, name))

    elif choice == "4":
        service.show_vehicles()

    elif choice == "5":
        vid = input("Vehicle ID: ")
        cid = input("Customer ID: ")
        try:
            days = int(input("Number of days: "))
            service.rent_vehicle(vid, cid, days)
        except ValueError:
            print("Enter a valid number of days.")

    elif choice == "6":
        service.return_vehicle(input("Vehicle ID: "))

    elif choice == "7":
        break

    else:
        print("Invalid choice.")