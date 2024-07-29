def ark(m,n):
    if not (isinstance(m,int) and isinstance(n,int)):
        print ("give an integer")
    elif m<0 or n<0:
        print("negative values are not excepted")
    elif m==0:
        return n+1
    elif m>0 and n==0:
        return ark(m-1,1)
    else:
        return ark(m-1,ark(m,n-1))

print(ark(3,5))
