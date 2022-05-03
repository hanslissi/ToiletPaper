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
#left top
startX = 0
startXBuf = startX
startY = 200
startDegree = random.randrange(0, 361)
turtle.goto(startX, startY)
# face downwards
turtle.right(startDegree)
turtle.down()

# specific toiletPaper attributes
maxPulsatingWidth = 4
pulsatingFactor = 0.009 # the higher, the faster it pulsates

def calcNewPensize(index):
    return maxPulsatingWidth * math.sin(pulsatingFactor * index - (math.pi / 2)) + maxPulsatingWidth

for k in range(1):
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
    for l in range(10):
        for i in range(turns):
            for j in range(randomlengths[i]):
                    #if i % 2 == 0:
                    if randomturndirections[i] % 2 == 0:
                        turtle.left(randomturnfactors[i] * j)
                    else:
                        turtle.right(randomturnfactors[i] * j)
                    turtle.forward(randomforwardmovements[i])
                    turtle.pensize(calcNewPensize(i * j))
                    
        turtle.up()
        startX += maxPulsatingWidth * 3
        turtle.setheading(360-startDegree)
        turtle.goto(startX, startY)
        turtle.down()

turtle.done()

wn.mainloop()