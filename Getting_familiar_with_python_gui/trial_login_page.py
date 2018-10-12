from tkinter import *
import tkinter.messagebox as tm

gui = Tk()
# Main window properties
gui.geometry("360x125")
gui.title("First title")
gui.resizable(False, False)

# widgets in the main Window
username = Label(gui, text="username").grid(row=0, column=0)
password = Label(gui, text="password").grid(row=1, column=0)
name_field = Entry(gui).grid(row=0, column=1)
password_field = Entry(gui, show="**").grid(row=1, column=1)
checkbox = Checkbutton(gui, text="Keep me logged in").grid(columnspan=2)


def _login_btn_clicked():
    # print("Clicked")
   # username_var = name_field.get()
   # password_var = password_field.get()

    # print(username, password)

    if name_field.get == "admin" and password_field.get == "dcs@123":
        tm.showinfo("Login info", "Welcome Admin")
    else:
        tm.showerror("Login error", "Incorrect username")


command_button = Button(gui, text="login", command=_login_btn_clicked).grid(row=3, column=1)
gui.mainloop()
