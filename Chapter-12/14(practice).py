def practice1():
    for i in range(2, 6):
        print(f"Number: {i:5} | Square: {i ** 2:5}")
    price = 49.99
    discount = 0.2
    message = f"The price after {discount * 100:.0f}% discount is ${price * (1 - discount):.2f}."
    print(message)

def writing_file():
    with open("C:\\Users\\THINKPAD\\Downloads\\text_write.txt", "w") as file:
        line_1 = "i am fine\n"
        line_2 = "love me 2"
        line_3 = "5"
        file.write(line_1)
        file.write(line_2)
        file.write(line_3)
    with open("text_write.txt", "w") as file1:
        line_1 = "i am fine\n"
        line_2 = "love me 2"
        line_3 = "5"
        file1.write(line_1)
        file1.write(line_2)
        file1.write(line_3)

import os
directory=os.getcwd()
def practice2():
    name = os.getcwd()
    print("name is", name)
    absolute_path = os.path.abspath("12debugging\\text_write.txt")
    # print("bool",os.path.isabs("12(debugging\\text_write.txt"))
    print(absolute_path)
    print("path", os.path.exists("7.2.py"))
    print(os.path.isdir("C:\\Users\\THINKPAD\\PycharmProjects\\linearegression\\12(debugging"))  # line23
    print(
        os.path.isfile("C:\\Users\\THINKPAD\\PycharmProjects\\linearegression\\12(debugging\\text_write.txt"))  # line24
    print(os.listdir(name))
    print(os.path.exists("13-1.py"))
    print(os.path.abspath("(7.1).py"))
    print(os.path.exists("C:\\Users\\THINKPAD\\PycharmProjects\\linearegression\\(7.1).py"))


def walk(directory):
    for name in os.listdir(directory):
        path=os.path.join(directory,name)
        if os.path.isfile(path):
            print(path)
        else:
            walk(path)
#walk(directory)
def errors():
    fin = open("badfile")
    print(fin)
    with open("C:\\Users\\THINKPAD\\Downloads", "r") as file:
        pass
def catching_exceptions():
    try:
        fin = open("badfile")
    except:
        print("opps")

def loop_with_dbm_and_pickle():
    import dbm
    import pickle
    with dbm.open("creation", "c") as db:
        db["nnn.txt"] = "love"
        db["mmm.png"] = "yourself"
        t1=[1,2,3,4]
        s=pickle.dumps(t1)
        db["list"]=s
        db["list object"]=pickle.loads(s)

        for key in db:
            print(key, db[key])
    with dbm.open("creation", "r") as ku:
        for key in ku:
            print(key, ku[key])
def database_creation_with_shelve():
    import shelve
    db = shelve.open("test database3", "c")
    db["name"] = "Imtiaz"
    db["age"] = "36"
    db["roll"] = 9
    db["list"] = [1, 2, 3]

    db.close()
    db = shelve.open("test database3", "r")
    print(type(db["age"]))
    print(type(db["roll"]))
    print(db["list"])
    print(type(db["list"]))
"""import pickle
t1=[1,2,3,4]
s=pickle.dumps(t1)
t2=pickle.loads(s)
print(type(s))
print(type(t2))

print(t1==t2)
print(t1 is t2)
"""
import os
def concept_of_pipes():
    cmd = 'dir'  # Use 'dir' instead of 'ls -l' for Windows
    fp = os.popen(cmd)  # Runs the command and opens a pipe to it
    output = fp.read()  # Read the output from the pipe
    # print(output)  # Print the output
    # print(fp)
    stat = fp.close()
    print(output)
    # print(stat)

def hash_function():
    file="C:\\Users\\THINKPAD\\Downloads\\emma.txt"

    cmd = 'certutil -hashfile ' + file +' MD5'

    fp=os.popen(cmd)
    res=fp.read()
    stat=fp.close()
    print(res)
    print(stat)
def byte():
    byte_literal = b"hello"
    byte_array = bytes([100, 101])
    print(byte_literal)
    print(byte_array)
    print(type(byte_literal))
    print(type(byte_array))
def importing_a_code():
    # use import directly if the file is in the same directory.
    import wc

    # or use this approach if it is in a different directory.
    import sys
    sys.path.append(r"C:\Users\THINKPAD\PycharmProjects\linearegression\12debugging")
    import wc

#byte()
import wc
wc.linecounter("C:\\Users\\THINKPAD\\PycharmProjects\\linearegression\\12debugging\\wc.py")

s1=("12\t3 \r4")
s2=("12\t3 \n4")
print(s1)
print("......")
print(s2)
print(repr(s1))
