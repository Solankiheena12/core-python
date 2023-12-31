#  In Python, polymorphism is implemented through method overloading and method overriding.


# 1. Method Overloading:

# Method overloading refers to the ability of a class to define multiple methods with the same name
# but with a different parameters.


class MathOperations:
    def add(self, x, y=0, z=0):
        return x + y + z


# Creating an object of MathOperations class
math_obj = MathOperations()

# Calling the add method with different numbers of arguments
result1 = math_obj.add(2)
result2 = math_obj.add(2, 3)
result3 = math_obj.add(2, 3, 4)

print(result1)
print(result2)
print(result3)







class Student:
    def sub(self, x, y=6, z=0):
        return x - y - z


st = Student()

value1 = st.sub(10)
value2 = st.sub(9, 3)
value3 = st.sub(7, 1, 3)
value4 = st.sub(6)

print(value1)
print(value2)
print(value3)
print(value4)










# 2. Method Overriding:

# Method overriding occurs when a subclass provides a specific implementation for a method that
# is already defined in its superclass.


class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


class Cat(Animal):
    def sound(self):
        print("Cat meows")


# Creating objects of different classes
animal_obj = Animal()
dog_obj = Dog()
cat_obj = Cat()

# Calling the sound method for each object
animal_obj.sound()
dog_obj.sound()
cat_obj.sound()







class Exam:
    def pass_fail(self):
        print("in exam result is pass or fail")


class Oracle(Exam):
    def pass_fail(self):
        print("you passed out..")


class Python(Exam):
    def pass_fail(self):
        print("you passed out..")


class React(Exam):
    def pass_fail(self):
        print("you failed..")


ex = Exam()
ore = Oracle()
py = Python()
re = React()

ex.pass_fail()
ore.pass_fail()
py.pass_fail()
re.pass_fail()








# 3. Polymorphism in Python:

#  Polymorphism refers to having multiple forms. Polymorphism is a programming term that refers to the
# use of the same function name, but with different signatures


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")


class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("sail!")


class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("fly!")


car1 = Car("Toyota", "Toyota Fortuner")
boat1 = Boat("MasterCraft", "Ski Boats")
plane1 = Plane("Boeing Co", "Boeing 747-8")

for x in (car1, boat1, plane1):
    x.move()










class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def my_func(self):
        print("this is a unknown person")


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def my_func(self):
        print("this is a student")


class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def my_func(self):
        print("this is a employee")


p = Person("heena", 20)
st = Student("savan", 18)
emp = Employee("tina", 19)

for x in (p, st, emp):
    x.my_func()






class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()
