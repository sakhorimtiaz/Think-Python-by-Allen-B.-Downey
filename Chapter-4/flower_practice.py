#taken from the author's solution
from __future__ import print_function, division

import turtle

from exercise import arc


def petal(t, r, angle):
    """Draws a petal using two arcs.

    t: Turtle
    r: radius of the arcs
    angle: angle (degrees) that subtends the arcs
    """
    for i in range(2):
        arc(t, r, angle)
        t.lt(180-angle)

def polygon(t, n, length):
    """Draws a polygon with n sides.

    t: Turtle
    n: number of sides
    length: length of each side.
    """
    angle = 360.0/n
    polyline(t, n, length, angle)

def polyline(t, n, length, angle):
    """Draws n line segments.

    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def flower(t, s, r, angle):
    """Draws a flower with s petals.

    t: Turtle
    s: number of petals
    r: radius of the arcs
    angle: angle (degrees) that subtends the arcs
    """
    for i in range(s):
        petal(t, r, angle)
        t.lt(360.0/s)


def move(t, length):
    """Move Turtle (t) forward (length) units without leaving a trail.
    Leaves the pen down.
    """
    t.pu()
    t.fd(length)
    t.pd()


bob = turtle.Turtle()

# draw a sequence of three flowers, as shown in the book.
move(bob, -100)
flower(bob, 7, 60.0, 60.0)

move(bob, 100)
flower(bob, 10, 40.0, 80.0)

move(bob, 100)
flower(bob, 20, 140.0, 20.0)

bob.hideturtle()
turtle.mainloop()
