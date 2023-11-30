# inheritance provide code reusability to the program because we can use an existing class to create a new class 
# instead of creating it from scratch.

#  in inheritance, the child class can access all the data members and functions defined in the parent class.

# a child class also provide its specific implementation to the function of the parent class


# without __init__() method :


class Animal:
    def speak(self):
        print("animal speaks")

class Dog(Animal):
    def bark(self):
        print("dog barks")

dog = Dog()
dog.speak()
dog.bark()




class Test:
    def marks(self):
        print("marks of test")

class Demo(Test):
    def live(self):
        print("live demo")

demo = Demo()
demo.marks()
demo.live()


# Create a Parent Class :


class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def my_func(self):
        print(self.firstname, self.lastname)


p1 = Person("heena", "solanki")
p1.my_func()


# Create a Child Class :


class Test:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def my_func(self):
        print(self.name, self.age)


class Student(Test):
    pass


t1 = Student("niya", 4)
t1.my_func()


# Add the __init__() Function :


class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def my_func(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
        
s1 = Student("harvi", "solanki")
s1.my_func()
