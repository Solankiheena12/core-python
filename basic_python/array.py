#
cars = ["Ford", "Volvo", "BMW"]
print(cars)

cars=["ford","volvo","bmw"]
print(cars)

color=["red","blue","white"]        #access the element of array:
print(color[0])

list1=["hye","bye","good"]
print(list1[1])

cars = ["Ford", "Volvo", "BMW"]
cars[0] = "Toyota"
print(cars)

color=["yello","black","white"]
color[0]="red"
print(color)


#the length of an array:
cars=["ford","volvo","bmw"]
x=len(cars)
print(x)

color=["red","blue","green","black"]
x=len(color)
print(x)


#looping array element:
cars = ["Ford", "Volvo", "BMW"]
for x in cars:
    print(x)

color=["yello","black","white"]
for x in color:
    print(x)


#adding array elements:
cars = ["Ford", "Volvo", "BMW"]   #append()      
cars.append("Honda")
print(cars)

color=["red","blue","green"]
color.append("white")
print(color)

#remove array element:
cars = ["Ford", "Volvo", "BMW"]         #pop()
cars.pop(1)
print(cars)

color=["red","green","blue"]
color.pop(0)
print(color)

cars = ["Ford", "Volvo", "BMW"]         #remove()
cars.remove("Volvo")
print(cars)

color=["red","blue","green"]
color.remove("green")
print(color)



#methods of array:
a = ["apple", "banana", "cherry"]       #add list to a list--> append()
b = ["Ford", "BMW", "Volvo"]
a.append(b)
print(a)

cars = ["Ford", "Volvo", "BMW"]      
color=["red","blue","green"]
cars.append(color)
print(cars)

fruits = ["apple", "banana", "cherry"]      #clear()
fruits.clear()
print(fruits)

color=["red","blue","green"]
color.clear()
print(color)

fruits = ["apple", "banana", "cherry"]      #copy()
x = fruits.copy()
print(x)

color=["red","blue","green"]
x=color.copy()
print(x)

fruits = ["apple", "banana", "cherry"]      #count()
x = fruits.count("cherry")
print(x)

fruits = ["apple", "banana", "cherry","apple","guava","apple"]
x = fruits.count("apple")
print(x)

color=["red","blue","green","blue","white"]
x=color.count("blue")
print(x)

points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = points.count(9)
print(x)

fruits = ['apple', 'banana', 'cherry']      #extend()
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)

cars=["ford","volvo","BMW"]
color=["red","blue","green"]
cars.extend(color)
print(cars)

color=["red","blue","green"]
points=[1,4,3,9,6,8]
color.extend(points)
print(color)

fruits = ['apple', 'banana', 'cherry']      #index()
x = fruits.index("cherry")
print(x)

color=["red","blue","green","guava"]
x=color.index("guava")
print(x)

points=[3,6,4,1,9,7,5]
x=points.index(1)
print(x)

fruits = [4, 55, 64, 32, 16, 32, 76 ,95]
x = fruits.index(95)
print(x)

fruits = ['apple', 'banana', 'cherry']      #insert()
fruits.insert(1, "orange")
print(fruits)

color=["red","blue","green"]
color.insert(3, "white")
print(color)

points=[3,5,4,8,6,9,1,7]
points.insert(3, 2)
print(points)

fruits = ['apple', 'banana', 'cherry']      #pop()
fruits.pop(1)
print(fruits)

color=["red","green","blue"]
color.pop(2)
print(color)

fruits = ['apple', 'banana', 'cherry']      #Return the removed element:
x = fruits.pop(1)
print(x)

color=["red","green","blue","white"]
x=color.pop()
print(x)

cars=["ford","volvo","BMW"]
x=cars.pop(0)
print(x)

fruits = ['apple', 'banana', 'cherry']      #reverse()
fruits.reverse()
print(fruits)

color=["red","blue","green","white"]
color.reverse()
print(color)



#sort()
cars = ['Ford', 'BMW', 'Volvo']     
cars.sort()
print(cars)

color=["red","blue","green","white"]
color.sort()
print(color)

cars = ['Ford', 'BMW', 'Volvo']     #Sort the list descending:
cars.sort(reverse=True)
print(cars)

color=["red","blue","green","white"]
color.sort(reverse=True)
print(color)

# A function that returns the length of the value:
def myFunc(e):
  return len(e)
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(key=myFunc)
print(cars)

def mydemo(e):
    return len(e)
color=["red","green","blue","white"]
color.sort(key=mydemo)
print(color)

def test(e):
    return len(e)
fruits=["apple","banana","cherry","mango"]
fruits.sort(key=test)
print(fruits)

def myFunc(e):              
  return e['year']
cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]
cars.sort(key=myFunc)
print(cars)

def mydemo(e):
    return e['number']
fruits=[
    {'number': 2,'fruits':'apple'},
    {'number': 1,'fruits':'banana'},
    {'number': 3,'fruits':'mango'}
]
fruits.sort(key=mydemo)
print(fruits)

def test(e):
    return e['points']
color=[
    {'points': 4,'color':'red'},
    {'points': 2,'color':'blue'},
    {'points': 1,'color':'green'},
    {'points': 3,'color':'white'}
]
color.sort(key=test)
print(color)

#Sort the list by the length of the values and reversed:
def myFunc(e):
  return len(e)
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(reverse=True, key=myFunc)
print(cars)

def mydemo(e):
    return len(e)
color=["red","blue","green","pink","purpal"]
color.sort(reverse=True, key=mydemo)
print(color)

def test(e):
    return len(e)
color=["red","blue","green","pink","purpal"]
color.sort(reverse=True, key=test)
print(color)

