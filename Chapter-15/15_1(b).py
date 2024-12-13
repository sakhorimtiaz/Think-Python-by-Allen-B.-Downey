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
        self.center=center #center is a point object
        self.radius=radius  #radius is a number

def distance(point1,point2):
    d=math.sqrt((point1.x-point2.x)**2+(point1.y-point2.y)**2)  #d=distance_from_test_point_to_center
    return d

def point_in_circle(circle,point):
    return distance(circle.center,point)<=circle.radius
def moved_rect(box):
    point_BL=box.corner
    point_BR=Point(box.corner.x + box.width,box.corner.y)
    point_TL=Point(box.corner.x,box.corner.y + box.height)
    point_TR=Point(box.corner.x + box.width,box.corner.y + box.height)
    return point_TR,point_TL,point_BR,point_BL
    #print (f"TR({point_TR.x},{point_TR.y}), TL({point_TL.x},{point_TL.y}), BR({point_BR.x},{point_BR.y}), BL({point_BL.x},{point_BL.y})")
def rect_in_circle(circle,box):
    points = moved_rect(box)
    for point in points:
        if not point_in_circle(circle, point):
            return False
    return True

if __name__=="__main__":
    rect_corner = Point(150, 90)
    box = Rectangle(rect_corner, 10, 20)
    center_point = Point(150, 100)
    circle = Circle(center_point, 24)
    print(rect_in_circle(circle,box))
