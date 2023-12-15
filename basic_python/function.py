#calling a function:
def my_function():
    print("hello from a function")
my_function()

def my_demo():
    print("how are you?")
my_demo()

def test():
    print("what are you doing now!")
test()


#argument
def my_function(fname):
    print((fname + " rajput"))
my_function("heena")
my_function("bansi")
my_function("krisha")

def my_demo(fname):
    print((fname + " solanki"))
my_demo("savan")
my_demo("darshan")
my_demo("sahil")

def test(fname):
    print((fname + " bhai"))
test("savan")
test("darshan")
test("margish")


#number of arguments:
def my_function(fname,lname):
    print((fname + " " + lname))
my_function("heena","rajput")

def my_demo(fname,lname):
    print((fname + " " + lname))
my_demo("darshan","rajput")

def test(id,work):
    print((id + " " + work))
test("1", "labor")


#arbitarary arguments, *args:
def my_function(*kids):
    print("the youngest child is " + kids[2])
my_function("bansi","krina","piya")

def my_demo(*color):
    print(color[2] + " color is so nice.")
my_demo("red","blue","white")

def test(*snacks):
    print(snacks[3] + " is good for health.")
test("chakli","handvo","aaloo tikki","bhakharvadi")

def this_demo(*color):
    print("light color is " + color[1])
this_demo("red","blue","green","black" )


#keyword arguments:
def my_function(child1,child2,child3):
    print("the youngest child is "+ child1)
my_function(child1="bansi", child2="kisu", child3="riya")

def my_demo(snacks1,snacks2,snacks3):
    print("the best dish is " + snacks1)
my_demo("pakoda","handvo","sev puri")

def test(sub1,sub2,sub3):
    print("highest marks in " + sub1)
test("maths","gujarati","science")

def this_demo(sub1,sub2,sub3):
    print("lowest marks in " + sub3)
this_demo("gujarati","maths","english")


#Arbitrary Keyword Arguments, **kwargs
def my_function(**kid):
    print("his last name is " + kid["lname"])
my_function(fname="darshan",lname="rajput")

def my_demo(**color):
    print("dark color is " + color["dark"])
my_demo(dark="black",light="white")

def test(**sub):
    print("easy subject is " + sub["guj"])
test(eng="english",guj="gujarati")

def this_demo(**snacks):
    print("gujarati snacks is " + snacks["guj"])
this_demo(guj="chikki",panjabi="aaloo tikki")


#default parameter value:
def my_function(country = "Norway"):
  print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

def my_demo(subject = "english"):
    print("my favorite subject is " + subject)
my_demo("maths")
my_demo("gujarati")
my_demo()
my_demo("science")
my_demo("economic")

def test(snacks="chikki"):
    print("in gujarati snacks my favorite is " + snacks)
test("sev puri")
test()
test("khaman")
test("chakli")


#Passing a List as an Argument:
def my_function(food):
  for x in food:
    print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)

def my_demo(food):
    for x in food:
        print(x)
snacks=["chakli","handvo","khaman","chikki"]
my_demo(snacks)

def test(color):
    for x in color:
        print(x)
color=["red","white","green"]
test(color)

def this_demo(kids):
    for x in kids:
        print(x)
kids=["niya","siya","riya"]
this_demo(kids)


#return values:
def my_function(x):
    return 5 * x
print(my_function(2))
print(my_function(8))
print(my_function(4))
print(my_function(7))

def my_demo(x):
    return 10 * x
print(my_demo(9))
print(my_demo(6))
print(my_demo(3))

def test(x):
    return 10 + x
print(test(20))
print(test(33))
print(test(72))

def this_demo(x):
    return 100 - x
print(this_demo(10))
print(this_demo(56))
print(this_demo(92))
print(this_demo(27))


#the pass statement:
def myfunction():
    pass

def mydemo():
    pass

def test():
    pass


#Recursion:
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result
print("\n\nRecursion Example Results\n")
tri_recursion(6)

