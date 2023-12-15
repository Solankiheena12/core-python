x = lambda a : a + 10
print(x(3))

x=lambda b:b +10
print(x(2))

x=lambda a,b : a*b
print(x(5,6))

x=lambda a,b,c:a+b+c
print(x(4,8,2))


def myfunc(n):
    return lambda a:a*n
mydoubler=myfunc(2)
print(mydoubler(11))

def mydemo(n):
    return lambda a:a*n
mydoubler=mydemo(2)
print(mydoubler(10))

def test(n):
    return lambda a:a*n
mydoubler=test(2)
print(mydoubler(15))


def myfunc(n):
  return lambda a : a * n
mytripler = myfunc(3)
print(mytripler(11))

def mydemo(n):
    return lambda a:a*n
mytripler=mydemo(3)
print(mytripler(15))

def test(n):
    return lambda a:a*n
mytripler=test(3)
print(mytripler(25))


def myfunc(n):
    return lambda a:a*n
mydoubler=myfunc(2)
mytripler=myfunc(3)
print(mydoubler(20))
print(mytripler(33))