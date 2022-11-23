import tkinter as tk
from tkinter import messagebox


class RegisterPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        border = tk.LabelFrame(self, text='Login', bd=10, font=("Arial", 20))
        border.pack(fill="both", expand="yes", padx=120, pady=120)

        username = tk.Label(border, text="Username:", font=("Arial", 15), )
        username.place(x=10, y=10)
        username_text = tk.Entry(border, width=30, bd=5)
        username_text.place(x=200, y=10)

        password = tk.Label(border, text="Password:", font=("Arial", 15), )
        password.place(x=10, y=60)
        password_text = tk.Entry(border, width=30, show="*", bd=5)
        password_text.place(x=200, y=60)

        l3 = tk.Label(border, text="Confirm Password:", font=("Arial", 15), )
        l3.place(x=10, y=110)
        t3 = tk.Entry(border, width=30, show="*", bd=5)
        t3.place(x=200, y=110)

        def check():
            if username_text.get() != "" or password_text.get() != "" or t3.get() != "":
                if password_text.get() == t3.get():
                    with open("credential.txt", "a") as f:
                        f.write(username_text.get() + "," + password_text.get() + "\n")
                        messagebox.showinfo("Welcome", "You are registered successfully!!")
                else:
                    messagebox.showinfo("Error", "Your password didn't get match!!")
            else:
                messagebox.showinfo("Error", "Please fill the complete field!!")

        signup_button = tk.Button(border, text="Sign Up", font=("Arial", 15), command=check)
        signup_button.place(x=170, y=150)


