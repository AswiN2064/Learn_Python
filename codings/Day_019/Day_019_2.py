'''
Task:

To build a Etch-a-sketch app using turtle module
'''


from turtle import Turtle, Screen

pointer = Turtle()
screen = Screen()

def move_forward():
    pointer.forward(50)

def move_backward():
    pointer.backward(50)

def clock_wise():
    new_heading = pointer.heading() - 10
    pointer.setheading(new_heading)

def anti_clock_wise():
    new_heading = pointer.heading() + 10
    pointer.setheading(new_heading)

def clear():
    pointer.clear()
    pointer.penup()
    pointer.home()
    pointer.pendown()

screen.listen()
screen.onkey(move_backward,"s")
screen.onkey(move_forward,"w")
screen.onkey(anti_clock_wise,"a")
screen.onkey(clock_wise,"d")
screen.onkey(clear,"c")
screen.exitonclick()