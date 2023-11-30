# constructor is a special method that is automatically called when an object is created. 
# It is used to initialize the attributes of the object. 
# The constructor method is named __init__ and is defined within a class

class Employee():
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def my_func(self):
        print("Employee Name :", self.name)
        print("Employee Salary :", self.salary)
        print("\n")

first = Employee("heena", 10000)
second = Employee("darshan", 20000)
third = Employee("savan", 30000)
fourth = Employee("harvi", 5000)

first.my_func()
second.my_func()
third.my_func()
fourth.my_func()






class Person():
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def my_func(self):
        print("Person Name: ", self.name)
        print("Person Salary is: ", self.salary)
        print("\n")

p1 = Person("heena", 10000)
p2 = Person("roohi", 11000)
p3 = Person("keval", 5000)

p1.my_func()
p2.my_func()
p3.my_func()






class Student():
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def my_role(self):
        print("Student Name is: ", self.name)
        print("Student Age is: ", self.age)
        print("Student Grade is: ", self.grade)
        print("\n")

s1 = Student("riya", 10, "A")
s2 = Student("tina", 13, "B")
s3 = Student("niya", 15, "A")

s1.my_role()
s2.my_role()
s3.my_role()






class Test():
    def __init__(self, name, sub, marks):
        self.name = name
        self.sub = sub
        self.marks = marks

    def unit_test(self):
        print("Unit test name: ", self.name)
        print("subjects is: ", self.sub)
        print("marks are: ", self.marks)
        print("\n")

first = Test("first unit test", "C++", 28)
second = Test("second unit test", "Oracle", 56)
third = Test("third unit test", "Python", 68)

first.unit_test()
second.unit_test()
third.unit_test()
