#ex:1                   #seed()
import random

random.seed(10)
print(random.random())

#ex:2
import random

random.seed(10)
print(random.random())

random.seed(10)
print(random.random())




#ex:1                   #getstate()
import random

x = random.getstate()

print(x)




#ex:1                      #setstate()
import random

#print a random number:
print(random.random())

#capture the state:
state = random.getstate()

#print another random number:
print(random.random())

#restore the state:
random.setstate(state)

#and the next random number should be the same as when you captured the state:
print(random.random())





#ex:1                       #getrandbits()
import random

print(random.getrandbits(8))




#ex:1                       #randrange()
import random

print(random.randrange(3, 9))




#ex:1                       #randint()
import random

print(random.randint(3, 9))



#ex:1                        #choices()
import random

mylist = ["apple", "banana", "cherry"]

print(random.choices(mylist, weights = [10, 1, 1], k = 14))




#ex:1                           #shuffle()
import random

mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist)

print(mylist)




#ex:1                           #sample()
import random

mylist = ["apple", "banana", "cherry"]

print(random.sample(mylist, k=2))




#ex:1                       #random()
import random

print(random.random())





#ex:1                          #uniform()
import random

print(random.uniform(20, 60))




#ex:1                       #triangular()
import random

print(random.triangular(20, 60, 30))
