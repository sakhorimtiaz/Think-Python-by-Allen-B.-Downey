def uses_all(word,letters):
    for i in letters:
        if i not in word:
            return False
    return True
#print(uses_all("abcd","bc"))
with open("C:\\Users\\THINKPAD\\Downloads\\words.txt", "r") as file:
    words=[word.strip() for word in file]
    counter=0
    for word in words:
        if uses_all(word, "aeiou"):
            counter = counter + 1
    print(counter)
