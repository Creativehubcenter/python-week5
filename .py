class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self.origin = origin

    def introduce(self):
        print(f"I am {self.name} from {self.origin}, and I wield the power of {self.power} 💥")

    def use_power(self):
        print(f"{self.name} uses {self.power}!")

class FlyingHero(Superhero):
    def __init__(self, name, power, origin, flight_speed):
        super().__init__(name, power, origin)
        self.__flight_speed = flight_speed  

    def use_power(self):
        print(f"{self.name} soars through the sky at {self.__flight_speed} km/h ✈️ using {self.power}!")

    def get_flight_speed(self):
        return self.__flight_speed

hero1 = Superhero("SolarFlare", "Heat Vision", "Sun City")
hero2 = FlyingHero("SkyBolt", "Wind Manipulation", "Cloud Haven", 300)

hero1.introduce()
hero1.use_power()

hero2.introduce()
hero2.use_power()
print(f"Flight speed: {hero2.get_flight_speed()} km/h")

class Vehicle:
    def move(self):
        print("The vehicle is moving.")


class Car(Vehicle):
    def move(self):
        print("Driving on the road 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying through the sky ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing across the ocean 🚢")

vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()