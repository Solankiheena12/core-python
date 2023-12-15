#LIST EXERCISE:

#Exercise 1:

mylist=["hello","good",10,True,26,"nice",False,20.4]
print(mylist)

mylist=[22.3,True,"neha",46,"ritu"]
print(mylist)


#Exercise 2:
list1=["neha","riya","tina"]
print(*list1)

list2=[1,4,7,5,8,9,5]
print(*list2)


#Exercise 3:
list3=["hye","hello","good","nice"]
print(len(list3))

list4=[4,5,8,2,6,9,7]
print(len(list4))


#Exercise 4:
list5=["bansi","tina","niya","riya","mahi"]
list5.reverse()
print(list5)

list6=[6,4,5,8,0,2,1]
list6.reverse()
print(list6)


#Exercise 5:
#points=[2,4,6]
#print(points)


#Exercise 6:
list1=["hye","hello","good"]
list1.remove("hye")
print(list1)

list1=[10,48,59,35,85]
list1.remove(48)
print(list1)


#Exercise 7:
list2=["riya","tina","siya","neha"]
list2.append("bansi")
print(list2)

mylist=["tanu","riya","neha"]
mylist.append("bansi")
print(mylist)


#Exercise 8:
mylist=[2,5,10,64,86,25,86,40]
for number in mylist:
    if number %5==0:
        print(number)    

list1=[47,86,10,46,30,90,55,39,50,70]
for number in list1:
    if number %10==0:
        print(number)

#Exercise 9:
mylist=[1,4,7,8,2,0,5]
mylist.sort()
print("largest element is :", max(mylist))

list1=[32,45,76,98,54,32,21,32,33]
list1.sort()
print("largest element is:,", max(list1))

#Exercise 10:
list1=["hye","hello","hye","good","hye","good","nice"]
list1=list(dict.fromkeys(list1))
print(list1)

mylist=[2,4,7,6,3,9,3,6,8,9,6]
mylist=list(dict.fromkeys(mylist))
print(mylist)







#TUPLE EXERCISE:

#Exercise 1:

mytuple=("apple","mango",10,"guava",True,32.4,"cherry",False)
print(mytuple)

tuple1=("hello","good",10,False)
print(tuple1)


#Exercise 2:

tuple1=("hello","hye","bye","good","nice")
print(*tuple1)

tuple2=("hello","guys")
print(*tuple2)


#Exercise 3:

tuple1=("hello","hye","bye","good","nice")
print(len(tuple1))


#Exercise 4:

tuple1=("apple","banana","mango","apple","mango")       #allow duplicate
print(tuple1)


#Exercise 5:

tuple1=("hello",)           #type()
print(type(tuple1))

thistuple=tuple(("bye","hye","hello"))
print(thistuple)

tuple1=("apple","banana","mango","apple","cherry","guava")
print(tuple1[2:5]) 

tuple1=("hello","hye","bye","good","nice")
if "hye" in tuple1:
    print("yes apple is in tuple1")


#Exercise 6:

tuple1=("hello","hye","bye","good","nice")
tuple2=list(tuple1)
tuple2[1]="kiwi"
tuple1=tuple(tuple2)
print(tuple1)


#Exercise 7:

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red) 

# Exercise8:

tuple1=("hello","hye","bye","good","nice")
for x in tuple1:
    print(x)


fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
for i in range(len(fruits)):
    print(fruits[i])

tuple1=("hye","hello","bye","good")
i=0
while i < len(tuple1):
    print(tuple1[i])
    i=i+1

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1







#DICT EXERCISE:

#Exercise 1:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)


#Exercise 2:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(len(thisdict))


#Exercise 3:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))


#Exercise 4:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("model")
print(x)


#Exercise 5:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change


#Exercise 6:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x) #before the change
car["year"] = 2020
print(x) #after the change


#Exercise 7:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["model"] = "swift"
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)


#Exercise 8:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)


#Exercise 9:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)


#Exercise 10:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y)

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily["child2"]["name"])
