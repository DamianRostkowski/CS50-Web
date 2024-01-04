class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        else:
            self.passengers.append(name)
            return True
    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)
people = ["Marek", "Arek", "Jonasz", "Maciek"]
for name in people:
    success = flight.add_passenger(name)
    if success:
        print(f"Added {name} to flight successfully.")
    else:
        print(f"No available seats for {name}.")
