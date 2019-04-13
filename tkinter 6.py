from tkinter import*
import random
root=Tk()
canvas=Canvas(root,width=600,height=600)
canvas.pack()
def randomRectangle(width,height):
    x1=random.randrange(width)
    y1=random.randrange(height)
    x2=x1+random.randrange(width)
    y2=y1+random.randrange(height)
    canvas.create_rectangle(x1,y1,x2,y2)
for x in range(0,111112):
    randomRectangle(600,600)
