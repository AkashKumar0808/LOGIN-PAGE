from tkinter import *
from tkinter import messagebox
a=Tk()
lb1=Label(a,text="LOGIN PAGE",font=("aerialbold",25))
lb1.grid(row=0,column=1)
lb2=Label(a,text="USER NAME",font=("arialbold",15))
lb2.grid(row=1,column=0)
lb3=Label(a,text="PASSWORD",font=("arialbold",15))
lb3.grid(row=2,column=0)
e1=Entry(a,width=15)
e1.grid(row=1,column=1)
e2=Entry(a,width=15)
e2.grid(row=2,column=1)
def mrec():
    if e1.get()=="mrec" and e2.get()=="1234":
        messagebox.showinfo("","LoginDone")
    else:
        messagebox.showerror("","Invalid USER NAME or PASSWORD")
b1=Button(a,text="Login",command=mrec)
b1.grid(row=3,column=1)
a.mainloop()