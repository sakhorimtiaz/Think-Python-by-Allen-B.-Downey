import math

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

def point_in_circle(circle,any_point):
    return distance(circle.center,any_point)<=circle.radius

if __name__=="__main__":
    test_point = Point(225, 90)
    center_point = Point(150, 100)
    circle = Circle(center_point, 75)
    result=point_in_circle(circle,test_point)
    print(result)
