'''
Task:
`````
Draw a Random walk using turtle.
'''
import turtle as t
import random as r

colors = ["red", "green","blue"]

directions = [0,90,180,270]


pointer = t.Turtle()
pointer.pensize(15)
pointer.speed("fastest")
for _ in range(1000):
    
    pointer.color(r.choice(colors))
    pointer.forward(30)
    pointer.setheading(r.choice(directions)) # for angle


screen = t.Screen()
screen.exitonclick()
