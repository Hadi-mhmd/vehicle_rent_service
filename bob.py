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

    # def show_vehicle_info(self):
    #     self.display_info()  
   




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

# car.display_info()
# R1.display_info()

def show_vehicle_info(vehicle):
    vehicle.display_info()
show_vehicle_info(car)
show_vehicle_info(R1)


days=int(input("enter the number of days to rent for: "))


print(f"Cost of rent for {car.brand} {car.model} for {days} days is = {car.calculate_rental_cost(days)}")
print(f"Cost of rent for {R1.brand} {R1.model} for {days} days is = {R1.calculate_rental_cost(days)}")

R1.set_rental_price_per_day(100)
# print(f"new rental price is ${R1.get_rental_price_per_day()}")
# show_vehicle_info(car)
# show_vehicle_info(R1)



# if we put show function inside the behicle class
# car.show_vehicle_info()
# R1.show_vehicle_info()

