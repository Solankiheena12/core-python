# thisset = {"apple", "banana", "cherry", "apple"}
# print(thisset)

# thisset = {"apple", "banana", "cherry", True, 1, 2}
# print(thisset)

# myset = {"apple", "banana", "cherry"}
# print(type(myset))


# # The set() Constructor :
# thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
# print(thisset)

# #Access Items:
# thisset = {"apple", "banana", "cherry"}
# for x in thisset:
#   print(x)

# thisset = {"apple", "banana", "cherry"}
# thisset.add("orange")
# print(thisset)

# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}
# thisset.update(tropical)
# print(thisset)

# #Remove Item:
# thisset = {"apple", "banana", "cherry"}
# thisset.remove("banana")
# print(thisset)

# #Remove a random item by using the pop() method:
# thisset = {"apple", "banana", "cherry"}
# x = thisset.pop()
# print(x)
# print(thisset)

# #The clear() method empties the set:
# thisset = {"apple", "banana", "cherry"}
# thisset.clear()
# print(thisset)

# thisset = {"apple", "banana", "cherry"}
# del thisset
# print(thisset)


# # loop:
# thisset = {"apple", "banana", "cherry"}
# for x in thisset:
#   print(x)


# join:
# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}
# set3 = set1.union(set2)
# print(set3)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)