with open("C:\\Users\\THINKPAD\\Downloads\\words.txt", "r") as file:
    # Read the file into a variable called wiki
    #wiki = file.read()
    first_line=file.readline()
    #print(repr(first_line))#to see the newline character
    #print(first_line)
#2nd half
def is_abecendarian(word):
    previous=word[0]
    for c in word:
        if c<previous:
            return False
        previous =c
    return True
#print(is_abecendarian("abdc"))
#print("c">"d")
def is_palindrome(word):
    i=0
    j=len(word)-1
    while i<j:
        if word[i]!=word[j]:
            return False
        i=i+1
        j=j-1
    return True
#print(is_palindrome("12021"))
