import tkinter
from tkinter import*

def submit():
    d=str(e1.get())
    mn=str(e2.get())
    ml=str(e3.get())
    mul=str(e4.get())
    ls=str(e5.get())
    dt=str(e6.get())
    uls=str(e7.get())
    lno=str(e8.get())
    cn=str(e9.get())
f=open("summer.txt","w")

root=Tk()
# label
l=Label(root,text=" transport details",fg='red')
l.grid(row=0,column=1)

l1=Label(root,text="date(d/m/y)")
l1.grid(row=1,column=0)

l2=Label(root,text="material name")
l2.grid(row=2,column=0)

l3=Label(root,text="material quantity loaded")
l3.grid(row=3,column=0)

l4=Label(root,text="material quantity unloaded")
l4.grid(row=4,column=0)

l5=Label(root,text="loading station")
l5.grid(row=5,column=0)

l6=Label(root,text="delievery time")
l6.grid(row=6,column=0)

l7=Label(root,text="unloading station")
l7.grid(row=7,column=0)

l8=Label(root,text="loury no:(eg-mh 00 ab 0000)")
l8.grid(row=8,column=0)

l9=Label(root,text="company name")
l9.grid(row=9,column=0)

#entry

e1=Entry(root)
e1.grid(row=1,column=2)
e2=Entry(root)
e2.grid(row=2,column=2)
e3=Entry(root)
e3.grid(row=3,column=2)
e4=Entry(root)
e4.grid(row=4,column=2)
e5=Entry(root)
e5.grid(row=5,column=2)
e6=Entry(root)
e6.grid(row=6,column=2)
e7=Entry(root)
e7.grid(row=7,column=2)
e8=Entry(root)
e8.grid(row=8,column=2)
e9=Entry(root)
e9.grid(row=9,column=2)

#submit

b=Button(root,text="submit",command=submit)
b.grid(row=11,column=2)
root.mainloop()
