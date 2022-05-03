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
    for l in range(50):
        turtle.pencolor(l*4, l*4, l*4)
        for i in range(turns):
            for j in range(randomlengths[i]):
                    #if i % 2 == 0:
                    if randomturndirections[i] % 2 == 0:
                        turtle.left(randomturnfactors[i] * j)
                    else:
                        turtle.right(randomturnfactors[i] * j)
                    #if randomturndirections[i] % 2 == 0 and (l >= 1 and l < 19):
                    #    turtle.up()
                    turtle.forward(randomforwardmovements[i])
                    turtle.down()
                    
        turtle.up()
        startX += 6 * math.pow(math.e, -0.004 * math.pow(l - 25, 2))
        turtle.pensize(5-(6 * math.pow(math.e, -0.004 * math.pow(l - 25, 2)))/1.5)
        turtle.setheading(360-startDegree)
        turtle.goto(startX, startY)
        turtle.down()

turtle.done()

wn.mainloop()