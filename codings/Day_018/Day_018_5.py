import turtle as t
import random as r

pointer = t.Turtle()
t.colormode(255)

def random_color():
    red = r.randint(0,255)
    green = r.randint(0,255)
    blue = r.randint(0,255)
    random_color = (red,green,blue)
    return random_color

directions = [0,90,180,270]
pointer.pensize(15)
pointer.speed("fastest")

for _ in range(1000):
    
    pointer.color(random_color())
    pointer.forward(30)
    pointer.setheading(r.choice(directions)) # for angle


screen = t.Screen()
screen.exitonclick()
