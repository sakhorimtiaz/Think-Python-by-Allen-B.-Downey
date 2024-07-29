# odometer:
#I have used product() which generates numbers. But time consuming. The second version in just great.
from itertools import product
digits = "0123456789"
number_list=list(product(digits,repeat=6)) # in a list all the 6 digits are there as individual string,
                                           # we need a single string
def digit_palindrome(number_string,a,b,c,d,e,f):
    if number_string[a]==number_string[f] and number_string[b]==number_string[e] and number_string[c]==number_string[d]:
        number_integer=int(number_string)
        next_number_integer=number_integer+1
        next_number_string=str(next_number_integer)
        if len(next_number_string)==6:  #the next number can be of 7 digits, like 999999+1=1000000
            return str(next_number_string)
    return "0"
def is_palindrome(number_string):
    i=0
    j=len(number_string)-1
    while i<j:
        if number_string[i]!=number_string[j]:
            return "0"
        i=i+1
        j=j-1
    return number_string
for number_tuple in number_list:
    number_string="".join(number_tuple)
    a=digit_palindrome(number_string,2,3,0,0,4,5)
    if a!="0":
        b=digit_palindrome(a,1,2,0,0,4,5)
        if b!="0":
            c=digit_palindrome(b,1,2,0,0,3,4)
            if c!="0":
                d=is_palindrome(c) #we have used a differnt function as we dont ned to add 1 with the number
                if d!="0":
                    print("the number odometer showed was: ",number_string, " ,when I looked at it at 1st")
                    print("the number odometer showed was: ",d, " ,when I looked at it after 3 miles")

#odometer: this was taken from solution section.
"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division


def has_palindrome(i, start, length):
    """Checks if the string representation of i has a palindrome.

    i: integer
    start: where in the string to start
    length: length of the palindrome to check for
    """
    s = str(i)[start:start + length]   #p = str(i),,,,,,, then s=p[strat:start+length]
    return s[::-1] == s                #s[::-1] from reverse.


def check(i):
    """Checks if the integer (i) has the desired properties.

    i: int
    """
    return (has_palindrome(i, 2, 4) and
            has_palindrome(i + 1, 1, 5) and
            has_palindrome(i + 2, 1, 4) and
            has_palindrome(i + 3, 0, 6))


def check_all():
    """Enumerate the six-digit numbers and print any winners.
    """
    i = 100000
    while i <= 999996: #as we need to 3 in total so 999996+3=999999; the possible last number.
        if check(i):
            print(i)
        i = i + 1


print('The following are the possible odometer readings:')
check_all()
print()
