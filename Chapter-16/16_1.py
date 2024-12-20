class Time():
    def __init__(self,hour,minute,second):
        self.hour=hour
        self.minute=minute
        self.second=second
def print_time(t):
    print(f"{t.hour:02}:{t.minute:02}:{t.second:02}")
def valid_time(t):
    if t.hour>=0 and 0<=t.minute<60 and 0<=t.second<60:
        return True
    return False
def time_to_int(t):
    return t.second+t.minute*60+t.hour*60*60
def int_to_time(seconds):
    m,s=divmod(seconds,60)
    h,remaining_m=divmod(m,60)
    time=Time(h,remaining_m,s)
    return time
def mul_time(t,number):
    if not valid_time(t) or number<0:
        raise ValueError("invalid input")
    total_seconds=time_to_int(t)*number
    return int_to_time(total_seconds)
def average_pace(t,mile):
    return mul_time(t,(1/mile))
try:
    duration = Time(0, 35, 26)
    print_time(duration)
    distance=5 #distance in miles
    print_time(average_pace(duration,distance))
except ValueError as e:
    print(e)
