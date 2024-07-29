"""a=[3,2.4]
b=[a,3,"a"]
print(a,b)
print(a[1])
print(type(a[1]))
print(type(b[2]))
print(type(b[1]))
print(type(a))
c=[34,45,45.6]
print(c)
c[1]=9
print(c)

for x in []:
    print("this never happens")
d= [2,4.5,6,89]
for i in d:
    print(i)
for i in range(len(d)):
    d[i]=d[i]*2
    print(d)

e=[5,6,7]
f=["a","b"]
print(e+f)
print(f+e)
g=f*3
print(g)
e[:1]=["s",3]
print(e)
e.append("kuku")
print(e)

t1=["a","b","c"]
t2=['d','e']
t=t1+t2
print(t)
print("t1 is: ",t1)
t1.extend(t2)
print("t1 is: ",t1)
t1.append(t2)
print("t1 is: ",t1)

s=["e","a","c","b","x"]
print(s)
s.sort()
print(s)

x=t1.extend(t2)
y=t1.append(t2)
z=s.sort()
print(x)
print(y)
print(z)"""
data=[2,3,5,8]
def add_the_numbers(data):
    total=0
    for i in data:
        total=total+i
    print (total)
    return total
#add_the_numbers(data)
#print(sum(data))
s=["e","A","C","b","x"]
#print(s)
#print("a".capitalize())
#print(s[3].capitalize())

def capitalized_all():
    s_new = []
    #print(s)
    for i in s:
        p = i.capitalize()
        s_new.append(p)
    #print(s_new)
    return s_new
#print(capitalized_all())

def only_upper():
    upper_list=[]
    for i in s:
        if i.isupper():
            upper_list.append(i)
    return upper_list
#print(only_upper())

def delete_an_element():
    del s[3]
    return s
#print(delete_an_element())

def need_the_deleted_element():
    x=s.pop(1)
    return x
#print(need_the_deleted_element())

def need_list_after_the_deleted_element():
    s.pop(1)
    return s
#print(need_list_after_the_deleted_element())
t=["a","b","C","x","d","b"]
def remove_an_element():
    p=t.remove("b")
    return p
#print(remove_an_element())

"""s='who are # you?'
print(s)
t=list(s)
print(t)

k=s.split()
print(k)

delimiter=" "
q=s.split(delimiter)
print(q)

delimiter="  "
r=s.split(delimiter)
print(r)

r=s.split(     )
print(r)

v=s.split("#")
print(v)

z=["who","are","you?"]
j=" ".join(z)
y="".join(z)
f="-".join(z)
print(f)"""

"""a="banana"
b="banana"
print(a==b) #same element
print(a is b) #same object
print()
c=[1,2,3]
d=[1,2,3]
print(c==d) #same element
print(c is d) #different object

#but
g=[3,4,5]
w=g
print(w is g)
w[0]=2
print(w) #both are changed
print(g)

a="banana"
b=a
a="Knana"
print(a)
print(b)"""

"""t1=[1,2]
t2=t1.append(3)
print(t1)
print(t2)

def tail(t):
    return t[1:]
x=tail(t1)
print(x)"""

"""t=[2,3,4,5]
x="d"
#p=t.append(x)
#print(p)
#print(t)

t=[2,3,4,5]
x=["d"]
#t=t+x
#print(t)

t=[2,3,4,5]
x="d"
t=t+[x]
print(t)"""
t=["a","b","c",'d']

t.extend(t[1])
#print(t)
evens = "abcd"[::2]
odds = "abcd"[1::2]
print(evens)
print(odds)

t=["abcdef","pqrs","hgjg","ace","bdf","pr","qs","hj"]
interlocking_words = []
for word in t:
    if len(word) % 2 == 0:
        mid = len(word) // 2
        evens = word[::2]
        odds = word[1::2]
        if evens in t and odds in t:
            interlocking_words.append(word)

print(interlocking_words)
print(len(interlocking_words))
