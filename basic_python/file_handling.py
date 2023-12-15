
f=open("link.txt","r")
print(f.read())

f=open("link.txt","r")
print(f.read(5))

f=open("link.txt","r")
print(f.readline())
print(f.readline())
print(f.readline())

f=open("link.txt","r")
for x in f:
    print(x)

f=open("link.txt","r")
print(f.readline())
f.close()


f = open("link.txt", "a")
f.write("Now the file has more content!")
f.close()
f = open("link.txt", "r")
print(f.read())


f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()
f = open("demofile3.txt", "r")
print(f.read())

f=open("hello.txt","w")
f=open("myfile.py","a")

import os
os.remove("hello.txt")

import os
os.remove("demofile2.txt")


import os
if os.path.exists("hello.txt"):
    os.remove("hello.txt")
else:
    print("the file does not exists")


