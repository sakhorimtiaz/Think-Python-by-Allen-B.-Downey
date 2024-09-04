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
                        d[cleaned_lower_words] = None
        #no repeated words are there.
        return d
book_dict=word_to_frequency_dict()
def word_list_dict():
    with open("C:\\Users\\THINKPAD\\Downloads\\words.txt", encoding="utf8") as file:
        d = {}
        for line in file:
            word=line.strip().encode("utf8")
            d[word]=None
        return d
word_dict=word_list_dict()
#print(len(book_dict))
#print(word_dict)

#we need a list of words that are not found in the word list
def words_not_in_word_dict():
    t = []
    for key in book_dict:
        if key not in word_dict:
            t.append(key)
    #print(len(t))
    return t
words_not_found_in_word_dict=words_not_in_word_dict()

#now we need to find the typo
import difflib
def find_typo_suggestion(word,word_dict):
	suggestions=difflib.get_close_matches(word,word_dict.keys(),n=1,cutoff=0.8)
	return suggestions

def identify_typos(words_not_found_in_word_dict,word_dict):
	typos=[]
	for word in words_not_found_in_word_dict:
		suggestions=find_typo_suggestion(word,word_dict)
		if suggestions:
			typos.append((word,suggestions[0]))
	return typos
print(identify_typos(words_not_found_in_word_dict,word_dict))
