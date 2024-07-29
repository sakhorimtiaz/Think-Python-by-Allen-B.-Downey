def three_consecutive_double(word):
    i=0
    while i<len(word) -1:
        if word[i]==word[i+1] and (i+5)<len(word):
            a=i+2
            while a<len(word)-1:
                if word[a] == word[a + 1] and (a + 3) < len(word):
                    b=a+2
                    while b<len(word)-1:
                        if word[b]==word[b+1] and (b+1)<len(word):
                            return 1
                        b=b+1
                a=a+1
        i=i+1
    return 0
#print(three_consecutive_double("ccddee"))

def checking_three_consecutive_double_in_doc():
    with open("C:\\Users\\THINKPAD\\Downloads\\words.txt", "r") as file:
        words = [word.strip() for word in file]
        count=0
        for i in words:
            if three_consecutive_double(i):
                count=count+1
        print(count)
checking_three_consecutive_double_in_doc()
