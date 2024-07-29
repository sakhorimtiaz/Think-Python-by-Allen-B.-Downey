#1st part
def uses_only(word,letters):
    for i in word:
        if i not in letters:
            return False
    return True
#print(uses_only("apple","pelas"))

#2nd part sentence : "A chef of a cafe"
