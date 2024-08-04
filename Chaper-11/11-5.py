def checking_word_in_text():
    with open("C:\\Users\\THINKPAD\\Downloads\\words.txt", "r") as file:
        d = {}
        for line in file:
            key = line.strip().lower()   #making lower case
            d[key] = 1   #let all the value are 1, as it doesn't matter
        return d
d=checking_word_in_text()
def rotate_letter(letter,n):
    start=ord("a")
    c = ord(letter) - start   # no character, or are in the file
    i = (c + n) % 26 + start
    return chr(i)

def rotate_word(word, n):
    """Rotates a word by n places.

    word: string
    n: integer

    Returns: string
    """
    res = ''
    for letter in word:
        res += rotate_letter(letter, n)
    return res

def rotate_pairs():
    t=set()  #using set to avoid repetation
    for key in d:
        for i in range(1,14): #checking 1-14, as rotation 1 is equivalent to rotation 26, and 2 is equivalent to 25...
            rotated=rotate_word(key, i)
            if rotated in d:
                t.add((key,i, rotated)) #add for set add.
    print(len(t))
    return t
print(rotate_pairs())