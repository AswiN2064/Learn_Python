# drawing a square using turtle
from turtle import Turtle, Screen

turtle = Turtle()
turtle.shape("turtle")
turtle.color("red")
def square():
    a = 4
    while a != 0:
        turtle.forward(100)
        turtle.left(90)
        a -= 1

square()

screen = Screen()
screen.exitonclick()