from turtle import Turtle, Screen

pointer = Turtle()
a = 15
while a != 0:
    pointer.forward(10) # to draw
    pointer.penup()
    pointer.forward(10) # to move
    pointer.pendown()
    a -= 1


screen = Screen()
screen.exitonclick()