import turtle
import math
t=turtle.Turtle()
def draw(t,length,n):
    if n==0:
        return
    angle=50
    t.fd(length*n)
    t.lt(angle)
    t.color("red")
    draw(t,length,n-1)
    t.rt(2*angle)
    t.color("yellow")
    draw(t, length, n-1)
    t.color("green")
    t.lt(angle)
    t.bk(length*n)
t.bk(200)
draw(t,130,3)
turtle.mainloop()
turtle.speed(1)
