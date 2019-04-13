import turtle
import random
t = turtle.Pen()
t.speed(0)
t.hideturtle()
turtle.bgcolor("blue")
def draw_circle(x,y):
    t.penup()
    t.setpos(x,y)
    t.pendown
    t.pencolor("orange")
    t.fillcolor("orange")
    t.begin_fill()
    t.circle(40)
    t.end_fill()
for n in range(50):
    x = random.randrange(-turtle.window_width()//2, turtle.window_width()//2)
    y = random.randrange(-turtle.window_height()//2, turtle.window_height()//2)
    draw_circle(x,y)
