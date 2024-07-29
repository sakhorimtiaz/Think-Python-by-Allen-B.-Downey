import math
def distance(x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1
    dsquare=dx**2+dy**2
    result =math.sqrt(dsquare)
    return result
def area(r):
    a=math.pi*r**2
    return a
def circle_area(xc,yc,xp,yp):
    return area(distance(xc,yc,xp,yp))
def is_between(x,y,z):
    if x<=y<=z:
        return True
    else:
        return False
def factorial(n):
    space = " " * 4 * n
    print(" " * 4 * n, "factorial", n)
    if not isinstance(n,int):
        print ("give an integer")
        return
    elif n<0:
        print("sorry, no negative values")
        return
    elif n==0:
        print(space, "returning", n)
        return 1
    else:

        recurse=factorial(n-1)
        result=n*recurse
        print(space, "returning", n)
        return result
factorial(4)
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        f=fibonacci(n - 1) + fibonacci(n - 2)
        return f
#print (fibonacci(1))
