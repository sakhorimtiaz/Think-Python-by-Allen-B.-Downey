#tuples are immutable, list are mutable, so we can use tuple when we get a unchangble values
#11/2 will give a specific result.
#slicing a string can be different
"""s="Maruf"
a=set(s)
b=list(s)
c=tuple(s)"""
#print(a)
#print(b)
#print(c)
"""t="a"
print(t)
print(type(t))
t1="a",
print(t1)
print(type(t1))
t2="a","b",
print(t2)
print(type(t2))
t3=("a",)
print(t3)
print(type(t3))
t4=("a")
print(t4)
print(type(t4))"""
#t=()
#print(type(t))
"""t=("maruf",)
print(t)
print(type(t))
t6=tuple("maruf")
print(t6)
print(type(t6))"""
"""t = ("a", "b", "c")
t = t + ("d",)  # Adding a new element "d" to the tuple
print(t)
t1=("a","b","d","e","f")
t1=t1[:2]+("c",)+t[2:]
print(t1)
print(type(t1[2])) # string
print(type(t1[2:])) #tuple
t2=("a","c","d","e","f")
t2=t2[:1]+("b",)+t2[1:] #using tuple-tuple concatenation 
print(t2)"""
#lexicographical, meaning compares only the 1st element, if equal the moves to the 2nd
#if it finds any differnec it prints True or False and shows the result.
#a=(1,2,4)<(0,3,4)
#print(a)
"""temp=a
a=b
b=temp
print(b)"""
"""addr="kt@python.org"
k=uname,domain=addr.split("@")
print(k)
addrr="kt@python.org"
m=usname,dmain=addrr.split("@") #list
print(tuple(m))
print(type(k))
print(type(m))"""
"""t=quot,rem=divmod(11,3) #tuple
print(type(t))
print(t)
def min_max(t):
    return min(t), max(t)
print(min_max([2,4,5,1,0,-1,7]))
print(type(min_max([2,4,5,1,0,-1,7])))#tuple"""
"""def printall(*arg):
    print (arg)
#printall(2,3.4,"a")
print(type((2,2.4)))"""
"""print(divmod(7,3))
d=(3,2)
print(divmod(d)) # wrong"""
"""#page 143
def sumall(*args):
    return sum(args)
print(sumall(2,3,4,5))"""
"""
#zip
s="abcd"
t={0:"a",1:"b",2:"c",3:"d"}
print(type(t))
#print(zip(s,t))
for pair in zip(s,t):
    print(pair) #sting to key mapping
    print(type(pair))"""
"""
#page144
t1=[1,2,3,4]
t2=[0,2,4,6]
def has_match(t1,t2):
    for a,b in zip(t1,t2):
        if a==b:
            return True
    return False
print(has_match(t1,t2))"""
"""d={}
for index,element in enumerate("abc"):
    d[index]=element
    #print(index,element)
    #a=element,index
    #print(type(a))
print(d)"""
"""d={0:"a",1:"b",2:"c",3:"d"}
t=d.items()
print(t)
print(type(t))
for key,value in d.items():
    print(key,value)"""
"""t=[("a",0),("b",1),("c",2)]
d=dict(t)
print(d)"""
"""zip(range(3),"abc")
d=dict(zip(range(3),"abc"))
print(d)"""

"""#iterator..page 143
t=[1,2,3,4]
my_iterator=iter(t)
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))  #done
print(next(my_iterator))  #error"""
"""dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4,'d':5}
dict1.update(dict2)
print(dict1)
dict1= {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4,'d':5}
dict2.update(dict1)
print(dict2)"""
"""directory={}
directory[("Smith","John")]=555599999
directory["Dua","Lipa"]=555500009
print(directory)
for last,first in directory:
    a=last,first,directory[last,first]
    print(a)
    print (last,first,directory[last,first])"""
"""#once a tuple is created, its elements cannot be changed. 
# However, the sorted() function doesn't modify the original tuple; 
# instead, it returns a new sorted list based on the elements of the tuple.
t=(1,2,3,0)
n=sorted(t)
print(t)
print(n)"""
