#previous code form 6-2
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

#print(ark(3,5))

#new code for this chapter
#in Ackermann function we need two variables (m and n) to get a result.
#we can write known={}
#but for better understanding of {(m,n):result} we have written this way
known={(0,0):0}
def ackermann_memo(m,n):
    if (m,n) in known:
        return known[(m,n)]  #memory checking, not memory storing
    if m==0:
        res= n+1
    elif m>0 and n==0:
        res= ackermann_memo(m-1,1)
    else:
        res= ackermann_memo(m-1,ackermann_memo(m,n-1))
    known[(m,n)]=res     #memory store
    return known[(m,n)]
print(ackermann_memo(3,5))