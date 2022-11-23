import tkinter as tk
from tkinter import messagebox
from RegisterPage import RegisterPage
from ToDo import ToDo


class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        border = tk.LabelFrame(self, text='Login', bd=10, font=("Arial", 20))
        border.pack(fill="both",expand="yes", padx=150, pady=150)

        username = tk.Label(border, text="Username", font=("Arial Bold", 15))
        username.place(x=50, y=20)
        username_text = tk.Entry(border, width=30, bd=5)
        username_text.place(x=180, y=20)

        password = tk.Label(border, text="Password", font=("Arial Bold", 15))
        password.place(x=50, y=80)
        password_text = tk.Entry(border, width=30, show='*', bd=5)
        password_text.place(x=180, y=80)

        def verify():
            try:
                with open("credential.txt", "r") as f:
                    info = f.readlines()
                    i = 0
                    for e in info:
                        u, p = e.split(",")
                        if u.strip() == username_text.get() and p.strip() == password_text.get():
                            controller.show_frame(ToDo)
                            i = 1
                            # break
                    if i == 0:
                        messagebox.showinfo("Error", "Incorrect username and password!!")
            except:
                messagebox.showinfo("Error", "Incorrect username and password!!")

        login_button = tk.Button(border, text="Login", font=("Arial", 15), command=verify)
        login_button.place(x=320, y=115)
        signup_button = tk.Button(border, text="Sign-Up", font=("Arial", 15), command=lambda: controller.show_frame(RegisterPage))
        signup_button.place(x=150, y=115)


