def is_abecedarian(word):
    #value=ord(word[0])
    c=0
    #print(value)
    while c<len(word)-1:
        if word[c]>word[c+1]: #we dont need to use the ord() function
            return False
        c=c+1
    return True
#print(is_abecedarian("aabde"))
with open("C:\\Users\\THINKPAD\\Downloads\\words.txt", "r") as file:
    words=[word.strip() for word in file]
    counter=0
    for word in words:
        if is_abecedarian(word):
            counter = counter + 1
    print(counter)
#or,
"""def is_abecedarian(word):
    for c in range(len(word) - 1):
        if word[c] > word[c + 1]:
            return False
    return True"""
#or,
"""def is_abecendarian(word):
    previous=word[0]
    for c in word:
        if c<previous:
            return False
        previous =c
    return True"""
