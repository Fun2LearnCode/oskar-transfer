#fourcolorspiral.py
import turtle
t = turtle.Pen()
turtle.bgcolor('black')
t.speed(0)
colors =['red','orange','yellow','black','yellow','red']
for x in range(1000):
    t.pencolor( colors[x % 6])
    t.circle(100-x)
    t.left(95)
