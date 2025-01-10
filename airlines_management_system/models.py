class Flight:
    def __init__(self, flight_number, origin, destination, price):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.price = price

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

# In-memory data storage
flights = [
    Flight("AA101", "New York", "Los Angeles", 300),
    Flight("AA102", "Chicago", "Miami", 200),
    Flight("AA103", "San Francisco", "Seattle", 150),
]

users = {
    "admin": User("admin", "password"),  # Example user
}

bookings = []  # List to store booked flights