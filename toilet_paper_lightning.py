import turtle
from turtle import Screen
import random
import math

wn = Screen()

rootwindow = wn.getcanvas().winfo_toplevel()
rootwindow.call('wm', 'attributes', '.', '-topmost', '1')

wn.bgcolor('white')  # Set the window background color
wn.title("Hello, Tess!")  # Set the window title

turtle.hideturtle()
turtle.colormode(255)
turtle.bgcolor('black')
turtle.pencolor(255, 255, 255)
turtle.pensize(2)
turtle.speed(0)
turtle.tracer(0)
turtle.up()
# left top
startX = -200
startY = -200
turtle.goto(startX, startY)
turtle.down()

for k in range(1):
    turns = 25
    randomlengths = []
    randomturnfactors = []
    randomforwardmovements = []
    randomturndirections = []
    startDegree = 0#random.randrange(0, 361)
    turtle.right(startDegree)
    turtle.forward(200)
    for i in range(turns):
        randomlengths.append(random.randrange(10, 40))
        randomturnfactors.append(random.randrange(45, 90))
        randomforwardmovements.append(random.randrange(40, 100))
        randomturndirections.append(random.randrange(1, 3))

    print(randomturndirections)
    for l in range(20):
        for i in range(turns):
                if i % 2 == 0:
                #if randomturndirections[i] % 2 == 0:
                    turtle.left(randomturnfactors[i])
                else:
                    turtle.right(randomturnfactors[i])
                turtle.forward(randomforwardmovements[i])

        turtle.up()
        startX += 3
        turtle.goto(startX, startY)
        turtle.setheading(360 - startDegree)
        turtle.down()

turtle.done()

wn.mainloop()