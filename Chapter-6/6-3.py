def first(word):
    return word[0]
def last(word):
    return word[-1]
def middle(word):
    return word[1:-1]
word= "abbca"
n=len(word)
def is_palindrome(word):
    """Returns True if word is a palindrome."""
    if len(word) <= 1:
        return True
    elif first(word) != last(word):
        return False
    g=is_palindrome(middle(word))
    return g
print(is_palindrome("nayan"))
