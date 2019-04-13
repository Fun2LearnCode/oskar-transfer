import turtle
t=turtle.Pen()
t.speed(0)
turtle.bgcolor('black')
colors=['green','yellow','blue','red']
for x in range(100):
    t.pencolor(colors[x % 4])
    t.circle(x)
    t.left(95)
