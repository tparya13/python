from tkinter import*
from tkinter import messagebox
root=Tk()
l1=Label(root,text="enter first number")
e1=Entry(root)
l1.pack()
e1.pack()
l2=Label(root,text="enter second number")
e2=Entry(root)
l2.pack()
e2.pack()
def asd():
    button=Button(root,text="add")
    button.pack()
    button=Button(root,text="quit")
    button.pack()
    label=Label(root,text="result")
    label.pack()
root.mainloop()
