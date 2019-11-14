from tkinter import *

window = Tk()

def km_to_miles():
    print(e_value.get())
    miles=float(e_value.get())*1.6
    t.insert(END,miles)
    

b= Button(window,text="Execute",command=km_to_miles)
b.grid(row=0,column=0)


e_value=StringVar()
e=Entry(window,textvariable=e_value)
e.grid(row=1,column=0)



t = Text(window,height=2,width=30)
t.grid(row=2,column=0)

window.mainloop()
