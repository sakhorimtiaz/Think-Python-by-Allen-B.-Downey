import string
def word_to_frequency_dict():
    with open("C:\\Users\\THINKPAD\\Downloads\\test1.txt",encoding="utf8") as file:
        d = {}
        t = []
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
                        d[cleaned_lower_words] = d.get(cleaned_lower_words, 0) + 1
                        t.append(cleaned_lower_words)

        #print("words with their frequency:", d)
        #print("different words: ", len(d))
        #print("total words", len(t))
        return d
d=word_to_frequency_dict()
#p=list(d.values())
#q=sorted(p,reverse=True)
#print(q)
#print(len(q))
#print(q[:20])

def frequency_to_word_dict():
    f = {}
    for key, value in d.items():
        if value not in f:
            f[value] = [key]
        else:
            f[value].append(key)
    #print(f)
    return f
f=frequency_to_word_dict()

def sorted_freq_to_word_dict():
    sorted_f = dict(sorted(f.items(), reverse=True))
    #print(sorted_f)
    return sorted_f
sorted_f=sorted_freq_to_word_dict()

def most_frequently_used_word():
    n = 1
    for key, value in sorted_f.items():
        if n <= 20:
            print(f"the word/words {value} is found {key} times in the book")
            n += 1

most_frequently_used_word()
