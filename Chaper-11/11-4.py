#prevoius code (10-7)
def has_duplicate(t):
    t2=sorted(t)
    #print(t)
    for j in range(len(t)-1):
        if t2[j] == t2[j + 1]:
            return True
    return False
#print(has_duplicate([5,1,2,3,5]))

#solution with dictionary
def has_duplicate_dict(t):
    d={}
    for i in t:
        if i in d:
            return True
        d.setdefault(i, 1)
#print(has_duplicate_dict([5,1,2,5,3]))

#solution with set
#t=[5,1,2,5,3]
#print(set(t))
def has_duplicate_set(t):
    """set(t)
    len(set(t))
    len(t)"""
    return len(set(t))<len(t)
print(has_duplicate_set([5,1,2,5,3]))
