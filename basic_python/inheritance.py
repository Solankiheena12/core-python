#Create a Parent Class:
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
x = Person("John", "Doe")
x.printname()

class test:
    def __init__(self, fname, lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)
x=test("bansi","patel")
x.printname()
        
class demo:
    def __init__(self, fname, lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)
x=demo("maahi","patel")
x.printname()

class mydemo:
    def __init__(self, city, state):
        self.city=city
        self.state=state
    def printname(self):
        print(self.city,self.state)
x=mydemo("rajkot","gujarat")
x.printname()
        


#Create a Child Class:
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
  pass
x = Student("Mike", "Olsen")
x.printname()

class demo:
    def __init__(self, fname, lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)
class test(demo):
    pass
x=test("bansi","patel")
x.printname()

class mydemo:
    def __init__(self, fname, lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)
class test(mydemo):
    pass
x=test("riya","patel")
x.printname()



#Add the __init__() Function:
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)
x = Student("Mike", "Olsen")
x.printname()

class demo:
    def __init__(self, fname, lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)
class test(demo):
    def __init__(self, fname, lname):
        demo.__init__(self, fname, lname)
x=test("darshan","solanki")
x.printname()

class mydemo:
    def __init__(self, fname, lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)
class mytest(mydemo):
    def __init__(self, fname, lname):
        mydemo.__init__(self, fname, lname)
x=mytest("gopi","solanki")
x.printname()



#super()-->it will automatically inherit the methods and properties from its parent.
#Use the super() Function:
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
x = Student("Mike", "Olsen")
x.printname()

class mydemo:
    def __init__(self, fname, lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)
class mytest(mydemo):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
x=mytest("gopi","solanki")
x.printname()

class demo:
    def __init__(self, fname, lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)
class test(demo):
   def __init__(self, fname, lname):
       super().__init__(fname, lname)
x=test("darshan","solanki")
x.printname()



#Add Properties:
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019
x = Student("Mike", "Olsen")
print(x.graduationyear)

class demo:
    def __init__(self, fname, lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)
class test(demo):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.bornyear=2003
x=test("mahi","solanki")
print(x.bornyear)

class demo:
    def __init__(self, fname, lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)
class test(demo):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.dethyear=2001
x=test("rina","patel")
print(x.dethyear)


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year
x = Student("Mike", "Olsen", 2019)
print(x.graduationyear)

class demo:
    def __init__(self, fname, lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)
class test(demo):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.bornyear=year
x=test("mahi","solanki",2003)
print(x.bornyear)

class demo:
    def __init__(self, fname, lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)
class test(demo):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.dethyear=year
x=test("rina","patel",2001)
print(x.dethyear)



#Add Methods:
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year
  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
x = Student("Mike", "Olsen", 2019)
x.welcome()

class demo:
    def __init__(self, fname, lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)
class test(demo):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.bornyear=year
    def welcome(self):
        print("welcome", self.firstname, self.lastname, "to the world", self.bornyear)
x=test("bansi","patel",2003)
x.welcome()

class demo:
    def __init__(self, fname, lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)
class test(demo):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.bornyear=year
    def welcome(self):
        print("welcome",self.firstname,self.lastname, "to the world", self.bornyear)
x=test("piya","patel",2002)
x.welcome()