from tkinter import*
root=Tk()
canvas=Canvas(root,width=500,height=500)
canvas.pack()
canvas.create_arc(20,20,300,200,extent=40,style=ARC)
canvas.create_arc(20,100,300,240,extent=90,style=ARC)
canvas.create_arc(20,180,300,290,extent=130,style=ARC)
canvas.create_arc(20,240,300,320,extent=180,style=ARC)
canvas.create_arc(20,310,300,380,extent=359,style=ARC)
