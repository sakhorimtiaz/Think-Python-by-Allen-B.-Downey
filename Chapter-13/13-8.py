Question-1:
import random
import string
def make_word_dict():
    with open("C:\\Users\\THINKPAD\\Downloads\\test(markov).txt") as file:
        t=[]
        #d={}
        process=False
        translation_table=str.maketrans("","",string.whitespace+string.punctuation)
        for line in file:
            if "*** START OF THE PROJECT" in line:
                process=True
                continue
            if process:
                words=line.split()
                for word in words:
                    cleaned_word=word.translate(translation_table).lower()
                    if cleaned_word:
                        t.append(cleaned_word)
                        #d[cleaned_word]=d.get(cleaned_word,0)+1
        return t
h=make_word_dict()

def collection(h,prefix_length):
    prefix_suffix_map={}
    for i in range(len(h)-prefix_length):
        prefix=tuple(h[i:i+prefix_length])
        suffix=h[i+prefix_length]
        if prefix not in prefix_suffix_map:
            prefix_suffix_map[prefix]=[] #use set to ignore the repeated words in values, but list will be used for getting the random analysis
        prefix_suffix_map[prefix].append(suffix)
    return prefix_suffix_map
print(h)
print(collection(h,2))
