# Parent Class
class Car:
    def start(self):
        print("Car is starting in normal mode")
# Child Class (Method Overriding)
class ElectricCar(Car):
    def start(self):
        print("Electric car is starting silently")
# Creating Objects
c1 = Car()
c2 = ElectricCar()
# Calling Methods
c1.start() # Parent class method
c2.start() # Overridden method in child class
