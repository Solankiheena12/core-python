#local scope:
def myfunc():
    x=300
    print(x)
myfunc()

def demo():
    x=89274
    print(x)
demo()

def test():
    x="what are you doing.."
    print(x)
test()


#function inside function:
def myfunc():
    x=300
    def myinnerfunc():
        print(x)
    myinnerfunc()
myfunc()

def mydemo():
    x=102
    def myinnerdemo():
        print(x)
    myinnerdemo()
mydemo()


#global scope:
x=300
def myfunc():
    print(x)
myfunc()
print(x)

x=10
def mydemo():
    print(x)
mydemo()
print(x)

x=100
def test():
    print(x)
test()
print(x)

x=654
def myfun():
    print(x)
myfun()
print(x)


#naming variables:
x=222
def myfunc():
    x=333
    print(x)
myfunc()
print(x)

x=125
def mydemo():
    x=345
    print(x)
mydemo()
print(x)

x=473
def test():
    x=635
    print(x)
test()
print(x)


#global keyword:
def myfunc():
    global x
    x=200
myfunc()
print(x)
    
def demo():
    global x
    x=100
demo()
print(x)

def test():
    global x
    x=856
test()
print(x)


#change the value of a global variable inside a function
x=300
def myfunc():
    global x
    x=200
myfunc()
print(x)

x=400
def demo():
    global x
    x=100
demo()
print(x)

x=230
def mydemo():
    global x
    x=125
mydemo()
print(x)