from tkinter import*
root=Tk()
canvas=Canvas(root,width=500,height=500)
canvas.pack()
canvas.create_polygon(20,20,120,40,150,200,120,180,70,80,fill="orange",outline="blue")
