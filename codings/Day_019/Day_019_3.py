'''
Task:

To create a turtle race.
'''

from turtle import Turtle, Screen
import random as rd

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet", prompt="which turtle will win the race ?/nEnter the color ?")
colors = ["red","orange","yellow","green","blue","purple"]
y_axis = [-70,-40,-10,20,50,80]
# print(user_bet)

is_race_on = False

#understanding the co ordinates  x and y axis
#pointer = Turtle(shape = "turtle")
#pointer.penup()
#pointer.goto(x = -230, y = 0)

all_turtles=[]
for i in range(0,6):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    #understanding the co ordinates  x and y axis
    new_turtle.goto(x = -230, y = y_axis[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if user_bet == winner:
                print(f"you won, the {winner} is the winner")
            else:
                print(f"you lose, the {winner} is the winner")
            is_race_on = False
        speed = rd.randint(0,10)
        turtle.forward(speed)

screen.exitonclick()