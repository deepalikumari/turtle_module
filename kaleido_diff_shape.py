import turtle
from itertools import cycle
colors = cycle(['red','orange','yellow','green','blue','purple','pink'])
def draw_shape(size,angle,shift,shape):
    turtle.pencolor(next(colors))
    next_shape = ''
    if shape == 'circle':
        turtle.circle(size)
        next_shape = 'square'
    elif shape == 'square':
        for i in range(4): #loop run 4 times for each side of sq
            turtle.forward(size * 2)
            turtle.left(90)
        next_shape = 'circle'
    turtle.right(angle) #turtle rotates
    turtle.forward(shift) #turtle move forwrd
    draw_shape(size + 5, angle + 1,shift +1, next_shape)

turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(4)
draw_shape(30, 0 ,1 , 'circle')