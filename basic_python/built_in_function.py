# abs()
x = abs(-8346)
print(x)

x = abs(3+5j)
print(x)

x = abs(9+2j)
print(x)

x = abs(3+4j)
print(x)



# all()
mylist = ["hye", True, True]
x = all(mylist)
print(x)

mylist = [0, True, "bansi"]
x = all(mylist)
print(x)

mytuple = ("hello", "hye", "bye", "good")
x = all(mytuple)
print(x)

mytuple = ("hye", False, 0, True)
x = all(mytuple)
print(x)

myset = {0, 1, 0}
x = all(myset)
print(x)

mydict = {0:"apple", 1:"mango"}     #When used on a dictionary, the all() function checks if all the keys are true, not the values.
x = all(mydict)
print(x)




# any()
mylist = [False, True, False]       #The any() function returns True if any item in an iterable are true, otherwise it returns False.
x = any(mylist)
print(x)

mytuple = (0, 1, False)
x = any(mytuple)
print(x)

myset = {0, 1, 0}
x = any(myset)
print(x)

mydict = {0:"one", 1:"two"}
x = any(mydict)
print(x)



# ascii()
x = ascii("my name is stela")
print(x)

x = ascii("My name is Ståle")
print(x)




# bin()
x = bin(36)     #return binary version of number
print(x)

x = bin(20)
print(x)



# bool()
x = bool(1)     #return boolean value 
print(x)

x = bool(00)
print(x)

x = bool(False)
print(x)



# bytearray()
x = bytearray(4)
print(x)

x = bytearray(3)
print(x)

x = bytearray(7)
print(x)



# bytes()
x = bytes(4)
print(x)



# callable()
def x():
    a = 10
print(callable(x))

x = 1
print(callable(x))




# chr()
x = chr(97)
print(x)

x = chr(74)
print(x)

x = chr(33)
print(x)



# ord()
x = ord("b")
print(x)

x=ord("k")
print(x)



# compile()
x = compile('print(55)', 'test', 'eval')
exec(x)

x = compile('print(10)\nprint(90)', 'test', 'exec')
exec(x)




# complex()
x = complex(3, 5)
print(x)

x = complex(9, 6)
print(x)

x = complex('3+5j')
print(x)




# delattr()
class Person:
  name = "John"     # The Person object will no longer contain an "age" property
  age = 36
  country = "Norway"

delattr(Person, 'age')




# dict()
x = dict(name = "John", age = 36, country = "Norway")

print(x)




# dir()
class Person:       #The dir() function returns all properties and methods of the specified object, without the values.
  name = "John"
  age = 36
  country = "Norway"

print(dir(Person))




# divmod()         return argument1 divide by argument2:
x = divmod(5, 2)
print(x)




# enumerate()
x = ("apple", "mango", "cherry")
y = enumerate(x)
print(tuple(y))

x = ["hye", "bye", "good", "nice"]
y = enumerate(x)
print(tuple(y))



# eval()
x = 'print(64)'
eval(x)

x = 'print("bansi")'
eval(x)




# exec()
x = 'name = "john"\nprint(name)'
exec(x)

x = 'name = "bansi"\nprint(name)'
exec(x)



# filter()
ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True
adults = filter(myFunc, ages)
for x in adults:
  print(x)


#float()
x = float("3.500")
print(x)



#format()
x = format(255, 'x')
print(x)



#frozenset()
mylist = ['apple', 'banana', 'cherry']
x = frozenset(mylist)
print(x)



#getattr()
class Person:
  name = "John"
  age = 36
  country = "Norway"
x = getattr(Person, 'age')
print(x)

class Person:
  name = "John"
  age = 36
  country = "Norway"
x = getattr(Person, 'page', 'my message')
print(x)



#globals()
x = globals()
print(x)

x = globals()
print(x["__file__"])



#hasattr()
class Person:
  name = "John"
  age = 36
  country = "Norway"
x = hasattr(Person, 'age')
print(x)



#hex()
x = hex(255)
print(x)



#id()
x = ('apple', 'banana', 'cherry')
y = id(x)
print(y)


#input()
# print("Enter your name:")
# x = input()
# print("Hello, " + x)

# x = input("Enter your name:")
# print(x)

# x = input("Enter your name:")
# print("Hello, " + x)



#int()
x = int("12")
print(x)



#isinstance()
x = isinstance(5, int)
print(x)

x = isinstance("Hello", (str, float, int, str, list, dict, tuple))
print(x)

class myObj:
  name = "John"
y = myObj()
x = isinstance(y, myObj)
print(x)



#issubclass()
class myAge:
  age = 36
class myObj(myAge):
  name = "John"
  age = myAge
x = issubclass(myObj, myAge)
print(x)


#iter()
x = iter(["apple", "banana", "cherry"])
print(next(x))
print(next(x))
print(next(x))



#locals()
x = locals()
print(x)

x = locals()
print(x["__file__"])



#max()
x = max(5, 10)
print(x)

x = max("Mike", "John", "Vicky")
print(x)

a = (1, 5, 3, 9)
x = max(a)
print(x)


#min()
x = min(5, 10)
print(x)

x = min("ike", "John", "Vicky")
print(x)

a = (1, 5, 3, 9)
x = min(a)
print(x)



#next()
mylist = iter(["apple", "banana", "cherry"])
x = next(mylist)
print(x)
x = next(mylist)
print(x)
x = next(mylist)
print(x)

mylist = iter(["apple", "banana", "cherry"])
x = next(mylist, "orange")
print(x)
x = next(mylist, "orange")
print(x)
x = next(mylist, "orange")
print(x)
x = next(mylist, "orange")
print(x)




#object()
x = object()
print(dir(x))




#open()
f = open("db.txt", "r")
print(f.read())



#print()
print("Hello World")

print("Hello", "how are you?")

x = ("apple", "banana", "cherry")
print(x)

print("Hello", "how are you?", sep="---")




#reversed()
alph = ["a", "b", "c", "d"]
ralph = reversed(alph)
for x in ralph:
  print(x)



#round()
x = round(5.76543,1)    #second parameter is count of how many decimal count in integer
print(x)

x = round(5.7)    #return nearest value of integer
print(x)




#setattr()
class Person:
  name = "John"
  age = 36
  country = "Norway"

setattr(Person, 'age', 40)
x = getattr(Person, 'age')
print(x)



#slice()
a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(2)
print(a[x])

a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(3, 5)
print(a[x])

a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(0, 8, 3)
print(a[x])



#sorted()
a = ("b", "g", "a", "d", "f", "c", "h", "e")    #assending order
x = sorted(a)
print(x)



#sum()
a = (1, 2, 3, 4, 5)
x = sum(a)
print(x)

a = (1, 2, 3, 4, 5)
x = sum(a, 7)
print(x)



#vars()
class Person:
  name = "John"
  age = 36
  country = "norway"
x = vars(Person)
print(x)



#zip()
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")
x = zip(a, b)
print(tuple(x))

a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")
x = zip(a, b)
print(tuple(x))
