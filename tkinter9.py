from tkinter import*
root=Tk()
canvas=Canvas(root,width=500,height=500)
canvas.pack()
canvas.create_polygon(20,20,150,20,150,200,fill="blue",outline="black")
