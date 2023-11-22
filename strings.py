# # Get the character at position 1 :

# a = "Hello, World!"
# print(a[1])

# #Looping Through a String:

# for x in "banana":
#   print(x)

# #String Length:

# a = "Hello, World!"
# print(len(a))

# #Check String:

# txt = "The best things in life are free!"
# print("free" in txt)


# # Slicing Strings :

# b = "Hello, World!"
# print(b[2:5])

# b = "Hello, World!"
# print(b[:5])

# b = "Hello, World!"
# print(b[2:])

# b = "Hello, World!"
# print(b[-5:-2])


# Modify Strings :

a = "hello world"
print(a.upper())

a = "HELLO GUYS"
print(a.lower())

a = " hello  world  "
print(a.strip())

a = "hello world"
print(a.replace("h", "j"))

a = "hello, guys"
print(a.split(","))


# String Concatenation :

a = "hello"
b = "guys"
c = a + b
print(c)

a = "hello"
b = "guys"
c = a + " " + b
print(c)


# Format - Strings :

age = 20
txt = 'my age is {}'
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))