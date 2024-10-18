import ex14_1_12_2
import shelve
#anagrams=ex14_1_12_2.anagram_sets("C:\\Users\\THINKPAD\\Downloads\\words.txt")
def store_anagrams():
    with shelve.open("anagrams_shelf","c") as shelf:
        for group in anagrams:
            s = "".join(sorted(group[0]))
            shelf[s] = group

def read_anagrams(word):
    with shelve.open("anagrams_shelf") as shelf:
        new_word="".join(sorted(word))
        for key in shelf:
            if key==new_word:
                print(f"The anagrams of the word '{word}' are {shelf[key]}")
                break
        else:
            print("no match found")
if __name__=="__main__":
    anagrams = ex14_1_12_2.anagram_sets("C:\\Users\\THINKPAD\\Downloads\\words.txt")
    store_anagrams()
    read_anagrams('bird')