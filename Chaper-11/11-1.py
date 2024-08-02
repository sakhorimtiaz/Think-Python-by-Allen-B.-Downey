import time
start_time=time.time()
def checking_word_in_text():
    with open("C:\\Users\\THINKPAD\\Downloads\\words.txt", "r") as file:
        d = {}
        for line in file:
            key = line.strip()
            d[key] = 1   #let all the value are 1, as it doesn't matter
        return d
        # print (d)
        # print(len(d))
d=checking_word_in_text()
print("zymology" in d)
end_time=time.time()
print("run time: ",end_time-start_time)

#lets compare with the Exercise 10-10
time_0=time.time()
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
time_1=time.time()
print("run time: ",time_1-time_0)