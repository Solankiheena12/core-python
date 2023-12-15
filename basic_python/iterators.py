mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))

mytuple=("bansi","riya","siya")
myit=iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))

tuple1=("hye","hello","good")
myit=iter(tuple1)
print(next(myit))
print(next(myit))
print(next(myit))

mystr = "banana"
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

test="mango"
myit=iter(test)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))



#looping through iterator:
mytuple=("apple","banana","cherry")
for x in mytuple:
    print(x)

mytuple=("mango","guava","chiku")
for x in mytuple:
    print(x)

mystr=("banana")
for x in mystr:
    print(x)

mystr=("chiku")
for x in mystr:
    print(x)



#create an iterator:
class mynumbers:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        x=self.a
        self.a += 1
        return x
myclass=mynumbers()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

class demo:
    def __iter__(self):
        self.a=10
        return self
    def __next__(self):
        x=self.a
        self.a += 1
        return x
myclass=demo()
myiter=iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))


print("hello, guys")

#stopiteration:
class mynumbers:
    def __iter__(self):
        self.a=10
        return self
    def __next__(self):
        if self.a <=20:
            x=self.a
            self.a += 1
            return x
        else:
            raise StopIteration
myclass=mynumbers()
myiter=iter(myclass)
for x in myiter:
    print(x)

class demo:
    def __iter__(self):
        self.a=89
        return self
    def __next__(self):
        if self.a <=94:
            x=self.a
            self.a += 1
            return x
        else:
            raise StopIteration
myclass=demo()
myiter=iter(myclass)
for x in myiter:
    print(x)