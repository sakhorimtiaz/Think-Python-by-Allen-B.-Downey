eng2sp=dict()
#print(eng2sp)
eng2sp["1"]="uno"
#print(eng2sp)
eng2sp={"one":"uno","three":"tres","two":"dos"}
#print(eng2sp["two"])
#print("uno" in eng2sp)

#page 127
"""def count_letter_occurrences(string):
    letter_count={}
    for char in string:
        if char not in letter_count:
            letter_count[char]=1
        else:
            letter_count[char]=letter_count[char]+1
    print(letter_count)
    return letter_count
h=count_letter_occurrences("Abraham, You can win.......")"""
#page 128
"""x=h.keys()
y=h.values()
m=list(h.keys())
n=list(h.values())
p=m[2]
q=n[2]
h.get("a",0)
print(x)
print(y)
print(m)
print(n)
print(p)
print(q)"""

"""print(h.get("a"))
print(h.get("a",0))
print(h.get("x"))
print(h.get("x",0))
print(h["a"])"""

def count_letter_occurrences_new_code(string):
    h = {}
    for char in string:
        h[char]=h.get(char,0)+1
    #print(h)
    return h
h=count_letter_occurrences_new_code("Abraham, You can win.......")

#page 128/129
def print_hist(h):
    for key in h:
        print(key,h[key])
#print_hist(h)

#sorted is done in the key.
def print_hist_sorted(h):
    h_new=sorted(h)
    for key in h_new:
        print(key,h[key])
#print_hist_sorted(h)

#1st approach
def reverse_lookup(h,value):
    k=list(h.keys())
    v=list(h.values())
    #print(k)
    #print(v)
    for i in range(len(h)):
        if v[i]==value:
            result=k[i]
            return result
    return None
#print(h)
#print(reverse_lookup(h,6))

#2nd approach
def reverse_lookup_new_code(h,value):
    for key in h:
        if h[key]==value:
            return key
    raise LookupError("is not in the dictionary")
#print(reverse_lookup_new_code(h,6))
print(h)
def invert_dict(h):
    inverse={}
    for key in h:
        if h[key] not in inverse:
            inverse[h[key]] = list(key)
            """h[key] is the value of the key
            inverse[h[key] means the value now becomes the key and creates a new dictionary
            then list(key) makes a list of it for further operation."""
        else:
            inverse[h[key]].append(key)
            """now, the inverse[h[key]] is the new dictionary with a list.
            do not use
            list(key).append(key)
            this is wrong, because it crates list for the current key and appends the key again."""
    print(inverse)
#invert_dict(h)

"""t=[1,2,3]
d={}
d[t]="abc"
print(d)"""

known={0:0,1:1}  # knowing, if n=0 the result is 0, when n=1, result=1
def fibonacci(n):
    if n in known:  #checking for key
        return known[n]
    res=fibonacci(n-1)+fibonacci(n-2)
    known[n]=res
    print(known)     #changes the dictionary
    return known[n]   #returns the last one
#print(fibonacci(5))

#page 133 global variable
verbose=True
def example1():
    if verbose:
        print("great")
#example1()

been_called=False   #here been_called is a global variable
def example2():
    been_called=True   #here been_called is a local variable
    print(been_called)
#example2()   #been_called is True in side the function
#print(been_called)  #been_called is false, when it is global variable

been_called=False
def example():
    global been_called  #we have called the global variable
    print(been_called)
    been_called=True  #then we have reassigned the global variable
    print(been_called)
#example()

count =0
def example3():
    global count
    count+=1
#example3()

known={0:0,1:1}
def example4():
    known[2]=3
    print(known)
#example4()

def example5():
    global known
    known =dict()
    return known
#print(example5())
#pprint
import pprint
data = {
    'name': 'Alice',
    'age': 30,
    'hobbies': ['reading', 'cycling', 'hiking'],
    'education': {
        'high_school': 'Central High',
        'university': 'State University'
    }
}
#pprint.pprint(data)
