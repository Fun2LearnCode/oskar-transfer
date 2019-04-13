#circleSpiral.py
import turtle
t = turtle.Pen()
t.speed(0)
circles = int(turtle.numinput("number of circles","how many circles would you like me to draw?",6))
for x in range(circles):
    t.circle(80)
    t.left(360/circles)
    t.right(x)
    
