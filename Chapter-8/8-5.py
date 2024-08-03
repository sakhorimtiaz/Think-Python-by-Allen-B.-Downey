#my code
def rotate_word(word,n):
    new_word = ""
    k = ""
    for i in word:
        if i.islower():
            if (ord(i) + n) <= 112:
                k = chr((ord(i) + n))
            else:
                k = chr((ord(i) + n - 112 + 96))
        elif i.isupper():
            if (ord(i) + n) <= 90:
                k = chr((ord(i) + n))
            else:
                k = chr((ord(i) + n - 90 + 64))
        else:
            k = i
        new_word = new_word + k
    print(new_word)

#original code (given by the author)
def rotate_letter(letter, n):
    """Rotates a letter by n places. Does not change other chars.

    letter: single-letter string
    n: int

    Returns: single-letter string
    """
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        return letter

    c = ord(letter) - start
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


if __name__ == '__main__':
    print(rotate_word('cheer', 7))
    print(rotate_word('melon', -10))
    print(rotate_word('sleep', 9))
    print(rotate_word("I love U, Dua", 3))
