from tkinter import *
import tkinter as Tk
import sqlite3

window = Tk()



def save():
    site1 = link.get()
    pass1 = pasw.get()
    display.insert(END,"website :"+site1+"\n password:"+pass1)
    return site1,pass1

label = Label(window,text="Welcome to password manager")
label.grid(row=0,column=1)


link = StringVar()
enter=Label(window,text="Enter the website : ")
entry=Entry(window,textvariable=link)
enter.grid(row=2,column=0)
entry.grid(row=2,column=1)


pasw= StringVar()
prompt=Label(window,text="Enter the password : ")
password=Entry(window,textvariable=pasw)
prompt.grid(row=3,column=0)
password.grid(row=3,column=1)




save = Button(window,text="Save",command=save)
leave  = Button(window,text="Exit",command=window.destroy)
save.grid(row=5,column=0)
leave.grid(row=5,column=1)


#hope i find a better way to manage the passord the whole point is security

display=Text(window,height=5,width=30)
display.grid(row=7,column=1)
window.mainloop()

class DB:
    def connect(self):
        conn=sqlite3.connect('pass.db')
        cur=conn.cursor()
        cur.execute("CREATE TABLE  IF NOT EXISTS webbase(id INTEGER PRIMARY KEY,website text,password text)")
        conn.commit()
        conn.close()
    def insert(self,site1,pass1):
        conn=sqlite3.connect("pass.db")
        cur=conn.cursor()
        cur.execute("INSERT INTO webbase VALUES(NULL,?,?)",(site1,pass1))
        conn.commit()
        conn.close()

    def view(self):
        conn=sqlite3.connect("pass.db")
        cur=conn.cursor()
        cur.execute("SELECT * FROM webbase")
        rows=cur.fetchall()
        conn.close()
    def search(self,site1=""):
        conn=sqlite3.connect("pass.db")
        cur=conn.cursor()
        cur.execute("SELECT * FROM webbase WHERE site1=?",(site1,))
        rows=cur.fetchall()
        conn.close()

    def delete(self,site1):
        conn=sqlite3.connect("pass.db")
        cur=conn.cursor()
        cur.execute("DELETE FROM webbase WHERE id=?",(id,))
        conn.commit()
        conn.close()
    def update(self,site1):
        conn=sqlite3.connect("pass.db")
        cur=conn.cursor()
        cur.execute("UPDATE webbase SET pass1=?",(pass1,))
        conn.commit()
        conn.close()
site1 = link.get()
pass1 = pasw.get()
base=DB()
base.connect()
base.insert(site1,pass1)
print(base.view())
