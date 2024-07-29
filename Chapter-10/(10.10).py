def attempt1():
    with open("C:\\Users\\THINKPAD\\Downloads\\words.txt") as file:
        x = []
        for i in file:
            p = i.strip()
            x.append(p)
        # print(x)
        return x
t=sorted(attempt1())

def in_bisect(t,word):
    if len(t)==0:
        return None
    d = len(t) // 2
    # print(t[d])
    if t[d] == word:
        print("matched: ",word)
        return True
    elif t[d] < word:
        d = d + 1
        t = t[d:]
        a=in_bisect(t, word)
        return a
        #print("second half")
    else:
        t = t[:d]
        b=in_bisect(t, word)
        return b
        #print("first half")
#print(in_bisect(t,"quickly"))

for i in ['aa', 'alien', 'allen', 'zymurgy']:
    in_bisect(t,i)