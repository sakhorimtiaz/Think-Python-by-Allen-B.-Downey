import bisect
def word_list():
    with open("C:\\Users\\THINKPAD\\Downloads\\words.txt") as file:
        x = []
        for i in file:
            p = i.strip()
            x.append(p)
        return x

t = sorted(word_list())
def in_bisect_cheat(t, word):
    """Checks whether a word is in a list using bisection search.

    Precondition: the words in the list are sorted

    word_list: list of strings
    word: string
    """
    i = bisect.bisect_left(t, word)
    if i == len(t):
        return False
    return t[i] == word

"""want to avoid counting the word itself as its reverse pair, 
and you aim to ensure that only different words form reverse pairs."""
result = []

for i, word in enumerate(t):  # position=i, and word both are counted
    reverse_word = word[::-1]
    if in_bisect_cheat(t[i + 1:], reverse_word):
        result.append(word)
print(len(result))
# print (reverse_check("maruf","furm"))