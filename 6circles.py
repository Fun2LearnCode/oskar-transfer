#6circles.py
import turtle
t = turtle.Pen()
t.speed(0)
circles = int(turtle.numinput("number of circles","how many circles would you like me to draw?",6))
for x in range(circles):
    t.pencolor('black')
    t.circle(x)
    t.pencolor('red')
    t.circle(2)
    t.pencolor('beige')
    t.circle(x)
    t.pencolor('blue')
    t.circle(4)
    t.left(360/circles)
    #t.right(x)
