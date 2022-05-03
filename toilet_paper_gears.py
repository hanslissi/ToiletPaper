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
turtle.pencolor(0, 0, 0)
turtle.pensize(2)
turtle.speed(0)
turtle.tracer(0)
turtle.up()
# left top
startX = 0
startY = 0
turtle.goto(startX, startY)
turtle.down()

for k in range(1):
    turns = 10
    randomlengths = []
    randomturnfactors = []
    randomforwardmovements = []
    randomturndirections = []
    startDegree = random.randrange(0, 361)
    turtle.right(startDegree)
    for i in range(turns):
        randomlengths.append(random.randrange(10, 40))
        randomturnfactors.append(random.randrange(20, 100))
        randomforwardmovements.append(random.randrange(40, 100))
        randomturndirections.append(random.randrange(1, 3))

    print(randomturndirections)
    for l in range(10):
        turtle.pencolor(150 - l*10, l*10, l*15)
        for i in range(turns):
            if random.randrange(1, 5) == 1:
                turtle.up()  # skip one

            for j in range(randomlengths[i]):
                    # if i % 2 == 0:
                    if randomturndirections[i] % 2 == 0:
                        turtle.left(randomturnfactors[i])
                    else:
                        turtle.right(randomturnfactors[i])
                    turtle.forward(randomforwardmovements[i])

            # transition to next gear
            turtle.up()
            turtle.forward(randomforwardmovements[i] * 1.5)
            turtle.down()
        turtle.up()
        startX += 5
        turtle.goto(startX, startY)
        turtle.setheading(360 - startDegree)
        turtle.down()

turtle.done()

wn.mainloop()