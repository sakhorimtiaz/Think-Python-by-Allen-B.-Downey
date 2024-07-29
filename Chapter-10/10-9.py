import time
def attempt1():
    with open("C:\\Users\\THINKPAD\\Downloads\\words.txt") as file:
        x = []
        for i in file:
            p = i.strip()
            x.append(p)
        # print(x)
        return x

def attempt2():
    with open("C:\\Users\\THINKPAD\\Downloads\\words.txt") as file:
        t = []
        for i in file:
            p = i.strip()
            t = t + [p]
        # print(t)
        return t
start_time=time.time()
#print(time.time())
t1=attempt1()
end_time=time.time()
#print(time.time())
elapsed_time=end_time-start_time
print("time for 1st attempt: ",elapsed_time)

start_time=time.time()
t2=attempt2()
elapsed_time=time.time()-start_time
print("time for 2st attempt: ",elapsed_time)

"""The t = t + [p] operation creates a new list by concatenating t and [p]. This operation is more costly 
because it involves creating a new list and copying all elements from t and [p] into the new list. """
