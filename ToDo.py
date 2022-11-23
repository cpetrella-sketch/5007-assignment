
import tkinter as tk


class ToDo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        first_frame = tk.Frame(self, width=200, height=500)
        first_frame.grid(row=0, column=0, padx=22, pady=22, ipadx=22, ipady=22)
        first_label = tk.LabelFrame(first_frame, text="To Do", width=200, height=500)
        first_label.pack(expand=True, fill="both")

        second_frame = tk.Frame(self, width=200, height=500)
        second_frame.grid(row=0, column=1, padx=22, pady=22, ipadx=22, ipady=22)
        second_label = tk.LabelFrame(second_frame, text="Doing", width=200, height=500)
        second_label.pack(expand=True, fill="both")

        third_frame = tk.Frame(self, width=200, height=500)
        third_frame.grid(row=0, column=3, padx=22, pady=22, ipadx=22, ipady=22)
        third_label = tk.LabelFrame(third_frame, text="Done", width=200, height=500)
        third_label.pack(expand=True, fill="both")

        login_button = tk.Button(self, text="AddTask", font=("Arial", 15))
        login_button.grid(row=0, column=4, padx=22)

