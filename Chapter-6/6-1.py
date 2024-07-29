def b(z):
    prod=a(z,z)
    print(z,prod)
    return prod
def a(x,y):
    x=x+1
    return x*y
def c(x,y,z):
    total = x+y+z #4x+5
    square = b(total)**2
    return square
x=1
y=x+1
print (c(x,y+3,x+y)) #equation = x+y+3+x+y=4x+5
