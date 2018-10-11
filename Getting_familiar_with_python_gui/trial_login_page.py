from tkinter import *

gui = Tk()
gui.geometry("400x400")
#make sure first is capital and second is not
gui.title("First title")
a = Label(gui ,text="username").grid(row=0,column = 0)
b = Label(gui ,text="password").grid(row=1,column=0)
e = Entry(gui).grid(row=0,column=1)
f = Entry(gui,show="**").grid(row=1,column=1)
c = Button(gui,text="LOGIN").grid(row=2,column=0)
gui.mainloop()