import math
def gcd(a,b):
    if b==0:
        return a
    else:
        #print("a,b:",a,b)
        r=a%b
        #print("r:",r)
        #print("b,r:",b,r)
        g=gcd(b,r)
        #print("g:",g)
        return g
print(gcd(140,109090))
