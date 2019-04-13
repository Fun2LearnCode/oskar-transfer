import turtle
t = turtle.Pen()
t.speed(-999999999999999999)
number = int(turtle.numinput("Number of sides circles","How many sides or circles should I draw?",8))
shape = turtle.textinput("What Should I draw?","Enter 'p' for a polygon or 'c' for circles:")
for x in range(number):
    if shape == 'c':
        t.circle(666)
    else:
        t.forward(x/2)
        #t.right(6)
        #t.circle(80)
    t.left(360/number)
