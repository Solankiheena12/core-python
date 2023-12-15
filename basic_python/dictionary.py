
thisdict =	{"brand": "Ford","model": "Mustang","year": 1964}
for x in thisdict:
  print(x)

mydict={"name":"heena","city":"rajkot","state":"guj"}
for x in mydict:
  print(x)


mydict={"one":1,"two":2,"three":3,"four":4}
for x in mydict:
  print(mydict[x])

dict1={"name":"bansi","city":"rajkot","state":"guj"}
for x in dict1:
  print(dict1[x])


thisdict =	{"brand": "Ford","model":"Mustang","year": 1964}    #value()
for x in thisdict.values():
  print(x)

dict1={"one":1,"two":2,"three":3}
for x in dict1.values():
  print(x)

dict2={"name":"kisu","city":"rajkot"}
for x in dict2.values():
  print(x)


thisdict =	{"brand": "Ford","model": "Mustang","year": 1964}       #keys()
for x in thisdict.keys():
  print(x)

dict1={"one":1,"three":3}
for x in dict1.keys():
  print(x)


thisdict =	{"brand": "Ford","model": "Mustang","year": 1964}     #items()
for x,y in thisdict.items():
  print(x,y)

dict1={"one":1,"two":2,"three":3}
for x,y in dict1.items():
  print(x,y)


#copy dictionaries:
thisdict = {"brand": "Ford","model": "Mustang","year": 1964}      #copy()
mydict = thisdict.copy()
print(mydict)

x={"name":"bansi","city":"rajkot"}
y=x.copy()
print(y)

mydict={"red":"blue","black":"white"}
newdict=mydict.copy()
print(newdict)

x={"name":"bansi","city":"rajkot"}        #dict()
y=dict(x)
print(y)





#nested dictionary:
myfamily = {
  "child1" : { "name" : "Emil","year" : 2004},
  "child2" : { "name" : "Tobias","year" : 2007 },
  "child3" : { "name" : "Linus","year" : 2011 }
}
print(myfamily)

family={
  "child1":{"name":"darshan","year":2012},
  "child2":{"name":"savan","year":2004}
}
print(family)


child1 = {"name" : "bansi","year" : 2004}
child2 = {"name" : "krisha","year" : 2007}
child3 = {"name" : "tina","year" : 2011}
myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)

child1={"name":"savan","city":"rajkot"}
child2={"name":"darshan","city":"rajkot"}
family={
  "child1":child1,
  "child2":child2
}
print(family)


myfamily = {
  "child1" : {"name" : "Emil","year" : 2004},
  "child2" : {"name" : "Tobias","year" : 2007},
  "child3" : {"name" : "Linus","year" : 2011}
}
print(myfamily["child2"]["name"])

family={
  "child1":{"name":"krisha","age":20},
  "child2":{"name":"piya","age":19}
}
print(family["child2"]["age"])

family1={
  "child1":{"name":"maya","age":20},
  "child2":{"name":"riya","age":19},
  "child3":{"name":"tiya","age":15}
}
print(family1["child2"]["name"])




#dictionary methods:
car =	{                       #remove()-->remove all element from the dict.
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()
print(car)

color={
  "red":"blue",
  "green":"yellow",
  "black":"white"
}
color.clear()
print(color)

car = {                       #copy()
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.copy()
print(x)

member={
  "name":"sahil",
  "age":20,
  "city":"rajkot"
}
x=member.copy()
print(member)

x = ('key1', 'key2', 'key3')    #fromkeys()
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)

mydict={"key1","key2","key3"}
newdict=dict.fromkeys(x,y)
print(mydict)


x = ('key1', 'key2', 'key3')    
thisdict = dict.fromkeys(x)
print(thisdict)

mydict=("heena","savan","darshan")
newdict=dict.fromkeys(mydict)
print(mydict)

car = {                                     #get()
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.get("model")
print(x)

family={
  "member1":"maya",
  "member2":"riya",
  "member3":"siya"
}
x=family.get("member2")
print(x)

family={
  "child1":"kisu",
  "child2":"piyu",
  "child3":"muskan"
}
x=family.get("child3")
print(x)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.get("price", 15000)
print(x)

family={
  "name":"heena",
  "age":20,
  "city":"rajkot"
}
x=family.get("mobile",123)
print(x)

fontstyle={
  "font1":"italic",
  "font2":"bold",
  "font3":"underline"
}
x=fontstyle.get("font3","big")
print(x)


car = {                       #items()
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.items()
car["year"] = 2018
print(x)

family={
  "name":"heena",
  "city":"rajkot",
  "mobile":2123123123
}
x=family.items()
family["name"]="neha"
print(x)

car = {                     #keys()
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.keys()
print(x)

family={
  "member1":"siya",
  "member2":"riya",
  "member3":"tina"
}
x=family.keys()
print(x)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.keys()
car["color"] = "white"
print(x)

family={
  "member1":"siya",
  "member2":"riya",
  "member3":"tina"
}
x=family.keys()
family["member4"]="mina"
print(x)

family={                            #pop()
  "member1":"siya",
  "member2":"riya",
  "member3":"tina"
}
family.pop("member2")
print(family)

fontstyle={
  "font1":"italic",
  "font2":"bold",
  "font3":"underline"
}
x=fontstyle.pop("font1")
print(x)

Number={
  1:"one",
  2:"two",
  3:"three"
}
x=Number.pop(2)
print(x)


car = {                          #popitem()-->remove the last item from the dictionay.
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.popitem()
print(car)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.popitem()
print(x)

fontstyle={
  "font1":"italic",
  "font2":"bold",
  "font3":"underline"
}
x=fontstyle.popitem()
print(x)

car = {                                  #setdefault()
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.setdefault("model", "Bronco")
print(x)

fontstyle={
  "font1":"italic",
  "font2":"bold",
  "font3":"underline"
}
x=fontstyle.setdefault("font1","small")
print(x)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.setdefault("color", "White")
print(x)

fontstyle={
  "font1":"italic",
  "font2":"bold",
  "font3":"underline"
}
x=fontstyle.setdefault("font4","big")
print(x)

car = {                             #update()
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.update({"color": "White"})
print(car)

fontstyle={
  "font1":"italic",
  "font2":"bold",
  "font3":"underline"
}
fontstyle.update({"font4":"big"})
print(fontstyle)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.values()
print(x)

fontstyle={
  "font1":"italic",
  "font2":"bold",
  "font3":"underline"
}
x=fontstyle.values()
print(x)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.values()
car["year"] = 2018
print(x)

family={
  "name":"heena",
  "city":"rajkot",
  "mobile":2123123123
}
x=family.values()
family["mobile"]=4545858562
print(family)