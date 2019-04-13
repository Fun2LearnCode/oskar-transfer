import turtle
t = turtle.Pen()
t.speed(0)
number = int(turtle.numinput("Number of sides","How many sides for the spiral should I draw?",8))
#= turtle.textinput("What Should I draw?","Enter 'p' for a polygon or 'c' for circles:")
for x in range(111):
    t.left(360/number)
    t.penup()
    t.forward(x)
    t.pendown()
    if (x % 2 == 0):
        for y in range(number):
            t.circle(1/5*2+9/(x+1))
            t.right(360/number)
    else:
        for y in range(number):
            t.forward(1/5*2+9/(x+1))
            t.right(360/number)
