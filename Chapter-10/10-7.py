def has_duplicate(t):
    t2=sorted(t)
    #print(t)
    for j in range(len(t)-1):
        if t2[j] == t2[j + 1]:
            return True
    return False

print(has_duplicate([5,1,2,3,5]))
