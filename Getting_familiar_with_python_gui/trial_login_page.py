from tkinter import *

gui = Tk()
# Main window properties
gui.geometry("400x400")
gui.title("First title")
gui.resizable(False, False)

# widgets in the main Window
username = Label(gui, text="username").grid(row=0, column=0)
password = Label(gui, text="password").grid(row=1, column=0)
name_field = Entry(gui).grid(row=0, column=1)
password_field = Entry(gui, show="*").grid(row=1, column=1)
submit_button = Button(gui, text="LOGIN").grid(row=2, column=0)

gui.mainloop()
