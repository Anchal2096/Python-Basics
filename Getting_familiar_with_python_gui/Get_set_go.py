import tkinter as tk
from tkinter import ttk

win  = tk.Tk()

win.geometry("500x500")
win.resizable(0,0)
win.title("STUDENT MANAGEMENT SYSTEM")
ttk.Label(win,text = "NAME").grid(row= 0,column = 0)

win.mainloop()


