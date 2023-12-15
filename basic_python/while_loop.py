i = 1
while i < 6:
  print(i)
  i += 1
print("thank you")

i=5
while i<=10:
    print(i)
    i+=1
print("thank you")

i=0
while i < 3:
    print(i)
    i+=1
print("thank you")

i=10
while i>0:
    print(i)
    i-=1
print("thank you")





#the break statement:
i = 1
while i < 6:
  print(i)
  if (i == 3):
    break
  i += 1
print("thank you")

i=1
while i<6:
  print(i)
  if (i==4):
    break
  i+=1
print("thank you")

i=5
while i<10:
  print(i)
  if(i==8):
    break
  i+=1
print("thank you")

i=20
while i < 100:
  print(i)
  if (i==35):
    break
  i+=1
print("thank you")





#the continue statement:
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
print("thank you")

i=10
while i<17:
  i+=1
  if i==13:
    continue
  print(i)
print("thank you")

i=5
while i < 15:
  i+=1
  if i==10:
    continue
  print(i)
print("thank you")

i=1
while i<10:
  i+=1
  if i==9:
    continue
  print(i)
print("thank you")

i=10
while i<1:
  i-=10
  if i==5:
    continue
  print(i)
print("thank you")




#else statement:
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

i=0
while i < 10:
  print(i)
  i+=1
else:
  print("i is no longer than ten")

i=3
while i < 9:
  print(i)
  i+=1
else:
  print("i is n onger than nine")

i=1
while i<10:
  print(i)
  i+=1
else:
  print("i is no longer than 10")