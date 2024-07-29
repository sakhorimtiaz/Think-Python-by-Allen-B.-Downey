#incorrect
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False
#flaws:if the 1st letter is uppercase it will execute "False" and get out from the loop
#corrected version:
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
    return False
#print(any_lowercase1("ABC"))

#incorrect
def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'
#here, "c" is a sting, not the c in s;
#again "True" is string, not boolean
#print(any_lowercase2("AAAAA"))


#incorrect
def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag
#it only shows the last letter to be true or not,
#as flag variable is updated after each iteration
#print(any_lowercase3("aaA"))

#corrcet
def any_lowercase4(s):
    flag=False
    for c in s:
        flag=flag or c.islower()
    return flag
#1st flag = False; updated in flag
#then False or False becomes False; updated in flag
#then False or True becomes True; updated in flag
#then True or false becomes True; updated in flag
print(any_lowercase4("AbC"))

#correct
