
vehicles = []
customers = []
rentals = []

vehicle_id = 1
customer_id = 1
rental_id = 1


def add_vehicle():
    global vehicle_id

    name = input("Enter vehicle name: ")
    vehicle_type = input("Enter type (Car/Bike/Van): ")
    rate = float(input("Enter rent per day: "))

    vehicle = {
        "id": vehicle_id,
        "name": name,
        "type": vehicle_type,
        "rate": rate,
        "available": True
    }

    vehicles.append(vehicle)
    print("Vehicle added successfully!")
    vehicle_id += 1


def display_vehicles():
    if not vehicles:
        print("No vehicles available.")
        return

    print("\n--- Vehicle Details ---")
    for v in vehicles:
        status = "Available" if v["available"] else "Rented"
        print(
            f'ID: {v["id"]} | Name: {v["name"]} | '
            f'Type: {v["type"]} | Rate: Rs.{v["rate"]:.2f} | '
            f'Status: {status}'
        )


def register_customer():
    global customer_id

    name = input("Enter customer name: ")
    phone = input("Enter phone number: ")

    customer = {
        "id": customer_id,
        "name": name,
        "phone": phone
    }

    customers.append(customer)
    print("Customer registered successfully!")
    customer_id += 1


def display_customers():
    if not customers:
        print("No customers registered.")
        return

    print("\n--- Customer Details ---")
    for c in customers:
        print(
            f'ID: {c["id"]} | Name: {c["name"]} | '
            f'Phone: {c["phone"]}'
        )


def rent_vehicle():
    global rental_id

    display_vehicles()

    try:
        v_id = int(input("\nEnter vehicle ID to rent: "))
        c_id = int(input("Enter customer ID: "))
        days = int(input("Enter number of rental days: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    vehicle = next(
        (v for v in vehicles if v["id"] == v_id), None
    )
    customer = next(
        (c for c in customers if c["id"] == c_id), None
    )

    if vehicle is None:
        print("Vehicle not found.")
        return

    if customer is None:
        print("Customer not found.")
        return

    if not vehicle["available"]:
        print("Vehicle is already rented.")
        return

    if days <= 0:
        print("Rental days must be greater than zero.")
        return

    amount = vehicle["rate"] * days

    rental = {
        "id": rental_id,
        "vehicle": vehicle["name"],
        "vehicle_id": v_id,
        "customer": customer["name"],
        "customer_id": c_id,
        "days": days,
        "amount": amount,
        "status": "Active"
    }

    rentals.append(rental)
    vehicle["available"] = False

    print("\nVehicle rented successfully!")
    print(f"Rental ID: {rental_id}")
    print(f"Customer: {customer['name']}")
    print(f"Vehicle: {vehicle['name']}")
    print(f"Total rent: Rs.{amount:.2f}")

    rental_id += 1


def return_vehicle():
    try:
        r_id = int(input("Enter rental ID to return: "))
    except ValueError:
        print("Please enter a valid rental ID.")
        return

    rental = next(
        (r for r in rentals if r["id"] == r_id), None
    )

    if rental is None:
        print("Rental record not found.")
        return

    if rental["status"] == "Returned":
        print("This vehicle has already been returned.")
        return

    rental["status"] = "Returned"

    for v in vehicles:
        if v["id"] == rental["vehicle_id"]:
            v["available"] = True
            break

    print("Vehicle returned successfully!")


def display_rentals():
    if not rentals:
        print("No rental records found.")
        return

    print("\n--- Rental History ---")
    for r in rentals:
        print(
            f'Rental ID: {r["id"]} | '
            f'Customer: {r["customer"]} | '
            f'Vehicle: {r["vehicle"]} | '
            f'Days: {r["days"]} | '
            f'Amount: Rs.{r["amount"]:.2f} | '
            f'Status: {r["status"]}'
        )


def dashboard():
    available = sum(1 for v in vehicles if v["available"])
    active = sum(1 for r in rentals if r["status"] == "Active")
    returned = sum(1 for r in rentals if r["status"] == "Returned")

    print("\n--- Vehicle Management Dashboard ---")
    print("Total vehicles:", len(vehicles))
    print("Available vehicles:", available)
    print("Registered customers:", len(customers))
    print("Total rentals:", len(rentals))
    print("Active rentals:", active)
    print("Completed rentals:", returned)


while True:
    print("\n===== VEHICLE MANAGEMENT SYSTEM =====")
    print("1. Add Vehicle")
    print("2. Display Vehicles")
    print("3. Register Customer")
    print("4. Display Customers")
    print("5. Rent Vehicle")
    print("6. Return Vehicle")
    print("7. Display Rental History")
    print("8. Dashboard")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_vehicle()
    elif choice == "2":
        display_vehicles()
    elif choice == "3":
        register_customer()
    elif choice == "4":
        display_customers()
    elif choice == "5":
        rent_vehicle()
    elif choice == "6":
        return_vehicle()
    elif choice == "7":
        display_rentals()
    elif choice == "8":
        dashboard()
    elif choice == "9":
        print("Thank you for using the Vehicle Management System!")
        break
    else:
        print("Invalid choice. Please try again.")
