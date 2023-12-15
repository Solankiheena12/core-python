#len()
x="hello world!"                  #string
print(len(x))

mytuple=("apple","banana","mango")          #tuple
print(len(mytuple))

mydict={"name":"bansi","city":"rajot","mobile":7575848392}          #dictionary
print(len(mydict))



#class polymorphism:
class car:
    def __init__(self, brand, model):
        self.brand=brand
        self.model=model
    def move(self):
        print("drive")
class boat:
    def __init__(self, brand, model):
        self.brand=brand
        self.model=model
    def move(self):
        print("sail")
class plane:
    def __init__(self, brand, model):
        self.brand=brand
        self.model=model
    def move(self):
        print("fly")
car1 = car("Ford", "Mustang")       
boat1 = boat("Ibiza", "Touring 20") 
plane1 = plane("Boeing", "747")    
for x in (car1, boat1, plane1):
    x.move()


class car:
    def __init__(self, brand, model):
        self.brand=brand
        self.model=model
    def move(self):
        print("long drive")
class boat:
    def __init__(self, brand, model):
        self.brand=brand
        self.model=model
    def move(self):
        print("sail")
class plane:
    def __init__(self, brand, model):
        self.brand=brand
        self.model=model
    def move(self):
        print("high flying")
car1=car("Ford", "Mustang")
boat1=boat("Ibiza", "Touring 20")
plane1=plane("Boeing", "747")
for x in (car1, boat1, plane1):
    x.move()


print("hello world")

#Inheritance Class Polymorphism:
class vehicle:
    def __init__(self, brand, model):
        self.brand=brand
        self.model=model
    def move(self):
        print("move")
class car(vehicle):
    pass
class boat(vehicle):
    def move(self):
        print("sail")
class plane(vehicle):
    def move(self):
        print("fly")
car1=car("Ford", "Mustang")
boat1=boat("Ibiza", "Touring 20")
plane1=plane("Boeing", "747")
for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model) 
    x.move()      


class vehicle:
    def __init__(self, brand, model):
        self.brand=brand
        self.model=model
    def move(self):
        print("move")
class car(vehicle):
    pass
class boat(vehicle):
    pass
class plane(vehicle):
    def __init__(self, brand, model):
        self.brand=brand
        self.model=model
    def move(self):
        print("fly")
car1=car("ford","mustang")
boat1=boat("Ibiza", "Touring 20")
plane1=plane("Boeing", "747")
for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move()