class Time():
    def __init__(self,hour,minute,second):
        self.hour=hour
        self.minute=minute
        self.second=second
t1=Time(11,20,30)
t2=Time(11,40,20)

def print_time(t):
    print(f"{t.hour:02}:{t.minute:02}:{t.second:02}") #padded with zeros, two digits output
#print_time(t1)
def is_after(t1,t2):
    time_1 = t1.hour * 60 * 60 + t1.minute * 60 + t1.second
    time_2 = t2.hour * 60 * 60 + t2.minute * 60 + t2.second
    return time_1>time_2
#print(is_after(t1,t2))
#pure function
def add_time(t1,t2):
    h=t1.hour+t2.hour
    m=t1.minute+t2.minute
    s=t1.second+t2.second
    if s>=60:
        s=s%60
        m+=1
    if m>=60:
        m=m%60
        h+=1
    sum=Time(h,m,s)
    return sum
#print_time(add_time(t1,t2))
#modifier
def increment(t,seconds):

    t.second+=seconds
    #overflow of seconds to minutes
    t.minute+=t.second//60
    t.second=t.second%60
    #overflow of minutes to seconds
    t.hour+=t.minute//60
    t.minute=t.minute%60
time=Time(2,50,45)
#increment(time,600)
#print_time(time)

#pure version of increment
def increment_pure(t,seconds):
    s = t.second + seconds
    #overflow of seconds to minutes
    m = t.minute + s//60
    s = s%60
    #overflow of minutes to seconds
    h = t.hour + m//60
    m = m%60
    t3 = Time(h, m, s) #t3=new_time
    return t3
new_time=increment_pure(time,600)
#print_time(time)  #original time
#print_time(new_time)  #incremented time

#designed development
def time_to_int(t):
    minutes=t.hour*60+t.minute
    seconds=minutes*60+t.second
    return seconds
#print_time(time)
#print(time_to_int(time))

def int_to_time(seconds):
    (minutes,remaining_seconds)=divmod(seconds,60)
    hour,remaining_minutes=divmod(minutes,60)
    time=Time(hour,remaining_minutes,remaining_seconds)
    return time
#checking_time=int_to_time(10245)
#print_time(checking_time)

#consistency check
x=890765
#print(time_to_int(int_to_time(x))==x)

def add_time_new(t1,t2):
    seconds=time_to_int(t1)+time_to_int(t2)
    return int_to_time(seconds)

#print_time(t1)
#print_time(t2)
#print_time(add_time_new(t1,t2))

def increment_new(t,seconds):
    s=time_to_int(t)+seconds
    return int_to_time(s)
#print_time(time)
#print_time(increment_new(time,600))

def subtract_time(t1,t2):
    a=time_to_int(t1)
    b=time_to_int(t2)
    return int_to_time(abs(a-b))
#print_time(t1)
#print_time(t2)
#print_time(subtract_time(t1,t2))

#adding invariants
def valid_time(t):
    if t.hour<0 or t.minute<0 or t.second<0:
        return False
    if t.minute>=60 or t.second>=60:
        return False
    return True

def add_time_invariants(t1,t2):
    if not (valid_time(t1) and  valid_time(t2)):
        raise ValueError("invalid Time object in add_time")
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)
try:
    t3 = Time(3, 7, 50)
    t4 = Time(5, 56, 70)
    print_time(t3)
    print_time(t4)
    print_time(add_time_invariants(t3, t4))
except ValueError as e:
    print(e)
def add_time_invariants_using_assert(t1,t2):
    assert (valid_time(t1) and  valid_time(t2)), "invalid"
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)

#print_time(add_time_invariants_using_assert(t3,t4))
try:
    t3 = Time(3, 7, 50)
    t4 = Time(5, 56, 70)
    print_time(t3)
    print_time(t4)
    print_time(add_time_invariants_using_assert(t3, t4))
except AssertionError as e:
    print(e)
