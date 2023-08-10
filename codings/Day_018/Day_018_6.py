# To draw a spirograph using turtle. the radius of circle is 100.

import turtle as t
import random as r

pointer = t.Turtle()
screen = t.Screen()
t.colormode(255)
pointer.speed("fastest")

def random_color():
    red = r.randint(0,255)
    green = r.randint(0,255)
    blue = r.randint(0,255)
    random_color = (red,green,blue)
    return random_color

for _ in range(90):    
    pointer.color(random_color())
    pointer.circle(100)
    pointer.left(4)


screen.exitonclick()