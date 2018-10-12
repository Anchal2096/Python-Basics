from tkinter import *
import tkinter.messagebox as tm

name_field = StringVar
password_field = StringVar
gui = Tk()
# Main window properties
gui.geometry("360x125")
gui.title("First title")
gui.resizable(False, False)

# widgets in the main Window
username = Label(gui, text="username").grid(row=0, column=0)
password = Label(gui, text="password").grid(row=1, column=0)
name_field = Entry(gui, textvariable=name_field).grid(row=0, column=1)
password_field = Entry(gui, textvariable=password_field, show="**").grid(row=1, column=1)
checkbox = Checkbutton(gui, text="Keep me logged in").grid(columnspan=2)


print(type(name_field), type(password_field))

def login_btn_clicked():
    # print("Clicked")
    global name_field
    global password_field
    username_var = name_field.get()
    password_var = password_field.get()
    # print(type(username_var), type(password_var))
    print(username_var, password_var)

    if username_var == "admin" and password_var == "dcs@123":
        print("name is:" + type(name_field))
        tm.showinfo("Login info", "Welcome Admin")
    else:
        print("name is:" + type(name_field))
        tm.showerror("Login error", "Incorrect username")


command_button = Button(gui, text="login", command=login_btn_clicked).grid(row=3, column=1)
gui.mainloop()
