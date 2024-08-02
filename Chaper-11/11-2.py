def count_letter_occurrences_new_code(string):
    h = {}
    for char in string:
        h[char]=h.get(char,0)+1
    #print(h)
    return h
h=count_letter_occurrences_new_code("Abraham, You can win.......")
print(h)
def invert_dict(h):
    d = {}
    for key in h:
        t=[]
        val = h[key]
        p=d.setdefault(val,t)
        p.append(key)  # Ensure the key exists with an empty list if it doesn't, then append
    return d
print(invert_dict(h))
