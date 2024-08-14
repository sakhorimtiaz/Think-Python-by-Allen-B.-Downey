with open("C:\\Users\\THINKPAD\\Downloads\\emma.txt","r",encoding='utf-8') as file:
    #encoding = 'utf-8' is used for other languages, like French, German, even Bnagla
    arg=file.read()

def cleaned_string(arg):
    h=[]
    #considering only letters
    for char in arg:
        if char.isalpha():
            #converting all the leeters into lowercase
            char=char.lower()
            #creating a new list
            h.append(char)
    #print(h)
    return h
c=cleaned_string(arg)

def letter_count(t):
    d = {}
    for e in t:
        if e not in d:
            d[e] = 1
        else:
            d[e] += 1
    #print(d)
    #print(len(d))
    return d
r=letter_count(c)
def sort_by_descending_frequency(r):
    k=r.keys() #alphabets
    v=r.values() #letter count
    z=zip(v,k)
    res=list(z)
    s=sorted(res,reverse=True) #reverse sorted
    #print(res)
    return s
print(sort_by_descending_frequency(r))