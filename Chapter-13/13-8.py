#we will not rease punctuation, coz it will play a vital role in the code
import random
def make_word_dict():
    with open("C:\\Users\\THINKPAD\\Downloads\\emma.txt") as file:
        t=[]
        #d={}
        process=False
        for line in file:
            if "*** START OF THE PROJECT" in line:
                process=True
                continue
            if process:
                words=line.split()
                for word in words:
                    cleaned_word=word.lower()
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
            prefix_suffix_map[prefix]=[]
        prefix_suffix_map[prefix].append(suffix)
    return prefix_suffix_map
#print(h)
def probability_list(c):
    result_dict={}
    for prefix,suffix in c.items():
        total_words=len(suffix)
        #create a new dictionary of mapping suffix words to relative frequencies
        freq_map=count_suffix_frequencies(suffix)
        #create a new dictionary of mapping suffix word to probabilty of getting a word
        prob_map=probability_of_suffix(freq_map,total_words)
        #modify the dictionary mapping prefix words (tuple) to probabilty of getting a word as suffix
        result_dict[prefix]=prob_map
    return result_dict
def count_suffix_frequencies(p):
    d = {}
    for word in p:
        d[word] = d.get(word, 0) + 1
    return d

def probability_of_suffix(f,total):
    for key, value in f.items():
        f[key] = value / total
    return f
#print(collection(h,4))

#print(probability_list(c))

def generate_random_text(prefix_suffix_map,prefix_length,max_words):
    prefixes=list(prefix_suffix_map.keys())  #prepare a list of all keys
    current_prefix=random.choice(prefixes)  #start with a random prefix, all are in tuple
    generated_words=list(current_prefix)   # make a list to work with, as tuples are immutable

    for i in range(max_words-prefix_length):
        if current_prefix not in prefix_suffix_map:  #checking current_prefix, not the generated_word; as generated words are modified to list
            break
        suffixes=list(prefix_suffix_map[current_prefix].keys()) #making a list for the probable next word
        weights=list(prefix_suffix_map[current_prefix].values())  #making a list for the weights next word
        next_word=random.choices(suffixes,weights)[0]  #we will get a list from random.choices, so we need to call the 1st element

        #we have a list of generated words
        generated_words.append(next_word) # it updates the list

        current_prefix=tuple(generated_words[-prefix_length:]) #current prefix is updated, must be in tuple as before
    return " ".join(generated_words)


max_words=50
prefix_length=100
c=collection(h,prefix_length)
prefix_suffix_map=probability_list(c)
print(generate_random_text(prefix_suffix_map,prefix_length,max_words))
