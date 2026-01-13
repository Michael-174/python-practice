def request_ride():
    print("=== Request a Ride ===")

    pickup_location = input("Enter pickup location: ")
    dropoff_location = input("Enter drop-off location: ")

    ride_request = {
        "pickup": pickup_location,
        "dropoff": dropoff_location
    }

    print("\nRide Requested Successfully!")
    print("Pickup Location:", ride_request["pickup"])
    print("Drop-off Location:", ride_request["dropoff"])

    return ride_request
