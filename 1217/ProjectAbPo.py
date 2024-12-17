from abc import ABC, abstractmethod
#abstract class
class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def get_specs(self):
        pass
#concrete class

class Smartphone(Device):
    def turn_on(self):
        print("Turning on the smartphone...")

    def turn_off(self):
        print("Turning off the smartphone...")

    def get_specs(self):
        print("Smartphone specs: 6GB RAM, 128GB Storage, 6.5-inch Display")
        
class Laptop(Device):
    def turn_on(self):
        print("Turning on the laptop...")

    def turn_off(self):
        print("Turning off the laptop...")

    def get_specs(self):
        print("Laptop Specs: 16GB RAM, 1TB SSD, Intel i7 Processor")

class Tablet(Device):
    def turn_on(self):
        print("Turning on the tablet...")

    def turn_off(self):
        print("Turning off the tablet...")

    def get_specs(self):
        print("Tablet Specs: 4GB RAM, 64GB Storage, 10-inch Display")
        

smartphone = Smartphone()
laptop = Laptop()
tablet = Tablet()

#polymorphism
devices = [smartphone(), laptop(), tablet()]

for device in devices:
    device.turn_on()
    device.get_specs()
    device.turn_off()
    print()
    
    