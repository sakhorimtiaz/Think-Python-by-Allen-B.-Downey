def do_twice(f):
    f()
    f()
def print_spam():
    print ("spam")
do_twice(print_spam)

def do_twice(f,v):    #3.2 page 33
    f(v)
    f(v)

def print_spam(a):
    print (a)
do_twice(print_spam,"spam")

def do_twice(f,v):
    f(v)
    f(v)
def print_twice(a):
    print (a)
    print (a)
do_twice(print_twice, "spam")
def do_four(f,v):
	do_twice(f,v)
	do_twice(f,v)
	
print ("--------cutting line---------")

do_four(print_twice,"four")

def do_four(f,v):
    do_twice(f,v)
    do_twice(f,v)
do_twice(print, 'spam')
print (" ")
do_four(print, 'spam')
