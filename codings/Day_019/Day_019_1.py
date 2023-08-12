'''
turtle.onkey(fun, key)
turtle.onkeyrelease(fun, key)

Parameters:
fun : a function with no arguments or None

key : a string: key (e.g. “a”) or key-symbol (e.g. “space”)

Bind fun to key-release event of key. 
If fun is None, event bindings are removed. Remark: in order to be able to register key-events, TurtleScreen must have the focus
'''


from turtle import Turtle, Screen

pointer = Turtle()
screen = Screen()

def move_forward():
    pointer.forward(10)

screen.listen()
screen.onkey(key = "space", fun = move_forward)
screen.exitonclick()