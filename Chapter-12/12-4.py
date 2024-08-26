"""could not solve the problem and ended up writing a long code considering n=21
then changed n, reduced to 11 to get the longest word"""
with open("C:\\Users\\THINKPAD\\Downloads\\words.txt", "r") as file:
    d = {}  # Dictionary to store original word and its sorted version
    for line in file:
        word = line.strip()
        if len(word) not in d:
            d[len(word)]=[word]
        else:
            d[len(word)].append(word)
    #adding base case letters to the dictionary
    for letter in ["a","i"]:
        d[len(letter)]=letter
def reducible(new_word, n):
    possible_words = []  # List to store all possible words after removing one letter
    if new_word in d[n]:
        for i in range(len(new_word)):
            # Generate next level word by removing one more letter
            new_word_2 = new_word[:i] + new_word[i + 1:]
            if new_word_2 in d[n - 1]:  # Check if the new word is in the dictionary
                possible_words.append(new_word_2)
    return possible_words

# Loop through dictionary to find words at key 3
s = set()
n = 11  # Starting length of words

for target_word in d[n]:
    new_words = reducible(target_word, n)  # Get all possible next-level words

    for new_word in new_words:
        new_words_2 = reducible(new_word, n - 1)
        for new_word_2 in new_words_2:
            new_words_3 = reducible(new_word_2, n - 2)
            for new_word_3 in new_words_3:
                new_words_4 = reducible(new_word_3, n - 3)
                for new_word_4 in new_words_4:
                    new_words_5 = reducible(new_word_4, n - 4)
                    for new_word_5 in new_words_5:
                        new_words_6 = reducible(new_word_5, n - 5)
                        for new_word_6 in new_words_6:
                            new_words_7 = reducible(new_word_6, n - 6)
                            for new_word_7 in new_words_7:
                                new_words_8 = reducible(new_word_7, n - 7)
                                for new_word_8 in new_words_8:
                                    new_words_9 = reducible(new_word_8, n - 8)
                                    for new_word_9 in new_words_9:
                                        new_words_10 = reducible(new_word_9, n - 9)
                                    for new_word_10 in new_words_10:
                                        if new_word_10 in d[n - 10]:
                                            s.add(f"{target_word}-{new_word}-{new_word_2}-{new_word_3}-{new_word_4}-{new_word_5}-{new_word_6}{new_word_7}-{new_word_8}-{new_word_9}-{new_word_10}")
                                            break  # Break once the full chain is found
print(s)
print(len(s))