import math
import turtle

t = turtle.Turtle()
t.speed(100)  # Fastest turtle speed

def draw(t, n, depth):
    if depth == 0:
        t.fd(n)  # Base case: draw straight line of length n
    else:
        draw(t, n / 3, depth - 1)  # Draw one third of the line
        t.lt(60)  # Turn left to create the peak
        draw(t, n / 3, depth - 1)  # Draw one third, the upward part of the triangle
        t.rt(120)  # Turn right to go down the triangle
        draw(t, n / 3, depth - 1)  # Draw one third, the downward part of the triangle
        t.lt(60)  # Turn left to realign with the original angle
        draw(t, n / 3, depth - 1) # draw the last part

#t.lt(60)  # Initial left turn to start drawing from an upward angle
draw(t, 300, 3)
t.rt (120)
draw(t, 300, 3)
t.rt(120)
draw(t, 300, 3)
# Example call to function; adjust depth as needed
turtle.mainloop()



"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

import turtle


def koch(t, n):
    """Draws a koch curve with length n."""
    if n < 10:
        t.fd(n)
        return
    m = n/3
    koch(t, m)
    t.lt(60)
    koch(t, m)
    t.rt(120)
    koch(t, m)
    t.lt(60)
    koch(t, m)


def snowflake(t, n):
    """Draws a snowflake (a triangle with a Koch curve for each side)."""
    for i in range(3):
        koch(t, n)
        t.rt(120)


bob = turtle.Turtle()

bob.pu()
bob.goto(-150, 90)
bob.pd()
snowflake(bob, 300)

turtle.mainloop()
