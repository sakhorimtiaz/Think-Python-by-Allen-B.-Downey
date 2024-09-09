import string
def word_to_frequency_set():
    with open("C:\\Users\\THINKPAD\\Downloads\\test1.txt",encoding="utf8") as file:
        s = set()
        processing = False
        translation_table=str.maketrans("","",string.punctuation+string.whitespace)
        for line in file:
            if "*** START OF THE PROJECT GUTENBERG EBOOK PETER PETTIGREW'S PRISONER ***" in line:
                # starts after this line, we dont need to write the full line,
                # "*** START OF THE PROJECT " in line:   is also fine
                processing = True
                continue
            if processing:
                words = line.split()
                for word in words:
                    cleaned_word = word.translate(translation_table)
                    cleaned_lower_words = cleaned_word.lower().encode("utf8")
                    """if the word is '---', then cleaned_lower_words will be an empty string, leading '' in the output
                    an empty string is false, thus we can get rid of it."""
                    if cleaned_lower_words:
                        s.add(cleaned_lower_words)
        #no repeated words are there.
        return s
book_set=word_to_frequency_set()
def word_list_set():
    with open("C:\\Users\\THINKPAD\\Downloads\\words.txt", encoding="utf8") as file:
        s = set()
        for line in file:
            word=line.strip().encode("utf8")
            s.add(word)
        return s
word_set=word_list_set()
#print(len(book_set))
#print(word_set)

#we need a list of words that are not found in the word list
def words_not_in_word_set(book_set,word_set):
    s=book_set-word_set
    return s
print(len(words_not_in_word_set(book_set,word_set)))
