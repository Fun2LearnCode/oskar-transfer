import turtle
t = turtle.Pen()
turtle.bgcolor('black')
t.speed(0)
sides = eval(input("Enter the number of sides between 2 and 6: "))
colors = ['gray','white','gray','white','beige','white']
for x in range(400):
    t.pencolor(colors[x % sides])
    t.forward(x)
    t.left(360/sides)
