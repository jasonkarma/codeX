#Implement Polymorphism with Method Overloading
class MathOperations:
    def multiply(self, a, b, c=1):
        return a * b * c
    
calc= MathOperations()

print (calc.multiply(1, 2))
print(calc.multiply(3, 6, 3))

#Implement Polymorphism with Method Overriding

class Shape:
    def area(self):
        print("calculating area...")
        
class Circle(Shape):
    def area(self,radius):
        π = 3.1415926
        return π * (radius**2)
    
calc2 = Circle()

print(calc2.area(2))
