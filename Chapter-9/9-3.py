#word=input("give a word: ")
#letters=input("write a string of letters without space or comma: ")
"""def avoid(word, letters):
    flag=True
    for i in letters:
        flag=flag and (i not in word)
    return flag"""
def avoid(word, letters):
    for i in letters:
        if i in word:
            return False
    return True
#print(avoid ("attendance","bx"))
#words that doesn't contain any of the given forbidden letter
"""with open("C:\\Users\\THINKPAD\\Downloads\\words.txt","r") as file:
    counter=0
    for word in file:
        word = word.strip() #removs unwnated newline character
        # print(avoid(word,letters))
        flag=avoid(word,letters)
        if flag==True:
            counter=counter+1
    print(counter)"""

#combination of letters
from itertools import combinations
import string
alphabet = string.ascii_lowercase
comb=list(combinations(alphabet,2))

min_count=float("inf")
best_combination=None

with open("C:\\Users\\THINKPAD\\Downloads\\words.txt","r") as file:
    words = list(word.strip() for word in file) #lists all words
    for letters in comb:
        counter = 0
        for word in words:
            if avoid(word, letters):
                counter = counter + 1 #checks all the alphabets of a every combination for one word
        if counter<min_count:
            min_count=counter #creates the number of words which does not contain the alphabets from the combination set
                              #if the number is minimum then it prints
            best_combination=letters
            #print(min_count)
    print(min_count)
    print(best_combination)
