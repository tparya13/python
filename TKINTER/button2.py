from tkinter import*
root=Tk()
button1=Button(root,text="Login",bg="red",fg="white")
button1.pack(fill="x")
button2=Button(root,text="Login",bg="blue",fg="white")
button2.pack(fill="y",side="right")
button3=Button(root,text="Login",bg="green",fg="white")
button3.pack(fill="x",side="bottom")
button4=Button(root,text="Login",bg="yellow",fg="white")
button4.pack(fill="y",side="left")
root.mainloop()