# import turtle

# paint = turtle.Turtle()
# Turtle is the class in the turtle package and
# The Class is always started using uppercase
# here "paint" the object. just like assigning variable to a function.

# we can also use this code ↓

from turtle import Turtle, Screen
paint = Turtle()

print(paint)  #<- an seperate window will be opened with a arrow.
paint.shape("triangle") # triangle shaped brush had been created.
paint.color('coral') # changes the colour of the pen
paint.forward(100) # creating a box
paint.right(90) # turning 90 degree right
paint.forward(100)
paint.right(90)
paint.forward(100)
paint.right(90)
paint.forward(100)
paint.right(90)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()   #exit the code when i am clicking on the screen

