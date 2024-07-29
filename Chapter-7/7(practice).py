
x=5
#print("x:",x)
y=x
x=2
#print("x:",x)
#print("y:",y)

def countdown(n):
    while n>0:
        print(n)
        n=n-1
    print("Blastoff")
#countdown(10)

def sequence(n):
    while n!=0:
        print(n)
        if n%2==0:
            n=n//2
        else:
            n=n*3+1
#sequence(-34)
#sequence (-10)
#sequence (-2)
#sequence (10)

#code from page 52
def print_n(s,n):
    if n<=0:
        return
    print(s)
    print_n(s,n-1)
#print_n(5,3)
#code with iteration
def print_n(s,n):
    while n>0:
        print(s)
        n=n-1
print_n(5,3)
while True:
    line = input("Do you love me?>")
    if line=="yes"or line=="Yes" or line=="YES":
        break
    #print (line)
print("Lets get married......")

#with recursion
def square_root(a,x):
    y=0.5*(x+a/x)
    if abs(y-x)<0.0000001:  #we could write y==x, but for more accuracy abs(y-x)<0.0000001 has written
        print (y)
    else:
        return square_root(a,y)
#square_root(3620,600)
#with iteration
def square_root(a):
    x=a/2 #guess a value
    while True:
        y = 0.5 * (x + a / x)
        if y == x:
            break
        x = y
    print(y)
#square_root(5)
