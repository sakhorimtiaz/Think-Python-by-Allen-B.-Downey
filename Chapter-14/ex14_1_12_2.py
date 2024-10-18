def sort_letters(arg):
    s=sorted(arg)
    return tuple(s)

def anagram_sets(book):
    with open(book, "r") as file:
        d = {}  # Dictionary to store original word and its sorted version
        for line in file:
            word = line.strip()  # Remove any leading/trailing whitespace
            w = sort_letters(word)  # Sort the letters of the word, make tuple
            # because we want to create a set of tuples, we cannot make a set of list
            if w not in d:
                d[w] = [word]  # making a dictionary for the values
            else:
                d[w].append(word)  # adding new words to the dictionary of values
        # print(d)
        # now d={tuple:list}
        # we will look for the list having more than 1 word
        sorted_d = sorted(d.values(), key=len, reverse=True)  # change in here, for question no.2
        k=[]
        for group in sorted_d:
            if len(group) > 1:
                k.append(group)
    return k

if __name__=="__main__":
    anagram_sets("C:\\Users\\THINKPAD\\Downloads\\words.txt")