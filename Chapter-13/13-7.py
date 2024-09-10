#original solution
import string
import random
import bisect
def word_book_dict(book,encoding="utf8"):
    with open(book,encoding=encoding) as file:
        d = {}
        processing=False
        translation_table=str.maketrans("","",string.whitespace+string.punctuation)
        for line in file:
            if "*** START OF THE PROJECT" in line:
                processing = True
                continue
            if processing:
                words=line.split()
                for word in words:
                    cleaned_word=word.translate(translation_table)
                    cleaned_lower_words=cleaned_word.lower().encode()
                    if cleaned_lower_words:
                        d[cleaned_lower_words]=d.get(cleaned_lower_words,0)+1
        return d

hist=word_book_dict("C:\\Users\\THINKPAD\\Downloads\\test1.txt",encoding="utf8")

def list_of_keys_of_dict(hist):
    t=[]
    for word,freq in hist.items():
        t.extend([word]*freq)
    return t
all_words=list_of_keys_of_dict(hist)
#print(len(all_words))

def cumulative_freq(hist):
    t=[]
    cumsum=0
    for freq in hist.values():
        cumsum=cumsum+freq
        t.append(cumsum)
    return t
#print(cumulative_freq(hist))
cumsum_list=cumulative_freq(hist)

def random_number(cumsum_list):
    total=cumsum_list[-1]
    n=random.randint(1,total)
    return n
random_n=random_number(cumsum_list)

def random_word():
    index=bisect.bisect(cumsum_list,random_n)
    res=all_words[index]
    return res
print(random_n)
print(random_word())
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
