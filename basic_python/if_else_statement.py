a = 33
b = 200
if b > a:
    print("b gretar than a")


a = 200
b = 33
if b > a:
  print("b is greater than a")


#if the previous conditions were not true, then try this condition--> if_elif
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

a = 200                              #short hand if
b = 33
if a > b: print("a is greater than b")

a=25
b=70
if a>b: print("a is greate than b")

x=74
y=84
if x<y: print("x is lessthan y")

a = 2                       #short hand if...else
b = 330
print("A") if a > b else print("B")

a=20
b=90
print("A") if a<b else print("B")

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

a=221
b=221
print("A") if a < b else print("=") if a == b else print("B")




#logical and:
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

a=67
b=89
c=10
if b>a and c<a:
    print("both condition are true")





#logical or:
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

a=10
b=20
c=30
if c>b or a>b:
    print("one condition is true")





#logical not:
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

a=50
b=90
if not a>b:
    print("a is not greater than b")




#nested if:
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

x=50
if x < 60:
    print("above fiften")
    if x > 30:
        print("under fiften")
    else:
        print("not above fiften")



#the pass statement:
a = 33
b = 200
if b > a:
  pass

