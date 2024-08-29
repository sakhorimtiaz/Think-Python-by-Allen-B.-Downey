import string
with open("C:\\Users\\THINKPAD\\Downloads\\test1.txt") as file:
    for line in file:
        words=line.split()
        for word in words:
            cleaned_word=word.strip(string.punctuation)
            cleaned_lower_words=cleaned_word.lower()
            print(cleaned_lower_words)
