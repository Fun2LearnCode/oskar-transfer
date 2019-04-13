import turtle
t = turtle.Pen()
colors = ['red','yellow']
for x in range(9000):
    t.forward(x)
    t.left(124)
    t.pencolor( colors[x % 2])
    t.speed(-300000000000000000000000000000000000000000000000000000000000000000)
