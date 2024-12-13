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

def diagonal_of_rectangle(box):
    return math.sqrt(box.width**2+box.height**2)
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
#print(rect_in_circle())
#print(point_in_circle(circle,box))

def rect_circle_overlap(circle,box):
    points = moved_rect(box)
    x1,y1=box.corner.x,box.corner.y
    x2,y2=box.corner.x+box.width,box.corner.y+box.height
    # check if any of the corners is inside
    for point in points:
        if point_in_circle(circle, point):
            return True
    # Check if circle's center is inside the rectangle
    if (box.corner.x <= circle.center.x <= box.corner.x + box.width and
        box.corner.y <= circle.center.y <= box.corner.y + box.height):
        return True
    closest_x = max(x1, min(circle.center.x, x2))
    closest_y = max(y1, min(circle.center.y, y2))
    closest_point=Point(closest_x,closest_y)
    if point_in_circle(circle,closest_point):
        return True
    
    return False

if __name__=="__main__":
    rect_corner = Point(10, 80)
    box = Rectangle(rect_corner, 95, 40)
    center_point = Point(100, 100)
    circle = Circle(center_point, 10)
    print(rect_circle_overlap(circle,box))
