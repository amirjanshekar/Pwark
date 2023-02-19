from tkinter import *
from tkinter import messagebox
from Controllers.login_controller import LoginController
from View.MainPage.main_page import MainMenu


class Login(Tk):
    def __init__(self, connection):
        super().__init__()

        self.connection = connection

        self.geometry("500x350")
        self.config(background="black")

        self.login_frame = Frame(self)
        self.login_frame.config(background='black')
        self.login_frame.place(relx=0.5, rely=0.5, anchor='center')

        self.username_label = Label(self.login_frame, font=('default', 20), text='Username', bg="black", fg='white')
        self.username_label.grid(row=0, column=0, padx=5)

        self.username_entry = Entry(self.login_frame, font=("default", 20), width=20)
        self.username_entry.grid(row=0, column=1)

        self.password_label = Label(self.login_frame, font=('default', 20), text='Password', bg="black", fg='white')
        self.password_label.grid(row=1, column=0, padx=5)

        self.password_entry = Entry(self.login_frame, font=("default", 20), width=20)
        self.password_entry.config(show='*')
        self.password_entry.grid(row=1, column=1, pady=30)

        self.login_button = Button(self, text='Login', font=('default', 16), width=12, bg='white', fg='black',
                                   command=self.login)
        self.login_button.place(relx=0.5, rely=0.8, anchor='center')

    def login(self):
        res = LoginController.login(self.connection, self.username_entry.get(), self.password_entry.get())
        match res['status']:
            case 401:
                messagebox.showerror(title="Login Error", message=res['message'])
            case 200:
                messagebox_result = messagebox.showinfo(title="Login successful", message=res['message'])
                if messagebox_result == 'ok':
                    self.destroy()
                    app = MainMenu(self.connection)
                    app.mainloop()
