import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")



import re
txt = "The rain in Spain nice"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")



#findall()
import re
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

import re 
txt="hello world"
x=re.findall("ll",txt)
print(x)

import re
txt="my name is bansi, my hobby is eating."
x=re.findall("my",txt)
print(x)

import re         #no matches are found an empty list returned
txt="hello guys"
x=re.findall("hy",txt)
print(x)

import re           #if_else statement
txt="how are you"
x=re.findall("picture",txt)
print(x)
if (x):
  print("there is one last match")
else:
  print("no matches")



#the search function():
import re
txt="the rain in spain"
x=re.search("\s",txt)
print("the first white-space character is located in position:", x.start())

import re
txt="hello guys, how are you!"
x=re.search("\s", txt)
print("the first white space character is located in position:", x.start())


import re
txt="what are you doing"
x=re.search("\s", txt)
print("the first white space character is located in position:", x.start())



import re
txt = "The rain in Spain"
x = re.search("hello", txt)
print(x)

import re
txt="what are you doing"
x=re.search("are",txt)
print(x)


#the split()
import re
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

import re
txt="you can go now"
x=re.split("\s",txt,1)
print(x)

import re
txt="hello guys, how are you"
x=re.split("\s",txt,0)
print(x)

import re
txt="you can go now"
x=re.split("\s",txt,2)
print(x)



#sub() function:
import re
txt="the rain in spain"
x=re.sub("\s","9",txt)
print(x)

import re
txt="hello everyone, what are you doing"
x=re.sub("\s","*",txt)
print(x)

import re
txt="hello everyone, what are you doing"
x=re.sub("\s","*",txt,1)
print(x)



#match object:
import re
txt="the rain in spain"
x=re.search("ai",txt)
print(x)

import re
txt="hello everyone"
x=re.search("hy",txt)
print(x)


import re       #.span()
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

import re     #.string
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

import re     #.group()
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)





#Metacharacters:
import re                       #findall()
txt = "The rain in Spain"
x = re.findall("[a-m]", txt)
print(x)

import re
txt="hello world"
x=re.findall("[a-k]",txt)
print(x)


import re
txt="my name is bansi, and i have 20 dollars"
x=re.findall("\d",txt)
print(x)

import re
txt="in my pocaket now 124 dollars"
x=re.findall("\d",txt)
print(x)


import re
txt="hello everyone"
x=re.findall("ev...o.e",txt)
print(x)

import re
txt="what are you doing"
x=re.findall("w..t",txt)
print(x)


import re
txt="lets go for the tour"
x=re.findall("^lets",txt)
print(x)



