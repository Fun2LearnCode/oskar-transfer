import turtle
t=turtle.Pen()
turtle.bgcolor('black')
t.speed(0)
sides=eval(input("Enter the number of sides between 2and6:"))
color=['blue','green','yellow','white','purple','orange']
for x in range(120):
    t.pencolor(color[x % sides])
    t.forward(x)
    t.left(360/sides)
    
