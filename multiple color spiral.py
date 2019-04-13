
import turtle
t = turtle.Pen()
turtle.bgcolor('black')
t.speed(0)
sides = 4
colors =['red','orange','yellow','green','blue','purple']
for x in range(300):
    t.pencolor( colors[x % sides])
    t.forward(x)
    t.left(90)
