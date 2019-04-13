from tkinter import*
root=Tk()
def hi():
        print('you clicked the button!')
btn=Button(root,text="Click Here",command=hi)
btn.pack()
root.mainloop()
