import turtle
t = turtle.pen()
turtle.bgcolor('black')
t.speed(0)
sides = 2
colors = ['blue','white']
for x in range(120):
    t.pencolor(colors[x % sides])
    t.forward(x)
    
