import turtle as t
from turtle import *

screen = t.Screen() #screen for o/p
speed(0)
t.hideturtle()

#initial penup()
t.penup()
t.goto(-200,125)
t.pendown()


#orange & white rectangle
t.color("orange")
t.begin_fill()
t.forward(400)
t.right(90)
t.forward(84)
t.right(90)
t.forward(400)
t.end_fill()
t.left(90)
t.forward(84)

#green rectangle
t.color("green")
t.begin_fill()
t.forward(84)
t.left(90)
t.forward(400)
t.left(90)
t.forward(84)
t.end_fill()

#big blue circle
t.penup()
t.goto(35,0)
t.pendown()
t.color("navy")
t.begin_fill()
t.circle(35)
t.end_fill()

#big white circle
t.penup()
t.goto(30,0)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(30)
t.end_fill()

#mini blue circle of flag
t.penup()
t.goto(-27,-4)
t.pendown()
t.color("navy")
for i in range(24):

    t.begin_fill()
    t.circle(2)
    t.end_fill()
    t.penup()
    t.forward(7)
    t.right(15)
    t.pendown()

#small blue circle
t.color("navy")
t.penup()
t.goto(10,0)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()

#the spokes of the flag
t.penup()
t.goto(0,0)
t.pendown()
t.pensize(1)
for i in range(24):
    t.forward(30)
    t.backward(30)
    t.left(15)


#for stick of flag
t.color("Brown")
t.pensize(10)
t.penup()
t.goto(-200,125)
t.right(180)
t.pendown()
t.forward(800)

#to hold the output window
t.done()




