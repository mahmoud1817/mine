from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
f = Tk()
f.title("أرشيف")
w = f.winfo_screenwidth()
h = f.winfo_screenheight()
f.geometry(f"600x700+{int(w/2-300)}+{int(h/2-400)}") 
f.resizable(True,True)
f.minsize(300,350)
f.maxsize(w,h)
f.config(background="#eee")

def mb():
    messagebox.showwarning('hey dear','take care')
    print(e.get())
    print(c.get())
    print(l.get(ACTIVE))
    print(r.get())

Style().configure('TButton',fg="blue")
Style().configure('TLabel',fg="green")
Label(f,text="hey bro",style='TLabel').pack()
#config font('impact',20) padding(1,2,3,4)
e=Entry(f);e.pack()
c=Combobox(f,values=('mahmoud','anas','yusef'));c.pack()
l=Listbox(f);l.insert(0,"mahmoud");l.insert(1,"anas");l.insert(2,'yusef');l.pack()
r=StringVar()
r1=Radiobutton(f,text="mahmoud",value="mahmoud",variable=r);r1.pack()
r2=Radiobutton(f,text='ali',value="ali",variable=r);r2.pack()
Button(f,style='TButton',text="hit",command=mb).pack()



f.mainloop()