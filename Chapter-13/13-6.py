import random
# Original histogram function
string = "abbcdddefg"
def histogram(string):
    d = {}
    for char in string:
        d[char] = d.get(char, 0) + 1
    return d
print(histogram(string))
h = histogram(string)
def choose_from_hist(h):
    length=sum(h.values())
    cumulative=0
    rand_val=random.uniform(0,length)
    for char,frequency in h.items():
        cumulative+=frequency
        if rand_val<cumulative:
            print((rand_val,char,frequency))
            return char
# Example of using the function
chosen_char = choose_from_hist(h)
print(chosen_char)