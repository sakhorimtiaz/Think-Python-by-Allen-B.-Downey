import math
#page179
class Point():
    pass
def distance_between_points(p1,p2):

    #print_Point(p1)
    #print_Point(p2)
    distance=math.sqrt((p1.x-p2.x)**2+(p1.y-p2.y)**2)

    return distance
def print_Point(p):
    print(f" ({p.x},{p.y})")
p1=Point()
p1.x=2
p1.y=3
p2=Point()
p2.x=7
p2.y=10
#print(distance_between_points(p1,p2))
class Rectangle():
    pass

box=Rectangle()
box.width=100
box.height=50
box.corner=Point()
box.corner.x=34
box.corner.y=45

def find_center(rect):
    p=Point()
    p.x=rect.corner.x+rect.width/2
    p.y=rect.corner.y+rect.height/2
    return p
center=find_center(box)
#print_Point(center)

def grow_rectangle(rect,dwidth,dheight):
    rect.width += dwidth
    rect.height += dheight
#print(box.width,box.height)
#grow_rectangle(box,30,10)
#print(box.width,box.height)
#page181
def move_rectangle(rect,dx,dy):
    rect.corner.x+=dx
    rect.corner.y+=dy
move_rectangle(box,10,10)
#print(box.corner)
#print_Point(box.corner)

#####################
#page182
import copy
p1=Point()
p1.x=3.0
p1.y=4.0
p2=copy.copy(p1)
"""print_Point(p1)
print_Point(p2)
print("<<point>>")
print("copy.copy")
print(p1 == p2)
print(p1 is p2)
print("copy.deepcopy")
p3=copy.deepcopy(p1)
print(p1 == p3)
print(p1 is p3)

print("copy.copy")
box2=copy.copy(box)
print("<<box>>")
print(box2==box)
print(box2 is box)
print("<<box.corner>>")
print(box2.corner == box.corner)
print(box2.corner is box.corner)
print("copy.deepcopy")
box3=copy.deepcopy(box)
print("<<box>>")
print(box3==box)
print(box3 is box)
print("<<box.corner>>")
print(box3.corner == box.corner)
print(box3.corner is box.corner)"""
"""a=2000
b=2000
print(b==a)
print(b is a)

a1=2000
b1=copy.copy(a)
print(b1==a1)
print(b1 is a1)

c=[1,2,3]
d=[1,2,3]
print(c is d)
print(c == d)

c1=[1,2,3]
d1=copy.copy(c1)
print(c1 is d1)
print(c1 == d1)
"""
x=[1,2,3,4]
y=x
x[0]=5
#print(x)
#print(y)
z=copy.copy(y)
#print(z)

m=[1,2,3,[4,[5,6]],7]
n=m
k=copy.copy(m)
h=copy.deepcopy(m)
m[0]=0
m[3][0]=9
print("m",m)
print("n",n)
print("k",k)
print("h",h)
print("copy.copy")
print(m==k)
print(m is k)
print(m==n)
print(m is n)
print("copy.deepcopy")
print(m==h)
print(m is h)
"""
p=Point()
p.x=3

a=7
print(type(p))
print(isinstance(p,Point))
print(isinstance(a,Point))
print(hasattr(p,"x"))
print(hasattr(p,"z"))

try:
    x=p.x
except AttributeError:
    x=0
"""
#page183
p=Point()
box=Rectangle()
box.corner=Point()
box.corner.x=4
box.corner.y=8
box.width=100
box.length=50
def move_rectangle(rect,dx,dy):
    new_box=copy.copy(rect)
    new_box.corner.x+=dx
    new_box.corner.y+=dy
    return new_box
print_Point(box.corner)
moved_box=move_rectangle(box,10,10)
print_Point(box.corner)
print_Point(moved_box.corner)
