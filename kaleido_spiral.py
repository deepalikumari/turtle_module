import turtle
from itertools import cycle

colors = cycle(['red','orange','yellow','green','blue','purple','pink'])
def drawcircle(size,angle,shift):
    turtle.pencolor(next(colors))
    turtle.circle(size)
    turtle.right(angle) #clockwise
    turtle.forward(shift) #moves forward
    #drawcircle(size + 5, angle + 1, shift +1)
    #drawcircle(size + 10, angle + 10, shift +1)
    drawcircle(size + 5, angle - 20, shift -10)
turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(4)
drawcircle(30,0 ,1)
