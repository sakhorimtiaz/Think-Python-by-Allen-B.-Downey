def has_no_e(word):
    for letter in word:
        if letter=="e":
            return False
    return True
#print(has_no_e("rosse"))

with open("C:\\Users\\THINKPAD\\Downloads\\words.txt", "r") as file:
    total_words=0
    words_without_e=0
    for line in file:
        total_words=total_words+1   #counts the total number of the words
        for letter in line:
            if letter=="e":
                break
        else:
            words_without_e=words_without_e+1   #counts the total number of words free from "e"
            #print(line.strip())   #without this line.strip() there will be a line gap in the output after every line
            #print(counter)
    print(words_without_e)
    print(total_words)
def percentage(total_words,words_without_e):
    p=(words_without_e/total_words)*100
    print(p,"%")
percentage(total_words,words_without_e)
#or to find the words without "e"
"""with open("C:\\Users\\THINKPAD\\Downloads\\words.txt", "r") as file:
    counter=0
    for line in file:
        if 'e' not in line:
            counter=counter+1
            print(line.strip())
            print(counter)"""

#total word count
"""with open("C:\\Users\\THINKPAD\\Downloads\\words.txt", "r") as file:
    line_count = 0
    for line in file:
        line_count=line_count+1
    print(line_count)"""
