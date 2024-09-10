#this process is not asked, but I did anyway.
import random
import string
def all_words_list(book,encoding="utf8"):
    with open(book) as file:
        t = []
        processing = False
        translation_table = str.maketrans("", "", string.punctuation + string.whitespace)
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
                        t.append(cleaned_lower_words)
        return t
h=all_words_list("C:\\Users\\THINKPAD\\Downloads\\test1.txt",encoding="utf8")
n=len(h)
print(n)
r=random.randint(1,n)
print(r)
print(h[r-1])
