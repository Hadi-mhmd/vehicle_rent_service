class Vehicle:
    def __init__(self,brand,year,rental_price_per_day):
        self.brand = brand
        self.year = year
        self.rental_price_per_day = rental_price_per_day
    
    def display_info(self):
        print(f"{self.brand} {self.model}, Year: {self.year}, Rental price: ${self.rental_price_per_day}/day")

    def calculate_rental_cost(self,days):
        return  self.rental_price_per_day * days   

