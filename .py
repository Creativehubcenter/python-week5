# Defining a class with more attributes and methods
class Car:
    def __init__(self, color, brand, speed=0):
        self.color = color        
        self.brand = brand        
        self.speed = speed        

    def drive(self):
        self.speed += 10
        print(f"{self.brand} is driving at {self.speed} km/h 🚗")

    def stop(self):
        self.speed = 0
        print(f"{self.brand} has stopped 🛑")

# Creating an object
my_car = Car("blue", "Toyota")
print(my_car.color)     
my_car.drive()          
my_car.drive()          
my_car.stop()           