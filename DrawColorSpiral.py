import turtle
t = turtle.Pen()
turtle.bgcolor('black')
t.speed(0)
colors = ['red',' pink','purple','blue','silver']
for x in range(5):
    for y in range(5):
        t.pencolor(colors[y%5])
        t.forward(100)
        t.left(72)
    t.right(72)
    




