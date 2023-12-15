#remove duplicate from a list:
mylist = ["a", "b", "a", "c", "c"]
mylist = list(dict.fromkeys(mylist))
print(mylist)

mylist = ["hello", "hye", "hello", "good", "hello", "hye"]
mylist = list(dict.fromkeys(mylist))
print(mylist)




#create a function:
def my_function(x):
  return list(dict.fromkeys(x))

mylist = my_function(["a", "b", "a", "c", "c"])

print(mylist)


def my_function(x):
    return list(dict.fromkeys(x))

mylist = my_function(["hye", "hello", "hye", "good", "hello"])

print(mylist)