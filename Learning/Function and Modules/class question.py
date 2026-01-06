# define a passenger class and print a passenger’s info
class Pssenger:
    def __init__(self, name, number, destination, seat):
        self.name = name
        self.number = number
        self.destination = destination
        self.seat = seat
    def display_info(self):
        print("Passenger name: " + self.name,
              "\nPassport number: " + self.number,
              "\nDestination: " + self.destination,
              "\nSeat number: " + self.seat)

passenger1 = Pssenger("Michael", "67", "Toronto", "A1")
print(passenger1.display_info())