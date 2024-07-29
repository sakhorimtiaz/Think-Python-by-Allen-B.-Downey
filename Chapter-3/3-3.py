#question-1
def do_two_times(f):
    f()
    f()
def do_four_times(a):
    do_two_times(a)
    do_two_times(a)

def row1():
    print ("+ - - - -", end= " ") # dont go to the new line, 
def row2():
    print ("|        ", end= " ")
def column1():
    do_two_times(row1)                  # dont put row1(), coz it has no value.
    print ("+")
def column2():
    do_two_times(row2)
    print ("|")
def set_1():
    column1()
    do_four_times(column2)
def set_1st_two():
    do_two_times(set_1)
def two_by_two_grid():
    set_1st_two()
    column1()
two_by_two_grid()

#question-2
def twotimes(f):
    f()
    f()
def fourtimes(a):
    twotimes(a)
    twotimes(a)
def function_of_three(x,y,z):
    x()
    fourtimes(y)
    z()

def plussign():
    print ("+", end= " ")
def dashsign():
    print ("-", end= " ")
def barsign():
    print ("|", end= " ")
def space():
    print (" ", end= " ")
def newline():
    print ()
def do_nothing():
    "no action"


def onebeam():
    function_of_three(do_nothing,dashsign,plussign)
def row_one():
    function_of_three(plussign,onebeam,newline)

def onepost():
    function_of_three(do_nothing,space,barsign)
def row_two():
    function_of_three(barsign,onepost,newline)

def block_one():
    function_of_three(row_one,row_two,do_nothing)
def block_without_last_row():
    function_of_three(do_nothing,block_one,do_nothing)

def final_out_put():
    function_of_three(block_without_last_row,do_nothing,row_one)
final_out_put()
