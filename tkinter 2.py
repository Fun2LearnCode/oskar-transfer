from tkinter import*
root = Tk()
pic = PhotoImage(file="New Piskel.png")
w1=Label(root,image=pic).pack(side="left")
words = "we can add images to tkinter module"
w2 = Label(root,text=words).pack(side="right")
root.mainloop()
