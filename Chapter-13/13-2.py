import string
with open("C:\\Users\\THINKPAD\\Downloads\\test1.txt") as file:
    d={}
    t=[]
    processing=False
    for line in file:
        if "*** START OF THE PROJECT GUTENBERG EBOOK PETER PETTIGREW'S PRISONER ***" in line:
            #starts after this line, we dont need to write the full line,
            # "*** START OF THE PROJECT " in line:   is also fine
            processing=True
            continue
        if processing:
            words = line.split()
            for word in words:
                cleaned_word = word.strip(string.punctuation)
                cleaned_lower_words = cleaned_word.lower()
                """if the word is '---', then cleaned_lower_words will be an empty string, leading '' in the output
                an empty string is false, thus we can get rid of it."""
                if cleaned_lower_words:
                    d[cleaned_lower_words] = d.get(cleaned_lower_words, 0) + 1
                    t.append(cleaned_lower_words)

    print("words with their frequency:", d)
    print("different words: ",len(d))
    print("total words",len(t))


