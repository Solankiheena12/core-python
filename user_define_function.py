# How do you define a function in Python ?

# define a function using the keyword “def”. we will have to write the name of the function. 
# The function name should follow the naming rules similar to Python identifiers.
#  In case, if the functions require parameters, we will need to specify them. 
# A colon will mark the end of the function header.


def multiply_numbers(a,b):
   product = a * b
   return product

n1 = 5
n2 = 6

print("The product is", multiply_numbers(n1, n2))


# What is a function in Python ?

# Python functions are blocks of code that can perform a function. 
# It support the reusability of the code

def my_function():
  print("Hello from a function")

my_function()


# What is the function of == in Python ?

# The ‘==’ is known as the equality operator. 
# There is a minor difference between the ‘==’ operator and the Python Identity operator.
# The == operator can compare the value of two objects. 
# if you need to compare any two objects and don’t need to know where they are stored in the memory, 
# you can use the equality operator.

list1 = ['a', 'b']
list2 = list1
print(list1 == list2)




# what is an Arguments ?

# Information can be passed into functions as arguments.
# Arguments are specified after the function name, inside the parentheses. You can add as many-
# arguments as you want, just separate them with a comma.

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")



def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")


# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, add a * before
# the parameter name in the function definition.

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")


# Default Parameter Value :
# If we call the function without argument, it uses the default value:

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")



# Passing a List as an Argument :
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)






# Recursion :

# recursion is a programming technique in which a function calls itself repeatedly until a certain 
# condition is met. This allows the function to perform a task that requires repeating a similar process 
# multiple times, such as iterating over the elements of a data structure or performing a mathematical 
# operation on a sequence of numbers.

def factorial(n): 
  if n == 1: 
    return 1 
  else: 
    return n * factorial(n-1) 
 
print(factorial(5))  # Output: 120 

                # "OR"

def factorial(n): 
  if n == 1: 
    return 1 
  else: 
    return n + factorial(n-1) 
 
print(factorial(5))  # Output: 15 

# In this example, the function calls itself repeatedly, reducing the value of n by 1 each time 
# until n is equal to 1. At that point, the function returns 1, which ends the recursion and allows 
# the function to return the final result.


