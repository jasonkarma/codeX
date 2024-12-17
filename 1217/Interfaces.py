#concrete class Inherits the interface, and should implement all the methods of the interface
from abc import ABC, abstractmethod

#interface class

class Drivable(ABC):
    @abstractmethod
    def start_engine(self):    
        pass
    def stop_engine(self):
        pass
    def drive(self):
        pass
    
#create two classes 

class Car(Drivable):
    def start_engine(self):
        print("Starting the engine")
    def drive(self):
        print("Driving the car")
    def stop_engine(self):
        print("Stopping the engine")
        
class Truck(Drivable):
    def start_engine(self):
        print("Starting the engine")
    def drive(self):
        print("Driving the truck")
    def stop_engine(self):
        print("Stopping the engine")
        
car = Car()
truck = Truck()

car.start_engine()
car.drive()
car.stop_engine()

truck.start_engine()
truck.drive()
truck.stop_engine()
    