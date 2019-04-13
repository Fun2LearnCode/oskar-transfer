from tkinter import*
root=Tk()
canvas=Canvas(root,width=600,height=600)
canvas.pack()
canvas.create_text(200,200,text="Austin is the capital of Texas." ,fill="purple",font=('Times',24))
