import time
from tkinter import*
root=Tk()
canvas=Canvas(root,width=500,height=500)
canvas.pack()
canvas.create_polygon(20,20,20,60,50,40)
for x in range(0,50):
    canvas.move(1,5,0)
    root.update()
    time.sleep(.1)
for x in range (0,50):
    canvas.move(1,-5,0)
    root.update()
    time.sleep(.1)
