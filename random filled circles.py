import turtle
import random
t=turtle.Pen()
t.speed(0)
t.hideturtle()
turtle.bgcolor("black")
def draw_circle(x,y):
    t.penup()
    t.setpos(x,y)
    t.pendown()
    t.pencolor("red")
    t.fillcolor("red")
    t.begin_fill()
    t.circle(10)
    t.end_fill()
for n in range(70):
    x = random.randrange(-turtle.window_width()//2,turtle.window_width()//2)
    y = random.randrange(-turtle.window_height()//2,turtle.window_height()//2)
draw_circle(x,y)
