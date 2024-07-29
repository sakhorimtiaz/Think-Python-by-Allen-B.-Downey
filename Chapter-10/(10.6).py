def anagram(word1,word2):
    x=list(word1)
    y=list(word2)

    if sorted(x)==sorted(y):
        return True
    return False
print(anagram("patla","palta"))