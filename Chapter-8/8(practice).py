"""fruit = "banana"
index=0
while index<len (fruit):
    letter = fruit [index]
    print(letter)
    index=index+1"""

"""page87
prefixes= "JKLMNOPQ"
suffix= "ack"

for i in prefixes:
    if i=="O" or i=="Q":
        print (i+"u"+suffix)
    else:
        print (i+suffix)"""

#page 89
def find(word, letter):
    index=0
    while index<len(word):
        if word[index]==letter:
            return index
        index=index+1
    return "not found"
#print(find ("bananaf","n"))
def counter(word,letter):
    count=0
    for i in word:
        if i==letter:
            count=count+1
    return count
#print (counter("banana","n"))
#page 90
def find_and_count(word, letter, return_count):
    first_occurrence = find(word, letter)
    if return_count:
        count = counter(word, letter)
        return first_occurrence, count
    else:
        return first_occurrence

#print(find_and_count("banana", "n", True))

def find_multiple_letters(word, letters):
    positions={}
    for i in letters:
        index = 0
        while index<len(word):
            if word[index]==i:
                if i not in positions:
                    positions[i]=[]
                positions[i].append(index)
            index=index+1
    #print (positions)
    return positions
#print(find_multiple_letters("banana","bkan"))
word = "banana"
new_word= word.upper()
index= word.find("a",0,1)
def in_both(word1,word2):
    for i in word1:
        if i in word2:
            print(i)
#in_both("mAruf","Miraj")
def checking(word):
    if word=="banana":
        print ("matched")
    elif word<"banana":
        print ("your word " + word+ " comes before banana")
    else:
        print("your word " + word + " comes after banana")
#checking ("banana")
#checking ("banaoa")
#checking ("banama")
#checking ("banaNa")
#checking ("banaOa")
#checking ("banaMa")

def is_reverse(word1, word2):
    if len(word1)!=len(word2):
        return False

    i=0
    j=len(word2)-1
    while j>=0:
        if word1[i]!=word2[j]:
            return False
        i=i+1
        j=j-1
    return True
#print (is_reverse("nayan","nayan"))
