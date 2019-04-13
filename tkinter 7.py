from tkinter import*
root=Tk()
canvas=Canvas(root,width=600,height=600)
canvas.pack()
canvas.create_arc(40,40,300,200,extent=90,style=ARC)
