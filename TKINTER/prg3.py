from tkinter import *
def calc():
    weight=float(e2.get())
    height=float(e3.get())
    res.set(weight/height)
app=Tk()
app.title("BMI CALCULATOR")
frame=Frame(Tk)
frame.pack()
l1=Label(app,text="age")
l1.pack()
e1=Entry(app)
e1.pack()  
l2=Label(app,text="enter your weight in cm")
l2.pack()
e2=Entry(app)
e2.pack() 
l3=Label(app,text="enter your height in kg")
l3.pack()
e3=Entry(app)
e3.pack() 
btn=Button(app,text="calculator",command=calc)
btn.pack()
res=StringVar()
res.set("result")
l4=Label(app,textvariable=res)
l4.pack()
app.mainloop()

