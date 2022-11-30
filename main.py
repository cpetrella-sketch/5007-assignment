# CS5007
# <<<<<<< Updated upstream
from task import Task
# =======
from task import Task
from Application import Application
# >>>>>>> Stashed changes

from tkinter import *
from tkinter import ttk
import tkinter as tk

def enter_release_text_handler_entry(event):
    print("Text entered = " + event.widget.get())
    data = str(event.widget.get())
    return data

def button_lambda_handler_updates(widget):
    print("confirmed "+ widget["text"])
    data = widget["text"]
    return data

def combobox_handler(event):
    print(event.widget["text"] + " Selected = " + str(event.widget.get()))
    data = str(event.widget.get())
    return data

def main():
    root = Tk()
    root.title('Entry Box')
    root.resizable(width=True, height=True)
    # Put the main window in the center of the screen
    # Gets the requested values of the height and width.
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()

    # Gets both half the screen width/height and window width/height
    positionRight = int(root.winfo_screenwidth() / 2 - windowWidth / 2)
    positionDown = int(root.winfo_screenheight() / 2 - windowHeight / 2)

    # Positions the window in the center of the page.
    root.geometry("+{}+{}".format(positionRight, positionDown))
    # The geometry() method defines the width, height and coordinates of top left corner of the frame
    # as below (all values are in pixels): top.geometry("widthxheight+XPOS+YPOS")

    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=1)
    root.rowconfigure(3, weight=1)

    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)

    label1 = ttk.Label(root)
    label1["text"] = "TaskName: "
    label1.grid(row=0, column=0, sticky=tk.W)

    label2 = ttk.Label(root)
    label2["text"] = "DueDate: "
    label2.grid(row=1, column=0, sticky=tk.W)

    label3 = ttk.Label(root)
    label3["text"] = "Status: "
    label3.grid(row=2, column=0, sticky=tk.W)

    text_field1 = ttk.Entry(root)
    text_field1.grid(row=0, column=1)

    text_field2 = ttk.Entry(root)
    text_field2.grid(row=1, column=1)


    control = StringVar()
    radio_button1 = ttk.Radiobutton(root, value=1, variable=control, text="set Reminder",
                                    command=lambda: button_lambda_handler_updates(radio_button1))

    radio_button1.grid(row=3, column=1)

    name = text_field1.bind("<KeyRelease-Return>", enter_release_text_handler_entry)
    date = text_field2.bind("<KeyRelease-Return>", enter_release_text_handler_entry)


    combo_box1 = ttk.Combobox(root)
    combo_box1.state(["readonly"])

    combo_box1["values"] = ["To Do", "Doing", "Done"]
    combo_box1.current(0)

    combo_box1.grid(row=2, column=1)

    status = combo_box1.bind("<<ComboboxSelected>>", combobox_handler)


    root.mainloop()

    newTask = Task(name, date, status)

    print(type(newTask))
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()