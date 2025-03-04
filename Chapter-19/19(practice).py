import math
x=0
if x>0:
    y=math.log(x)
else:
    y=float("nan")
#print(y)
z=math.log(x) if x>0 else float("nan")
#print(z)
def factorial_1(n):
    if n==0:
        return 1
    else:
        return n*factorial_1(n-1)
#print(factorial_1(3))
def factorial_2(n):
    return 1 if n==0 else n*factorial_2(n-1)
#print(factorial_2(3))
class GoodKangaroo_1:
    def __init__(self,name,contents=None):
        self.name=name
        if contents==None:
            contents=[]
        self.pouch_contents=contents
class GoodKangaroo_2:
    def __init__(self,name,contents=None):
        self.name=name
        self.pouch_contents=[] if contents==None else contents
def capitalize_all_1(t):
    res=[]
    for s in t:
        res.append(s.capitalize())
    return res
#print(capitalize_all("banana"))
def capitalize_all_2(t):
    return [s.capitalize() for s in t]
#print(capitalize_all_2("orange"))
def only_upper_1(t):
    res=[]
    for s in t:
        if s.isupper():
            res.append(s)
    return res
#print(only_upper_1("BanaNa"))
def only_upper_2(t):
    return [s for s in t if s.isupper()]
#print(only_upper_2("BanaNa"))

for x in range(5):
    g=x**2
    #print(g)
#generator object, generator expression
p=(x**2 for x in range(5))
#print(p)
"""print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))#StopIteration error"""
for val in p:
    pass
    #print(val)
#print(next(p))#StopIteration error
s=sum(x**2 for x in range(5))
#print(s)
b=any([False,True,False])
#print(b)
m=any(letter=="t" for letter in "monty")
#print(m)
#print("t" in "monty")
def avoids(word, forbidden):
    return not any(letter in forbidden for letter in word)
avoids("monty",["e","t"])
def uses_all(word,required):
    return all(letter in word for letter in required)
uses_all("monty",["o","a"])
def has_duplicate_1(t):
    d={}
    for x in t:
        if x in d:
            return True
        d[x]=True
        #print(d)
    return False
has_duplicate_1("apple")

def has_duplicates_2(t):
    return len(set(t))<len(t)
has_duplicates_2("apple")

def uses_only_1(word,available):
    for letter in word:
        if letter not in available:
            return False
    return True
def uses_only_2(word,available):
    return set(word)<=set(available)
def avoids(word,unused):
    return not(set(word) & set(unused))
#print(avoids("maruf","king"))

from collections import Counter
count=Counter("parrot")

print(count)
#print(count["p"])
dic={"d":0,"m":3}
#print(dic["n"])     #error
def is_anagram(word1,word2):
    #print(Counter(word1),Counter(word2))
    return Counter(word1)==Counter(word2)
#print(is_anagram("madam","amdam"))
c1={'m': 2, 'a': 2, 'd': 1}
c2={'a': 2, 'm': 2, 'd': 1}
#print(c1==c2)
count=Counter("parrot")
for val,freq in count.most_common(2):
    print(val,freq)
from collections import defaultdict
d=defaultdict(list)
t=d["new key"]
m=d["another key"]
"""print(t)
print(m)
print(d)
print(dict(d))"""
t.append(8)
m.append("k")
#print(d)

def signature(s):
    t = list(s)
    t.sort()
    t = ''.join(t)
    return t

def all_anagrams(filename):
    d = defaultdict(list)
    for line in open(filename):
        words = line.strip().lower().split()
        for word in words:
            t = signature(word)
            d[t].append(word)
    return d
from collections import namedtuple
Point=namedtuple("Point",["x","y"])
#print(Point)
p=Point(1,2)
#print(p)
k=p.x,p.y
#print(k)

def printall(*args,**kwargs):
    print(args,kwargs)
#printall(2,3.4,"r")
d=dict(x=1,y=3)
a=Point(**d)   #unpacks key-values
b=Point(*d)    #unpacks only keys and assigns the keys as arguments
print(a)
print(b)

