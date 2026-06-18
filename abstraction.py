from abc import ABC, abstractmethod

# Abstract Class
class Vehicle(ABC):

    @abstractmethod
    def fuel_type(self):
        pass

# Child Class 1
class PetrolCar(Vehicle):
    def fuel_type(self):
        print("Fuel Type: Petrol")

# Child Class 2
class ElectricCar(Vehicle):
    def fuel_type(self):
        print("Fuel Type: Electric")

# Creating Objects
car1 = PetrolCar()
car2 = ElectricCar()

# Calling Methods
car1.fuel_type()
car2.fuel_type()
