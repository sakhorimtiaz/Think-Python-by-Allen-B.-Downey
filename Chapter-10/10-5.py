def is_sorted(t):
    t2=sorted(t)
    if t2==t:
        return True
    return False
print(is_sorted([1,3,4,4,9]))
print(is_sorted([1,3,4,4,2]))
print(is_sorted([1,3,4,4,9]))
