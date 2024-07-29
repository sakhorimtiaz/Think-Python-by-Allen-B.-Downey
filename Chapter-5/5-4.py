def resource(n,s):
    if n==0:
        return
    else :
        print("love", n)
        resource(n-1,n+s)
        print(n, s)
        resource(n - 1, n + s)
        print("lost",n)
resource (3,10)
