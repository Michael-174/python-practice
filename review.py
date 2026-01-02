from collections import deque
queue = deque()
for i in range(5):
    plate = input(f"Enter license plate number for car {i+1}: ")
    queue.append(plate)

print("\nAll cars have arrived.")
print("Queue:", queue)

menu = ["Basic Wash", "Deluxe Wash", "Premium Detailing"]


print("\n--- Serving Cars ---")
while queue:
    car = queue.popleft()

    print(f"\nNow serving car with license plate: {car}")

    print("Menu options:")
    for item in menu:
        print("-", item)
    print(f"Car {car} has been served and removed from the queue.")

print("\nAll cars served. The queue is now empty.")