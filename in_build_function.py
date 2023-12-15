# Built-in Functions :

# Type Conversion Functions:
# int(): Converts a number or a string to an integer.

num_str = "123"
num_int = int(num_str)
print(num_int)

x = "10"
y = int(x)
print(y)

a = "25"
b = int(a)
print(b)

# float(): Converts a number or a string to a floating-point number.

num_int = 42
num_float = float(num_int)
print(num_float)

x = 25
y = float(x)
print(y)

# str(): Converts an object to a string.

num_int = 123
num_str = str(num_int)
print(num_str)

x = 12
y = str(x)
print(y)

x = 00
y = str(x)
print(y)

# list : Converts into list

tuple_values = (1, 2, 3)
list_values = list(tuple_values)
print(list_values)

x = ("hello", "hye", "bye")
y = list(x)
print(y)

# tuple : Converts into tuple

list_values = [1, 2, 3]
tuple_values = tuple(list_values)
print(tuple_values)

x = ["hello", "hye", "bye"]
y = tuple(x)
print(y)

# set : Converts into set

list_values = [1, 2, 2, 3]
set_values = set(list_values)
print(set_values)

x = ["hello", "hye", "bye"]
y = set(x)
print(y)

x = ("hello", "hye", "bye")
y = set(x)
print(y)

# bool : Converts into bool
# bool() function considers any non-zero numeric value as True, and the value 0 (zero) as False.

value = 42
bool_value = bool(value)
print(bool_value)

a = 10
b = bool(a)
print(b)

p = 0
q = bool(p)
print(q)

# dict : Converts into dict

x = dict([(1, "one"), (2, "two")])
print(x)

a = [(1, "one"), ("name", "heena")]
b = dict(a)
print(b)

p = [("name", "heena"), ("age", 20), ("city", "rajkot")]
q = dict(p)
print(p)

# chr : Converts an integer i to a Unicode character.

i = 65
x = chr(i)
print(f"this is 65's unicode character :", x)

a = 26
b = chr(a)
print(f"this is 26's unicode character :", b)

p = 22
q = chr(p)
print(f"this is 22's unicode character :", q)

m = 97
n = chr(m)
print(f"this is 97's unicode character :", n)

# ord : Converts a Unicode character c to its integer Unicode code.

x = ord("A")
print(f"this is unicode character A's integer unicode:", x)

a = "^"
b = ord(a)
print(f"this is unicode character ^'s integer unicode:", b)

x = "#"
y = ord(x)
print(f"this is unicode character #'s integer unicode:", y)

p = "~"
q = ord(p)
print(f"this is unicode character ~'s integer unicode:", q)

m = "&"
n = ord(m)
print(f"this is unicode character &'s integer unicode:", n)


# Mathematical Functions :

# abs() :
# The abs() function in Python is a built-in function that returns the absolute value of a number.
# In other words, it returns the non-negative value of a numeric expression.

num1 = -10
num2 = +7.5

absolute_value_num1 = abs(num1)
absolute_value_num2 = abs(num2)

print(f"absolute value of {num1} is {absolute_value_num1}")
print(f"absolute value of {num2} is {absolute_value_num2}")


x = -10
y = abs(x)
print(f"absolute value is :", y)

a = -5555
b = abs(a)
print(f"absolute value is :", b)

p = -24.75
q = abs(p)
print(f"absolute value is :", q)


# max() :
words = ["apple", "banana", "orange", "grape"]
max_word = max(words, key=len)

print("Longest word:", max_word)


a = ["hello", "hye", "bye", "nice"]
b = max(a, key=list)
print("Longest Word :", b)

# min() :
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
smallest_number = min(numbers)
print(smallest_number)

list = ["hello", "hye", "nice", "thanks"]
list1 = min(list)
print(list1)

list = ["hello", "hye", "nice", "thanks"]
list1 = min(list, key=len)
print(list1)

list = ["hello", "bye", "nice", "thanks"]
list1 = min(list_values)
print(list1)


# pow() :
# Example 1: Calculate 2 to the power of 3
result1 = pow(2, 3)
print("power is:", result1)  # Output: 8   (2*2*2)

# Example 2: Calculate 3 to the power of 4 with modulus 5
result2 = pow(3, 4, 5)
print("power is:", result2)  # Output: 1 (because 3^4 % 5 is 1)   (3*3*3*3=81, 81 % 5)

a = pow(5, 2)
print("power of a is:", a)

b = pow(6, 5)
print("power of b is:", b)

stu = pow(20, 3, 5)
print("power of stu is:", stu)


# round() :
# Example 1: Round to the nearest integer
result = round(5.67)
print("nearest integer is:", result)  # Output: 6

# Example 2: Round to a specified number of decimal places
result = round(3.1415926535, 2)
print("nearest integer is:", result)  # Output: 3.14

# Example 3: If n digits is not specified, it rounds to the nearest integer
result = round(9.876)
print("result nearest integer is:", result)  # Output: 10

stu = round(10.62)
print("stu nearest integer is:", stu)

abc = round(23.924789, 3)
print("abc nearest integer is:", abc)

result = round(0.5)
print("result nearest integer is:", result)  # Output: 0


# String Manipulation :


# len() :
# The len() function in Python is a built-in function that is used to determine the length (the number of items)
# of an object.

string_var = "Hello, World!"
length_of_string = len(string_var)
print("length of the string:", length_of_string)

my_range = range(5)
length_of_range = len(my_range)
print("length of range(5) is:", length_of_range)

my_dict = {"a": 1, "b": 2, "c": 3}
length_of_dict = len(my_dict)
print("length of my_dict is:", length_of_dict)  # Output: 3 (number of key-value pairs)

my_set = {1, 2, 3, 4, 5}
length_of_set = len(my_set)
print("length of my_set is:", length_of_set)

my_tuple = (10, 20, 30, 40, 50)
length_of_tuple = len(my_tuple)
print("length of my_tuple is:", length_of_tuple)

my_list = [1, 2, 3, 4, 5]
length_of_list = len(my_list)
print("length of my_list is:", length_of_list)


# str() :
# the str() function is used to convert an object into a string.
# It returns a string representation of the specified object.

num = 42
str_num = str(num)

print("Original Number:", num)
print("String Representation:", str_num)


a = 1223
b = str(a)

print("Original Number:", a)
print("String Representation:", b)


test = 684
demo = str(test)

print("Original Number:", test)
print("String Representation:", demo)


my_list = [1, 2, 3, 4, 5]
str_list = str(my_list)

print("Original List:", my_list)
print("String Representation:", str_list)


my_tuple = (10, 20, 30)
str_tuple = str(my_tuple)

print("Original Tuple:", my_tuple)
print("String Representation:", str_tuple)


my_dict = {"a": 1, "b": 2}
str_dict = str(my_dict)

print("Original Dictionary:", my_dict)
print("String Representation:", str_dict)


# format() :
# The format() function in Python is used for formatting strings.
# It allows you to create dynamic strings by replacing placeholders with values.
name = "John"
age = 30

message = "My name is {}, and I am {} years old.".format(name, age)
print(message)

message = "My name is {0}, and I am {1} years old. {0} is my first name.".format(name, age)
print(message)

message = "My name is {name}, and I am {age} years old.".format(name="Alice", age=25)
print(message)


pi = 3.141592653589793
formatted_pi = "The value of pi is approximately {:.2f}".format(pi)
print(formatted_pi)





# ord() :

