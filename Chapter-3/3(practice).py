def newname():
    myname()
    print ("again")
    myname()
def myname():
    print ("okaa")
    print ("hmm")
newname()

def write_twice(a):
    print (a)
    print (a)
#write_twice("I love u."*5)

def lines (line_1, line_2):
    line =line_1+line_2
    #write_twice (line)
    return line
line_1= "I love"
line_2= "You"
result = lines(line_1, line_2)

print (result)
