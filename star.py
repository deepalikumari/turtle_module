import turtle as t

from numpy import angle
size = 100
points = 7
angle = 180 - (180 / points)

t.color('yellow')
t.begin_fill()
for i in range(points):
    t.forward(size)
    t.right(angle)


t.end_fill()

#turtle lib used to create graphics,pic,games.
#It provides onscreen pen that we can use for drawing
