import math
a = int(input("a=\n"))
b = int(input("b=\n"))
c = int(input("c=\n"))
n = int(input("n=\n"))
def check_fermat(a,b,c,n):
    if n>2 and (a**n)+(b**n)==(c**n):
        print("Holy smokes, Fermat was wrong!")
    elif (a**n)+(b**n)==(c**n):
        print("Heh heh")
    else:
        print("No, that doesn't work")
check_fermat(a,b,c,n)
