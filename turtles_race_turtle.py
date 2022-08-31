import turtle
from random import *
from turtle import *

penup()
goto(-140,140) #positioning the pen

for i in range(15): #loop for creating the lines labelled with nos.
    speed(10) #setting the speed
    write(i) #writing the int
    right(90) #90 degree
    forward(10)
    pendown() #ready to draw
    forward(150)
    penup() #not ready to draw
    backward(160)
    left(90)
    forward(20)

a = Turtle() #creating instance of turtle at 'a' variable #inheriting the variable
a.color('green')
a.shape('turtle')
a.penup()
a.goto(-160,100)
a.pendown()

b = Turtle()#creating instance of turtle at 'a' variable #inheriting the variable
b.color('red')
b.shape('turtle')
b.penup()
b.goto(-160,80)
b.pendown()

c = Turtle() #creating instance of turtle at 'a' variable #inheriting the variable
c.color('blue')
c.shape('turtle')
c.penup()
c.goto(-160,60)
c.pendown()

for turn in range(100): #loop for the race
    a.forward(randint(1,5))
    b.forward(randint(1,5))
    c.forward(randint(1,5))

turtle.done()

#turtle is a name of package
#Turtle is the name of class



