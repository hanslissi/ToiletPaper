import turtle
from turtle import Screen
import random

wn = Screen()

rootwindow = wn.getcanvas().winfo_toplevel()
rootwindow.call('wm', 'attributes', '.', '-topmost', '1')

wn.bgcolor('white')  # Set the window background color
wn.title("Hello, Tess!")  # Set the window title

turtle.hideturtle()
turtle.colormode(255)
turtle.bgcolor('black')
turtle.pencolor(255, 255, 255)
turtle.pensize(4)
turtle.speed(0)
turtle.tracer(0)
turtle.up()
#left top
startX = 0
startXBuf = startX
startY = 200
startDegree = random.randrange(0, 361)
turtle.goto(startX, startY)
# face downwards
turtle.right(startDegree)
turtle.down()

for i in range(1):
    turns = 25
    randomlengths = []
    randomturnfactors = []
    randomforwardmovements = []
    randomturndirections = []
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

turtle.done()

wn.mainloop()