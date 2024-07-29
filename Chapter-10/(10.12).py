#preparing a list of sorted words
def length_and_sorted_list():
    with open("C:\\Users\\THINKPAD\\Downloads\\words.txt") as file:
        word_list=[]
        for word in file:
            w = word.strip()
            word_list.append(w)

        #print(word_list)
        return word_list
t=length_and_sorted_list()

import bisect
def in_bisect_cheat(t, word):
    i = bisect.bisect_left(t, word)
    if i == len(t):
        return False
    return t[i] == word

def two_way_interlock():
    interlocking_words = []
    for word in t:
        evens = word[::2]
        odds = word[1::2]
        if in_bisect_cheat(t, evens) and in_bisect_cheat(t, odds):
            interlocking_words.append(word)
    #print(interlocking_words)
    #print(len(interlocking_words))
    return interlocking_words
print(two_way_interlock())
#print(len(two_way_interlock()))
def three_way_interlock():
    interlocking_words = []
    for word in t:
        way_1 = word[0::3]
        way_2 = word[1::3]
        way_3 = word[2::3]
        if in_bisect_cheat(t, way_1) and in_bisect_cheat(t, way_2) and in_bisect_cheat(t, way_3):
            interlocking_words.append(word)
    #print(interlocking_words)
    #print(len(interlocking_words))
    return interlocking_words
print(three_way_interlock())
#print(len(three_way_interlock()))


"""#or,,, but this will take longer time to run
interlocking_words = []
for word in t:
    evens = word[::2]
    odds = word[1::2]
    if evens in t and odds in t:
        interlocking_words.append(word)

print(interlocking_words)
print(len(interlocking_words))"""