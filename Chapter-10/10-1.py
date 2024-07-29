def nested_sum(t):
    a=0
    for i in t:
        for j in i:
            sum(i)
        a=a+sum(i)
    print(a)
    return a

nested_sum([[1,3,6],[10],[],[4,6]])
