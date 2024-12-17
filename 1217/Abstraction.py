from abc import ABC, abstractmethod

#abstract class 
class Vehicle(ABC):
    @abstractmethod
    def max_speed(self):  #abstract method
        pass
    
    @abstractmethod
    def fuel_type(self):  #abstract method
        pass
    
#Concrete Class for car
class Car(Vehicle):
    
    def max_speed(self):
        return 200
    
    def fuel_type(self):
        return "Petrol"
    
#Concrete Class for Bike

class Bike(Vehicle):
    
    def max_speed(self):
        return 120
    def fuel_type(self):
        return "Electric"
    
#Create objects for car and bike 
car=Car()
bike=Bike()

#call their max_speed() and fuel_type()

print("Car Max Speed:" , car.max_speed(), "km/h")
print("Car Fuel Type:" , car.fuel_type())

print("Bike Max Speed:" , bike.max_speed(), "km/h")
print("Bike Fuel Type:" , bike.fuel_type())

