answer = input("Do you want to see a spirtal? y/n:")
if answer == 'y':
    print("Great,i will draw one for you.")
    import turtle
    t = turtle.Pen()
    t.speed(0)
    for x in range(100):
        t.forward(x*2)
        t.left(95)
print("ok i'm done!") 
