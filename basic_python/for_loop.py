from subprocess import list2cmdline


fruits=["apple","banana","mango"]
for x in fruits:
    print(x)

mylist=["hye","hello","bye"]
for x in mylist:
    print(x)


for x in "banana":
    print(x)

for a in "guava":
    print(a)


fruits=["apple","banana","mango","cherry"]
for x in fruits:
    print(x)
    if x=="banana":
        break
print("thank you")

mylist=["bansi","kishu","piyu","tina"]
for x in mylist:
    print(x)
    if x=="kishu":
        break
print("thank you")

list1=["red","blue","green","black","orange"]
for x in list1:
    print(x)
    if x=="black":
        break   
print("thank you")


fruits=["apple","banana","mango","guava"]
for x in fruits:
    if x=="banana":
        break
    print(x)
print("thank you")

list1=["hye","bye","hello"]
for a in list1:
    if a=="hello":
        break
    print(a)
print("thank you")



fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x) 
print("thank you")

list1=["hye","hello","bye","good"]
for x in list1:
    if x=="bye":
        continue
    print(x)
print("thank you")




#the range function:
for x in range(6):
  print(x)
print("thank you")

for x in range(10):
    print(x)
print("thank you")

for x in range(2):
    print(x)
print("thank you")


for x in range(2,8):        #value from 2 to 8(but not including 8)
    print(x)
print("thank you")

for x in range(10,15):
    print(x)
print("thank you")


for x in range(2, 30, 3):
  print(x) 
print("thank you")

for x in range(3,20,2):
    print(x)
print("thank you")

for x in range(10,20,5):
    print(x)
print("thank you")



#else in for loop:
for x in range(6):
  print(x)
else:
  print("Finally finished!")

for x in range(8):
    print(x)
else:
    print("finally finished")

for x in range(5):
    print(x)
else:
    print("finally finished")



for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

for x in range(7):
    if x==5: break
    print(x)
else:
    print("finally finished")

for x in range(5):
    if x==3: break
    print(x)
else:
    print("finally finished")




#nested loop:
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)

key=["name","city"]
value=["bansi","rajkot"]
for x in key:
    for y in value:
        print(x,y)

adj=["red","yellow","tasty"]
fruits=["apple","banana","cherry"]
for x in adj:
    for y in fruits:
        print(x,y)



#the pass statement:
for x in [0,1,2]:
    pass

for x in [0,10,20]:
    pass

