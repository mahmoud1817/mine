from tkinter import *;from tkinter import messagebox;from tkinter.ttk import *
m = Tk() ; m.title('saving info') ; m.geometry('500x500+200+50');m.config(bg='#f6f6f6')

def s():
    if e1.get().strip()!="" and e3.get().strip()!="" and e3.get().strip()!="":
        messagebox.askyesno('confirmed','info saved\nwanna display it?')
    else: messagebox.showerror('hey you!','complete info')

l1 = Label(m,text='id',font=(24),padding=20) ; l1.grid(row=1,column=1)
l2 = Label(m,text='name',font=(24),padding=20) ; l2.grid(row=2,column=1)
l3 = Label(m,text='job',font=(24),padding=20) ; l3.grid(row=3,column=1)

e1 = Entry(m);e1.grid(row=1,column=3)
e2 = Entry(m);e2.grid(row=2,column=3)
e3 = Entry(m);e3.grid(row=3,column=3)

b1= Button(m,text="save",command=s) ; b1.grid(row=5,column=5)



m.mainloop()