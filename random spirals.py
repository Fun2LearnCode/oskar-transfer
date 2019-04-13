import random
import turtle
t=turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
colors=["blue","red","yellow","purple","green","orange"]
for s in range(50):
    t.pencolor(random.choice(colors))
    size=random.randint(20,50)
    x=random.randrange(-turtle.window_width()//2,turtle.window_width()//2)
    y=random.randrange(-turtle.window_height()//2,turtle.window_height()//2)
    t.penup()
    t.setpos(x,y)
    t.pendown()
    for z in range(size):
        t.forward(z)
        t.left(95)
