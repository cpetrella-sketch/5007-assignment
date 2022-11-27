# CS5007
from Task import Task
from Application import Application

from tkinter import *
from tkinter import ttk
import tkinter as tk

all_task = []

def enter_release_text_handler_entry(event):
    print("Text entered = " + event.widget.get())

def save_database(event):
    f = open("db1.txt", "a")
    data = str(event.widget.get())
    f.write(data + "\n")

def collect_taskName(event):
    print('WTF')
    all_task.append(str(event.widget.get()))

def collect_dueDate(event):
    all_task.append(str(event.widget.get()))

def collect_status(event):
    all_task.append(str(event.widget.get()))

def button_lambda_handler_updates(widget):
    print("confirmed "+ widget["text"])


def combobox_handler(event):
    print(event.widget["text"] + " Selected = " + str(event.widget.get()))

def createTask(widget, todo, doing, done):
    global all_task
    print("confirmed " + widget["text"] + " TASK CREATED")
    newTask = Task(all_task[0], all_task[1], all_task[2])
    print(newTask.getStatus())
    if all_task[2] == 'To Do':
        task_frame = Frame(todo, highlightcolor="blue", highlightbackground="blue", highlightthickness=5)
        task_frame.pack()
        name_label = ttk.Label(task_frame)
        name_label["text"] = all_task[0]
        name_label.pack()
        date_label = ttk.Label(task_frame)
        date_label["text"] = all_task[1]
        date_label.pack()
    if all_task[2] == 'Doing':
        task_frame = Frame(doing, highlightcolor="blue", highlightbackground="blue", highlightthickness=5)
        task_frame.pack()
        name_label = ttk.Label(task_frame)
        name_label["text"] = all_task[0]
        name_label.pack()
        date_label = ttk.Label(task_frame)
        date_label["text"] = all_task[1]
        date_label.pack()
    if all_task[2] == 'Done':
        task_frame = Frame(done, highlightcolor="blue", highlightbackground="blue", highlightthickness=5)
        task_frame.pack()
        name_label = ttk.Label(task_frame)
        name_label["text"] = all_task[0]
        name_label.pack()
        date_label = ttk.Label(task_frame)
        date_label["text"] = all_task[1]
        date_label.pack()
    all_task = []
def add_task_button(event):
    print("test")


def main():
    f = open("db1.txt", "a")

    app = Tk()
    app.title("Application")
    app.resizable(width=True, height=True)

    app.geometry('600x800')

    # limit max 5 tasks each column for application
    app.rowconfigure(0, weight=1)
    app.rowconfigure(1, weight=1)
    app.rowconfigure(2, weight=2)
    app.rowconfigure(3, weight=2)
    app.rowconfigure(4, weight=2)
    app.rowconfigure(5, weight=2)
    app.rowconfigure(6, weight=2)

    app.columnconfigure(0, weight=1)
    app.columnconfigure(1, weight=1)
    app.columnconfigure(2, weight=1)

    label1 = ttk.Label(app)
    label1["text"] = "TO DO"
    label1.grid(row=1, column=0)

    label2 = ttk.Label(app)
    label2["text"] = "DOING"
    label2.grid(row=1, column=1)

    label3 = ttk.Label(app)
    label3["text"] = "DONE"
    label3.grid(row=1, column=2)

    add_button = ttk.Button(app)
    add_button["text"] = "Add Task"
    add_button.grid(row=0, column=2)

    todo_frame = Frame(app, highlightcolor="pink", highlightbackground="pink", highlightthickness=5)
    todo_frame.grid(row=2, column=0)

    doing_frame = Frame(app, highlightcolor="pink", highlightbackground="pink", highlightthickness=5)
    doing_frame.grid(row=2, column=1)

    done_frame = Frame(app, highlightcolor="pink", highlightbackground="pink", highlightthickness=5)
    done_frame.grid(row=2, column=2)


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


    control = IntVar()
    radio_button1 = ttk.Radiobutton(root, value=0, variable=control, text="set Reminder",
                                    command=lambda: button_lambda_handler_updates(radio_button1))

    radio_button2 = ttk.Radiobutton(root, value=1, variable=control, text="Done",
                                    command=lambda: createTask(radio_button2, todo_frame, doing_frame, done_frame))


    radio_button1.grid(row=3, column=0)
    radio_button2.grid(row = 3, column = 1)

    text_field1.bind("<KeyRelease-Return>", enter_release_text_handler_entry)
    text_field1.bind("<KeyRelease-Return>", save_database, add = '+')
    text_field1.bind("<KeyRelease-Return>", collect_taskName, add = '+')

    text_field2.bind("<KeyRelease-Return>", enter_release_text_handler_entry)
    text_field2.bind("<KeyRelease-Return>", collect_dueDate, add='+')

    combo_box1 = ttk.Combobox(root)
    combo_box1.state(["readonly"])

    combo_box1["values"] = ["To Do", "Doing", "Done"]

    combo_box1.grid(row=2, column=1)

    combo_box1.bind("<<ComboboxSelected>>", combobox_handler)
    combo_box1.bind("<<ComboboxSelected>>", collect_status, add = '+')


    add_button.bind("<Button-1>", add_task_button)




    f.write('the hell\n')

    #print(all_task)

    root.mainloop()

    f.close()
    print(all_task)
    taskCard = Task(all_task[0], all_task[1], all_task[2])
    taskCard = Frame(app, highlightcolor="pink", highlightbackground="pink", highlightthickness=5)
    taskCard.grid(row=1, column=1, sticky=N + S + E + W)


    app.mainloop()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()