'''
Task:
`````

To draw a triangle, square, pentagon, hexagon, heptagon, octagon, nanogan, decagon using turtle.
The sides of the shapes should be 100px.
'''

from turtle import Turtle, Screen
t = Turtle()
s = Screen()

# triangle
def triangle():
    t.color("red")
    triangle = 3
    sides = 3
    while sides !=0 :
        t.forward(100)
        t.left(360//triangle)
        sides -= 1
# square
def square():
    t.color("blue")
    square = 4
    sides = 4
    while sides !=0 :
        t.forward(100)
        t.left(360//square)
        sides -= 1
# pentagon
def pentagon():
    t.color("green")
    pentagon = 5
    sides = 5
    while sides !=0 :
        t.forward(100)
        t.left(360//pentagon)
        sides -= 1
# hexagon
def hexagon():
    t.color("violet")
    hexagon = 6
    sides = 6
    while sides !=0 :
        t.forward(100)
        t.left(360//hexagon)
        sides -= 1
# heptagon
def heptagon():
    t.color("orange")
    heptagon = 7
    sides = 7
    while sides !=0 :
        t.forward(100)
        t.left(360//heptagon)
        sides -= 1
# octagon
def octagon():
    t.color("red")
    octagon = 8
    sides = 8
    while sides !=0 :
        t.forward(100)
        t.left(360//octagon)
        sides -= 1
# nonagon
def nonagon():
    t.color("green")
    nonagon = 9
    sides = 9
    while sides !=0 :
        t.forward(100)
        t.left(360//nonagon)
        sides -= 1
# decagon
def decagon():
    t.color("red")
    decagon = sides = 10
    while sides !=0 :
        t.forward(100)
        t.left(360//decagon)
        sides -= 1
def draw():
    triangle()
    square()
    pentagon()
    hexagon()
    heptagon()
    octagon()
    nonagon()
    decagon()

draw()
s.exitonclick()
