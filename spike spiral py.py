import turtle
t = turtle.Pen()
turtle.bgcolor('black')
t.speed(-9000)
sides = 6
colors = ['red','yelow','beige','yellow','red','orange','orange']
for x in range(10000000):
    t.pencolor(colors[x % sides])
    t.forward(x*3/sides + x)
    t.left(360/sides + 90)
