import random
import datetime

BASE_FARE = 5.00
RATE_PER_KM = 2.00
SERVICE_FEE = 3.00
HST_RATE = 0.13
distance_traveled = 0

def create_account():
    print("---------------- Apple Uber Ride Booking Service Program ----------------")
    name = input("Please enter your full name: ")
    while True:
        email = input("Please enter your email address: ")
        if "@" in email and "." in email:
            break
        else:
            print("Please enter an email address in the correct format.")
    while True:
        phone = input("Please enter your phone number: ")
        if len(phone) >= 10 and phone.isdigit():
            break
        else:
            print("Please enter a phone number in the correct format.")
    print("Account created successfully")
    print("Your name:", name)
    print("Your email address:", email)
    print("Your phone number:", phone)
    return {"name": name, "email": email, "phone": phone}

def request_ride():
    print("---------------- Request a Ride ----------------")
    pickup_location = input("Enter pickup location: ")
    dropoff_location = input("Enter drop-off location: ")
    ride_request = {"pickup": pickup_location, "dropoff": dropoff_location}
    print("\nRide Requested Successfully!")
    print("Pickup Location:", ride_request["pickup"])
    print("Drop-off Location:", ride_request["dropoff"])
    return ride_request

def share_driver_info():
    drivers = [
        {"name": "Thinh", "rating": 4.5, "car": "Rolls-Royce Phantom", "plate": "ABC-123"},
        {"name": "Timmy", "rating": 4.7, "car": "McLaren 720s", "plate": "XYZ-456"},
        {"name": "Michael", "rating": 4.6, "car": "Leopard tank 2A7", "plate": "LMN-789"},
        {"name": "Jawei", "rating": 4.8, "car": "Optimus Prime", "plate": "QRS-321"}
    ]
    driver = random.choice(drivers)
    print("\n------ Driver Assigned ------")
    print("Name:", driver["name"])
    print("Rating:", driver["rating"])
    print("Car:", driver["car"])
    print("License Plate:", driver["plate"])
    return driver

def calculate_ride_cost():
    global distance_traveled
    distance_traveled = float(input("\nEnter distance traveled (km): "))
    distance_cost = distance_traveled * RATE_PER_KM
    subtotal = BASE_FARE + distance_cost + SERVICE_FEE
    hst = subtotal * HST_RATE
    total = subtotal + hst
    print("\n------ Ride Cost Breakdown ------")
    print(f"Base Fare: ${BASE_FARE:.2f}")
    print(f"Distance Cost: ${distance_cost:.2f}")
    print(f"Service Fee: ${SERVICE_FEE:.2f}")
    print(f"HST (13%): ${hst:.2f}")
    print(f"Total Cost: ${total:.2f}")
    return {"base_fare": BASE_FARE, "distance_cost": distance_cost, "service_fee": SERVICE_FEE, "hst": hst, "total": total}

def estimate_ride_cost():
    global distance_traveled
    current_hour = datetime.datetime.now().hour
    if (7 <= current_hour <= 9) or (16 <= current_hour <= 19):
        multiplier = 1.5
        pricing_type = "Peak Hours"
    else:
        multiplier = 1.0
        pricing_type = "Off-Peak Hours"
    distance_cost = distance_traveled * RATE_PER_KM
    subtotal = (BASE_FARE + distance_cost + SERVICE_FEE) * multiplier
    hst = subtotal * HST_RATE
    estimated_total = subtotal + hst
    print("\n------ Estimated Ride Cost (Dynamic Pricing) ------")
    print("Pricing Type:", pricing_type)
    print("Surge Multiplier:", multiplier)
    print(f"Estimated Total: ${round(estimated_total,2)}")
    return estimated_total

def generate_invoice(user, ride, driver, fare):
    global distance_traveled
    print("\n------ APPLE UBER INVOICE ------")
    print("\nPassenger Information")
    print("Name:", user["name"])
    print("Email:", user["email"])
    print("Phone:", user["phone"])
    print("\nRide Details")
    print("Pickup Location:", ride["pickup"])
    print("Drop-off Location:", ride["dropoff"])
    print(f"Distance Traveled: {distance_traveled} km")
    print("\nDriver Information")
    print("Name:", driver["name"])
    print("Car:", driver["car"])
    print("License Plate:", driver["plate"])
    print("Rating:", driver["rating"])
    print("\nFare Breakdown")
    print(f"Base Fare: ${fare['base_fare']:.2f}")
    print(f"Distance Cost: ${fare['distance_cost']:.2f}")
    print(f"Service Fee: ${fare['service_fee']:.2f}")
    print(f"HST (13%): ${fare['hst']:.2f}")
    print(f"Total Cost: ${fare['total']:.2f}")
    print("------------------------------")

def ride_survey():
    print("\n------ Ride Feedback Survey ------")
    professionalism = input("Rate the driver's professionalism and behavior (1–5): ")
    cleanliness = input("Rate the cleanliness and condition of the car (1–5): ")
    route_accuracy = input("Rate the accuracy and efficiency of the route (1–5): ")
    feedback = {"professionalism": professionalism, "cleanliness": cleanliness, "route_accuracy": route_accuracy}
    print("\nThank you for completing the survey!")
    return feedback

def apple_uber_app():
    print("===== Welcome to Apple Uber Ride Booking Service =====")
    choice = input("Do you want to book a ride? (yes/no): ").lower()
    if choice != "yes":
        print("Thank you. Application closed.")
        return
    user = create_account()
    ride = request_ride()
    fare = calculate_ride_cost()
    estimate_ride_cost()
    driver = share_driver_info()
    generate_invoice(user, ride, driver, fare)
    ride_survey()
    print("\nThank you for using Apple Uber Ride Booking Service!")

apple_uber_app()
