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
