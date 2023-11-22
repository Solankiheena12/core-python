# List Length:

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# A list can contain different data types:

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]
print(list1)
print(list2)
print(list3)
print(list4)


# List Type() :
mylist = ["apple", "banana", "cherry"]
print(type(mylist))


# The list() Constructor :
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)


# Access List Items :

thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#Negative Indexing:
# Negative indexing means start from the end,  -1 refers to the last item, -2 refers to the second last item etc.
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# Check if Item Exists:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")


# Change Item Value

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)




# Add List Items :

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)


# Extend List :

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


# Remove Specified Item :

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# Remove Specified Index :

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# del keyword can also delete the list completely.:

thislist = ["apple", "banana", "cherry"]
del thislist

# Clear the List :

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


# Loop Through a List :

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])


# Using while loop :

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#  Sort List Accending:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#  Sort List Descending:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)


# Copy List :
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)


# Join Two Lists :

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)

