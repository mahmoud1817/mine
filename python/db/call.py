from mysql.connector import *;from tkinter import * ;from tkinter import messagebox; Tk().geometry('0x0-10-0')
try:
    a = connect(
        host     = "localhost",
        user     = "mahmoud18",
        passwd   = "",
        # database = 'python'
    )
    c = a.cursor()
    c.execute("create database newpy")
    # c.callproc("folanen")
    # fetch ?
    
    # c.execute('drop database pytry')
    # c.execute('create table names(mahmoud varchar(30) , anas varchar(30))')
    # c.execute('show databases')
    # for i in c:
    #     print(i)
    # c.execute('insert into content values(1,"mahmoud")')
    # a.commit()
    # c.execute('select * from content')
    # messagebox.showinfo('',c.fetchone())
    
    
except Error as e:
    messagebox.showerror("error",e)