class Car:                  # create class named Car
    def __init__(self, name, roll):         # define __init__(self) method
        self.name = name
        self.roll = roll

car1 = Car("toyota", 10)            # create object named car1
print(car1.name)
print(car1.roll)



class Student:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

stu = Student("heena", 20, "rajkot")
print(stu.name)
print(stu.age)
print(stu.city)




# __str__(self) method :

class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __str__(self):
        return f"{self.name}({self.id})"
    
p1 = Person("keval", 11)
print(p1)


class Test:
    def __init__(self, sub, marks):
        self.sub = sub
        self.marks = marks

    def __str__(self):
        return f"{self.sub}({self.marks})"
    
t1 = Person("maths", 86)
print(t1)





# object methods:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def my_func(self):
        print("my name is " + self.name)

p1 = Person("heena", 20)
p1.my_func()



class Demo:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def my_func(self):
        print("my name is " + self.name + " and my city is " + self.city)

d1 = Demo("vihaa", "rajkot")
d1.my_func()



# modify object property:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def my_func(self):
        print("my age is " + self.age)

p1 = Person("darshan", 15)
p1.age = 14
print(p1.age)