def read_dictionary(filename='c06d'):
    """Reads from a file and builds a dictionary that maps from
    each word to a string that describes its primary pronunciation.

    Secondary pronunciations are added to the dictionary with
    a number, in parentheses, at the end of the key, so the
    key for the second pronunciation of "abdominal" is "abdominal(2)".

    filename: string
    returns: map from string to pronunciation
    """
    d = {}
    with open ("C:\\Users\\THINKPAD\\Downloads\\cmudict-0.7b", "r") as file:
        for line in file:

            # skip over the comments
            if line[0] == '#':
                continue

            t = line.split()
            word = t[0].lower()
            pron = ' '.join(t[1:])
            d[word] = pron

        return d
d = read_dictionary()

"""if __name__ == '__main__':
    d = read_dictionary()
    for (k, v) in d.items():
        print(k, v)"""

def checking_word_in_text():
    with open("C:\\Users\\THINKPAD\\Downloads\\words.txt", "r") as file:
        d = {}
        for line in file:
            key = line.strip()
            d[key] = 1   #let all the value are 1, as it doesn't matter
        return d
w=checking_word_in_text()

def words_in_CMU():
    #checks if the word is in the CMU
    #creates a new COM dictionary with the words given in word file
    n = {}
    for key in w:
        if key in d:
            res = d[key]
            n[key] = res
        elif len(key)>2:
            modified_key_1=key[1:]
            modified_key_2=key[0]+key[2:]
            if modified_key_1 in d:
                res = d[modified_key_1]
                n[modified_key_1] = res
            elif modified_key_2 in d:
                res = d[modified_key_2]
                n[modified_key_2] = res
    return n
#h=modified dictionary of words to pronunciation
h=words_in_CMU()
def homophones():
    final = set()
    for k in h:
        if k[1:] in h and h[k] == h[k[1:]]:
            if k[0] + k[2:] in h and h[k] == h[k[0] + k[2:]]:
                final.add((k,k[1:], k[0] + k[2:], h[k]))
    return final

print(homophones())
print(len(homophones()))
#the more the dictionary is enriched, the more words will be found