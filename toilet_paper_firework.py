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
turtle.pensize(5)
turtle.speed(0)
turtle.tracer(0)
turtle.up()
#left top
startX = 0
startY = 0
turtle.goto(startX, startY)
turtle.down()

for k in range(10):
    turns = k
    randomlengths = []
    randomturnfactors = []
    randomforwardmovements = []
    randomturndirections = []
    startDegree = random.randrange(0, 361)
    turtle.pencolor((200, 15, 12 * k))
    turtle.right(startDegree)
    for i in range(turns):
        randomlengths.append(random.randrange(10, 40))
        randomturnfactors.append(random.randrange(10, 30)/100.0)
        randomforwardmovements.append(random.randrange(2, 7))
        randomturndirections.append(random.randrange(1, 3))

    print(randomturndirections)
    for l in range(1):
        for i in range(turns):
            for j in range(randomlengths[i]):
                    #if i % 2 == 0:
                    if randomturndirections[i] % 2 == 0:
                        turtle.left(randomturnfactors[i] * j)
                    else:
                        turtle.right(randomturnfactors[i] * j)
                    turtle.forward(randomforwardmovements[i])
                    
        turtle.up()
        turtle.goto(startX, startY)
        turtle.down()

turtle.done()

wn.mainloop()