
from tkinter import *
import tkinter.messagebox as tm


class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.label_username = Label(self, text="Username")
        self.label_password = Label(self, text="Password")
        self.label_department = Label(self, text="Department")

        self.entry_username = Entry(self)
        self.entry_password = Entry(self, show="*")

        self.label_username.grid(row=0, column=0)
        self.label_password.grid(row=1, column=0)
        self.label_department.grid(row=2, column=0)
        self.entry_username.grid(row=0, column=1)
        self.entry_password.grid(row=1, column=1)

        variable = StringVar(master)
        variable.set("DCS")
        self.drop_down_box = OptionMenu(self,variable, "DCS", "IT", "HINDI", "B.Ed").grid(row=2,columnspan=8)

        self.checkbox = Checkbutton(self, text="Keep me logged in")
        self.checkbox.grid(columnspan=2)

        self.logbtn = Button(self, text="Login", command=self._login_btn_clicked)
        self.logbtn.grid(columnspan=2)

        self.pack()

    def _login_btn_clicked(self):
        # print("Clicked")
        username = self.entry_username.get()
        password = self.entry_password.get()

        # print(username, password)

        if username == "admin" and password == "admin@123":
            tm.showinfo("Login info", "Welcome Admin")
        else:
            tm.showerror("Login error", "Incorrect username")


root = Tk()
root.geometry("250x150")
lf = LoginFrame(root)
root.resizable(0, 0)
root.mainloop()
