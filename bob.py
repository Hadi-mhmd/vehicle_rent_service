class Vehicle:
    def __init__(self,brand,model,year,rental_price_per_day):
        self.brand = brand
        self.year = year
        self.model = model
        self.__rental_price_per_day = rental_price_per_day
        
    
    def display_info(self):
        print(f"{self.brand} {self.model}, Year: {self.year}, Rental price: ${self.__rental_price_per_day}/day")

    def calculate_rental_cost(self,days):
        return  self.__rental_price_per_day * days   

    def get_rental_price_per_day(self):
        return self.__rental_price_per_day

    def set_rental_price_per_day(self,newPrice):
        if newPrice>0:
          self.__rental_price_per_day=newPrice
        else:
            print("price cannot be negative")    




class Car(Vehicle):
    def __init__(self,brand,model,year,rental_price_per_day,seating_capacity):
        self.seating_capacity = seating_capacity
        super().__init__(brand,model,year,rental_price_per_day)

    def display_info(self):
        print(f"{self.brand} {self.model}, Year: {self.year},Seats number:{self.seating_capacity} Rental price: ${self.get_rental_price_per_day()}/day")


class Motorcycle(Vehicle):
    def __init__(self,brand,model,year,rental_price_per_day,engine_capacity):
        self.engine_capacity = engine_capacity
        super().__init__(brand,model,year,rental_price_per_day) 

    def display_info(self):
        print(f"{self.brand} {self.model}, Year: {self.year}, Engine power: {self.engine_capacity}CC, Rental price: ${self.get_rental_price_per_day()}/day")

car=Car("toyota","corolla",2020,50,5)
R1=Motorcycle("yamaha","R1",2019,30,1000)           

car.display_info()
R1.display_info()