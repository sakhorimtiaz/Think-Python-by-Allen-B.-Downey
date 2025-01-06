class Time():
    def __init__(self,hour=0,minute=0,second=0):
        self.hour=hour
        self.minute=minute
        self.second=second
    def __repr__(self): #unambiguous for developers
        return f"Time {self.hour:02}:{self.minute:02}:{self.second:02}"
    def __str__(self):  #user friendly
        return f"Time is {self.hour:02}:{self.minute:02}:{self.second:02}"
    def print_time(self):
        print(f"{self.hour:02}:{self.minute:02}:{self.second:02}")  # padded with zeros, two digits output
    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds
    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()
    def increment(self,seconds):
        seconds+=self.time_to_int()
        return int_to_time(seconds)
    def __add__(self, other):
        if isinstance(other,Time):  #no need to write Time()
            return self.add_time(other)
        else:
            return self.increment(other)
    def __radd__(self, other):
        return self.__add__(other)
    def add_time(self, other):
        seconds=self.time_to_int()+other.time_to_int()
        return int_to_time(seconds)
def int_to_time(seconds):
    (minutes, remaining_seconds) = divmod(seconds, 60)
    hour, remaining_minutes = divmod(minutes, 60)
    time = Time(hour, remaining_minutes, remaining_seconds)
    return time
t=Time(5,30,9)
t2=Time(5,30,7)
#print(t.time_to_int()>t2.time_to_int())
#print(t.is_after(t2))
#print(t.time_to_int())
#print(type(t.increment(2)))
total=sum((t,t2))
print(total)
#print(new_time)   #using __str__ directly
#new_time.print_time()   #calling the print_time()
start=Time(4,40,50)
duration=Time(1,40,2)
#end=start.add_time(duration)
#print(end)
#print(start+duration)  # this is same as #end=start.add_time(duration)  #print(end)
#print(6002+start)
class Point():
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __str__(self):
        return f"Point at ({self.x},{self.y})"
    def __repr__(self):
        return f"Point ({self.x},{self.y})"
    def __add__(self, other):
        if isinstance(other,Point):
            return self.add_points(other)
        elif isinstance(other,tuple):
            x=self.x+other[0]
            y=self.y+other[1]
            return Point(x,y)
    def __radd__(self, other):
        return self.__add__(other)
    def add_points(self, other):
        x=self.x+other.x
        y=self.y+other.y
        return Point(x,y)
p=Point()
p1=Point(2,3)
p2=Point(3,2)
p3=(3,3)
#print(p1+p2)
#print(p2+p3)
#print(p3+p1)
print(vars(p2))
def print_attributes(obj):
    for attr in vars(obj):
        print(attr,getattr(obj,attr))
print_attributes(p2)

"""print(type(p))
print(p)
print(type(str(p)))
print(str(p))
print(type(repr(p)))
print(repr(p))"""
