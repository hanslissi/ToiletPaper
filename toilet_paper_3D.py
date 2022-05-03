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
turtle.pencolor(0, 0, 0)
turtle.pensize(2)
turtle.speed(0)
turtle.tracer(0)
turtle.up()
# left top
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
    nIterations = 50
    for l in range(nIterations):
        turtle.pencolor(20 + l*4, 40 + l*2, 80)
        for i in range(turns):
            for j in range(randomlengths[i]):
                # if i % 2 == 0:
                if randomturndirections[i] % 2 == 0:
                    turtle.left(randomturnfactors[i] * j)
                else:
                    turtle.right(randomturnfactors[i] * j)
                turtle.forward(randomforwardmovements[i])
                turtle.down()

        turtle.up()
        startX += 1
        if l >= nIterations-2:
            print('yeet')
            startX = 0
            turtle.setheading(360-startDegree)
            turtle.goto(startX + 100, startY)
            turtle.down()
        else:
            turtle.setheading(360-startDegree)
            turtle.goto(startX, startY)
            turtle.down()


turtle.done()

wn.mainloop()
