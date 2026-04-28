# Base Class
class Vehicle:
    def __init__(self, model, rental_rate):
        self.model = model
        self.rental_rate = rental_rate

    def calculate_rental(self, days):
        return self.rental_rate * days


# Car Class (extra insurance per day)
class Car(Vehicle):
    def __init__(self, model, rental_rate, insurance_per_day):
        super().__init__(model, rental_rate)
        self.insurance_per_day = insurance_per_day

    def calculate_rental(self, days):
        return (self.rental_rate + self.insurance_per_day) * days


# Bike Class (discount if rented more than 3 days)
class Bike(Vehicle):
    def __init__(self, model, rental_rate):
        super().__init__(model, rental_rate)

    def calculate_rental(self, days):
        total = self.rental_rate * days
        if days > 3:
            total = total * 0.9   # 10% discount
        return total


# Truck Class (fixed extra charge)
class Truck(Vehicle):
    def __init__(self, model, rental_rate, extra_charge):
        super().__init__(model, rental_rate)
        self.extra_charge = extra_charge

    def calculate_rental(self, days):
        return (self.rental_rate * days) + self.extra_charge


# -------- Polymorphism Demo --------
vehicles = [
    Car("Honda City", 2000, 200),
    Bike("Hero Splendor", 500),
    Truck("Tata", 3000, 1500)
]

days = 5

for v in vehicles:
    print(v.model, "Rental Cost:", v.calculate_rental(days))