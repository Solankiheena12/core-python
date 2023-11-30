#  a process of handling complexity by hiding unnecessary information from the user.


class Shape():
    def area(self):
        pass
    
    def perimeter(self):
        pass

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius
    
circle = Circle(5)
print("Circle Area:", circle.area())
print("Circle Perimeter:", circle.perimeter())





class Vehicle():
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self): 
        pass

    def stop(self):
        pass


class Car(Vehicle):
    def start(self):
        return f"{self.brand} {self.model} is starting."
    
    def stop(self):
        return f"{self.brand} {self.model} is stopping."
    

class Plane(Vehicle):
    def start(self):
        return f"{self.brand} {self.model} now plan is flying!"
    
    def stop(self):
        return f"{self.brand} {self.model} is now landing!"
    

car = Car("toyota", "camry")
plane = Plane("Boeing", "747")

print(car.start())
print(car.stop())
print(plane.start())
print(plane.stop())
