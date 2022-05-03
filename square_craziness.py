import turtle

turtle.hideturtle()
turtle.colormode(255)
turtle.bgcolor('black')
turtle.pencolor(0, 0, 0)
turtle.pensize(3)
#turtle.delay(0)
turtle.tracer(0) # no drawing animation

turtle.up()
turtle.goto(-200, 0)
degreeOffset = 20
firstSquareSize = 100
squareCount = 100
colorIncreaseFactor = 255 / squareCount

turtle.down()

for i in range(squareCount):
    size = firstSquareSize + i * 4
    turtle.pencolor(i*colorIncreaseFactor, i*colorIncreaseFactor, i*colorIncreaseFactor)
    for j in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.up()
    newX = turtle.position()[0]
    if i >= squareCount / 2:
        newX -= ((squareCount/2) / (squareCount- i + 1))
    else:
        newX += ((squareCount/2) / (i + 1))
    turtle.goto(newX, turtle.position()[1] + i / 50)
    turtle.down()

turtle.done()