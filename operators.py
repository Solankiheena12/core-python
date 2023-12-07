# # Arithmetical Operator:

# Addition    +
# Subtraction     -
# Multiplication  *
# Division    /
# Modulus     %
# Exponentiation  **
# Floor Division  //

# # Addition :
# a = 10
# b = 20
# c = a + b
# print(c)

# x = 10.5
# y = 11.3
# z = x + y
# print(z)


# # Subtraction :
# a = 10
# b = 5
# c = a - b
# print(c)

# x = 20.35
# y = 1.9
# z = x - y
# print(z)


# # Multiplication :
# a = 10
# b = 5
# c = a * b
# print(c)

# x = 10.5
# y = 11.3
# z = x * y
# print(z)


# # Division :
# a = 10
# b = 5
# c = a / b
# print(c)

# x = 150
# y = 10
# z = x / y
# print(z)

# # Modulus :
# a = 225              
# b = 20
# c = a % b
# print(c)

# x = 150
# y = 9
# z = x % y
# print(z)

# # Exponentiation :
# a = 10
# b = 5
# c = a ** b
# print(c)

# x = 4
# y = 4
# z = x ** y
# print(z)

# a = 2
# b = 12
# c = a ** b
# print(c)

# # Floor division :
# a = 10
# b = 5
# c = a // b
# print(c)

# x = 150
# y = 10
# z = x // y
# print(z)

# x = 104
# y = 10
# z = x // y
# print(z)








# # Assignment Operators :

# Assignment    =
# Addition assignment   +=
# Subtraction assignment    -=
# Multiplication assignment     *=
# Division assignment   /=
# Modulus assignment    %=
# Exponentiation assignment     **=
# Floor Division assignment     //=

# # equal-to operator or Assignment operator :
# x = 3
# print(x)

# y = 10
# print(y)

# # plus equal-to operator or Addition assignment :
# x = 10
# x += 3
# print(x)

# y = 25
# y += 20
# print(y)

# # Subtraction assignment :
# x = 22
# x -= 2
# print(x)

# y = 10
# y -= 5
# print(y)

# # Multiplication assignment :
# x = 22
# x *= 2
# print(x)

# y = 10
# y *= 5
# print(y)

# # Division assignment :
# x = 22
# x /= 2
# print(x)

# y = 10
# y /= 5
# print(y)

# # Modulus assignment :
# x = 22
# x %= 2
# print(x)

# y = 10
# y %= 5
# print(y)

# z = 24
# z %= 5
# print(z)

# # Exponentiation assignment :
# x = 22
# x **= 2
# print(x)

# y = 10
# y **= 5
# print(y)

# # Floor Division assignment :
# x = 22
# x //= 2
# print(x)

# y = 10
# y //= 5
# print(y)

# # bitwise operator :
# y = 10
# y &= 5
# print(y)

# y = 5
# y &= 5
# print(y)

# y = 10
# y |= 5
# print(y)

# y = 10
# y ^= 5
# print(y)

# y = 10
# y >>= 5
# print(y)

# y = 10
# y <<= 5
# print(y)

# x = 5
# y = 3
# x &= y  
# print(x)







# # Comparison Operations :

# Equal to      ==
# Not equal to      != or <>
# Greater than      >
# Less than         <
# Greater than or equal to      >=
# Less than or equal to         <=

# # Equal :
# x = 10
# y = 14
# c = x == y
# print(c)

# a = 5
# b = 5
# print(a == b)

# # Not equal	:
# x = 10
# y = 11
# print(x != y)

# a = 5
# b = 5
# print(a != b)

# # Greater than :
# x = 10
# y = 11
# print(x > y)

# a = 5
# b = 5
# print(a > b)

# x = 109
# y > 11
# print(x > y)

# # Less than	:
# x = 10
# y = 11
# print(x < y)

# x = 109
# y = 11
# print(x < y)

# # Greater than or equal to :
# x = 109
# y = 11
# print(x >= y)

# x = 10
# y = 11
# print(x >= y)

# p = 4
# q = 4
# print(p >= q)

# # Less than or equal to	:
# x = 109
# y = 11
# print(x <= y)

# x = 10
# y = 11
# print(x <= y)

# p = 4
# q = 4
# print(p <= q)






# # Logical Operators :

# AND and
# OR or
# NOT not

# # "AND" or "and" Operator :
# # Returns True if both statements are true
# x = 5
# print(x > 3 and x < 10)     #true

# y = 10
# print(y < 20 and y > 2)     #true

# y = 10
# print(y < 20 and y > 20)    #false

# y = 10
# print(y < 2 and y > 20)     #false

# # "OR" or "or" Operator :
# # Returns True if one of the statements is true
# x = 5
# print(x > 3 or x < 4)

# x = 20
# print(x > 3 or x > 22)

# y = 10
# print(y < 20 and y > 20)    

# # "NOT" or "not" Operators :
# # Reverse the result, returns False if the result is true
# x = 5
# print(not(x > 3 and x < 10))

# x = 22
# print(not(x < 2 and x > 23))






# # Identity Operators :

# is 
# is not 

# # is Operator :
# # Returns true if both variables are the same object :
# x = ["apple", "banana"]
# y = ["apple", "banana"]
# z = x

# print(x is z)         #true
# print(x is y)         #false
# print(x == y)         #true


# # is not Operator :
# # Returns true if both variables are not the same object
# a = 25
# b = 25
# c = 20

# print(a is b)
# print(a is c)
# print(b is not c)
# print(a is not b)
# print(c is not b)





# # Membership Operators :

# in 
# not in

# # in Operator :
# # checks if a value exists in a sequence :
# x = ["apple", "banana"]
# print("banana" in x)

# x = ["apple", "banana"]
# if "banana" in x:   
#     print("banana")

# a = {"meera", "niya", "tina"}
# if "tina" in a:
#     print("tina in this tuple")
# else:
#     pass


# # not in Operator :
# # checks if a value does not exist in a sequence :
# x = ["apple", "banana"]
# print("pineapple" not in x)

# x = ["apple", "banana"]
# if "mango" not in x:
#     print("mango is not in list")

y = {"riya", "niya", "mina"}
if "siya" not in y:
    print("siya is not in tuple")
else:
    print("siya is in this tuple")






# Bitwise Operators :

# Bitwise AND   &
# Bitwise OR    |
# Bitwise XOR   ^
# Bitwise NOT   ~
# Left shift    <<
# Right shift   >>

