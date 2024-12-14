import turtle
import math
class Rectangle():
    def __init__(self,corner,width,height):
        self.corner=corner
        self.width=width
        self.height=height
class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y

class Circle():
    def __init__(self,center,radius):
        self.center=center
        self.radius=radius
def draw_rect(t,box):
    t.pu()
    t.goto(box.corner.x,box.corner.y)
    t.pd()
    for side in [box.width,box.height]*2:
        t.fd(side)
        t.lt(90)

def draw_circle(t,circle):
    t.pu()
    t.goto(circle.center.x,circle.center.y)
    t.fd(circle.radius)
    t.lt(90)
    t.pd()
    for _ in range(360):
        t.fd(math.pi*circle.radius/180)
        t.lt(1)

if __name__=="__main__":
    rect_corner = Point(100, 150)
    box = Rectangle(rect_corner, 90, 50)
    circle_center=Point(50,70)
    circle=Circle(circle_center,100)
    bob = turtle.Turtle()
    #draw_rect(bob, box)
    draw_circle(bob,circle)
    turtle.done()
