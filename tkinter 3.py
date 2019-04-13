from tkinter import*
root=Tk()
Label(root,text="Blue Text in Times Font",fg="blue",font="times").pack()
Label(root,text="Red Text in Helvetica Font",fg="red",bg="yellow",font="Helvetica 16 bold italic").pack()
Label(root,text="Purple Text in Verdana Bold",fg="purple",bg="green",font="Verdana 10 bold").pack()
root.mainloop()
