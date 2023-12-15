class MyClass:
  x = 5
print(MyClass)

class myclass:
    x=2
print(myclass)



#create an object:
class MyClass:                
  x = 5
p1 = MyClass()
print(p1.x)

class myclass:
    x=10
obj=myclass()
print(obj.x)

class mydemo:
    x=874
obj1=mydemo()
print(obj1.x)

class test:
    x=64
obj1=test()
print(obj1.x)



#The __init__() Function:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("John", 36)
print(p1.name)
print(p1.age)

class test:
    def __init__(self, name, age):
        self.name=name
        self.age=age
p1=test("bansi", 20)
print(p1.name)
print(p1.age)

class mydemo:
    def __init__(self, name, age, city):
        self.name=name
        self.age=age
        self.city=city
obj=mydemo("kishu", 20, "rajkot")
print(obj.name)
print(obj.age)
print(obj.city)



#The __str__() Function
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __str__(self):
    return f"{self.name}({self.age})"    
p1 = Person("John", 36)
print(p1)

class test:
    def __init__(self, roll, name):
        self.roll=roll
        self.name=name
    def __str__(self):
        return f"{self.roll}({self.name})"
p1=test(1,"bansi")
print(p1)

class mydemo:
    def __init__(self, name, city):
        self.name=name
        self.city=city
    def __str__(self):
        return f"{self.name}({self.city})"
p1=mydemo("shivi","rajkot")
print(p1)


#object methods'
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("bansi", 36)
p1.myfunc()

class test:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def myfunc(self):
        print("hye i am "+ self.name)
p1=test("maahi",20)
p1.myfunc()
        
class mydemo:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def myfunc(self):
        print("my name is "+ self.name)
        print("my age is "+ self.age)
p1=mydemo("riya","29")
p1.myfunc()

class test:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def myfunc(self):
        print("my name is "+ self.name)
p1=test("niya",24)
p1.myfunc()        



#The self Parameter:
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age
  def myfunc(abc):
    print("Hello my name is " + abc.name)
p1 = Person("John", 36)
p1.myfunc()

class test:
    def __init__(mysillyobj, name, age):
        mysillyobj.name=name
        mysillyobj.age=age
    def myfunc(abc):
        print("hello, my name is "+ abc.name)
p1=test("bansi",20)
p1.myfunc()
    
class mydemo:
    def __init__(sillyobject, name, age) -> None:
        sillyobject.name=name
        sillyobject.age=age
    def myfunc(abc):
        print("hye, my name is "+ abc.name)
p1=mydemo("tina",20)
p1.myfunc()


#modify object properties:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
p1.age = 40
print(p1.age)

class myclass:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def myfunc(abc):
        print("hello, my name is "+ abc.name)
p1=myclass("bansi",20)
p1.age=22        
print(p1.age)

class test:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def myfunc(abc):
        print("my name is "+ abc.self)
p1=test("riya",20)
p1.age
print(p1.age)



#delete object:         del keyword
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
del p1

class test:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def myfunc(self):
        print("hello, my name is " + self.name)
p1=test("bansi",20)
del p1
        


#the pass statement:
class Person:
  pass

class test:
    pass

class mydemo:
    pass
