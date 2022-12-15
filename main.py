# CS5007
import csv

from Task import Task
from Application import Application

from datetime import datetime
from tkinter import *
from tkinter import ttk
import tkinter as tk

#all_task = []
all_task = ["No_Name", "No_Date", "Doing"]
all_Doing_task = {}
share_todo = []
share_doing = []
share_done = []
priority = []
#all_Doing_task = []
#all_Done_task = []
def enter_release_text_handler_entry(event):
    print("Text entered = " + event.widget.get())

def save_database(event):
    f = open("db1.txt", "a")
    data = str(event.widget.get())
    f.write(data + "\n")

def collect_taskName(event):
    all_task[0]= (str(event.widget.get()))

def collect_dueDate(event):
    all_task[1]= (str(event.widget.get()))

def collect_status(event):
    all_task[2]= (str(event.widget.get()))

def button_lambda_handler_updates(widget):
    print("confirmed "+ widget["text"])

def button_lambda_handler_priority(widget):
    print("confirmed "+ widget["text"])
    priority.append(True)

def combobox_handler(event):
    print(event.widget["text"] + " Selected = " + str(event.widget.get()))

def sort_doing(all_Doing_task, todo, doing, done, widget):
    listDate = []
    # Step 1: delete all tasks in Doing
    for key in all_Doing_task:
        listDate.append(key)
        frame = all_Doing_task[key][1]
        delete_frame(frame, "Doing", all_Doing_task[key][0], key)

    # Step 2: sort all tasks based on due date
    listDate.sort(key=lambda date: datetime.strptime(date, "%d-%m-%Y "))
    print(listDate)
    new_list_task = []
    for d in listDate:
        new_list_task = [all_Doing_task[d][0], d, "Doing"]
        print("print in all task")
        print()
        root = all_Doing_task[d][1]
        #all_task = new_list_task
        #print(all_task)
        createTask(widget, todo, doing, done, root, new_list_task, priority)
    # step 3: loop through list of sorted task to create new tasks in Doing


def createTask(widget, todo, doing, done, box, all_task, priority):
    temp = all_task[2]
    print("confirmed " + widget["text"] + " TASK CREATED")
    newTask = Task(all_task[0], all_task[1], all_task[2])
    print(newTask.getStatus())
    if all_task[2] == 'To Do':
        clmn = todo
        share_todo.append([all_task[0], all_task[1]])
    if all_task[2] == 'Doing':
        clmn = doing
        all_Doing_task[all_task[1]] = [all_task[0]]   # assign date key to name
        share_doing.append([all_task[0], all_task[1]])
    if all_task[2] == 'Done':
        clmn = done
        share_done.append([all_task[0], all_task[1]])

    if priority[-1] == False:
        color = "blue"
    else:
        color = "red"
    task_frame = Frame(clmn, highlightcolor=color, highlightbackground=color, highlightthickness=5)
    if all_task[2] == 'Doing':
        all_Doing_task[all_task[1]].append(task_frame)   # assign date key to task frame
    print(all_Doing_task)
    task_frame.pack()
    name_label = ttk.Label(task_frame)
    name_label["text"] = all_task[0]
    name_label.pack()
    date_label = ttk.Label(task_frame)
    date_label["text"] = all_task[1]
    date_label.pack()
    update_button = ttk.Button(task_frame, command=lambda: update_frame(name_label, date_label, temp, all_task[0], all_task[1]))
    update_button["text"] = "Update"
    update_button.pack()
    delete_button = ttk.Button(task_frame, command=lambda: delete_frame(task_frame, temp, all_task[0], all_task[1]))
    delete_button["text"] = "Delete"
    delete_button.pack()
    all_task = [all_task[0], all_task[1], "Doing"]
    box.destroy()
def add_task_button(todo_frame, doing_frame, done_frame):
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
    root.columnconfigure(2, weight=1)

    label1 = ttk.Label(root)
    label1["text"] = "TaskName: "
    label1.grid(row=0, column=0, sticky=tk.W)

    label2 = ttk.Label(root)
    label2["text"] = "DueDate (DD-MM-YYYY ): "
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

    radio_button3 = ttk.Radiobutton(root, value=2, variable=control, text="priority HIGH",
                                    command=lambda: button_lambda_handler_priority(radio_button3))

    radio_button2 = ttk.Radiobutton(root, value=1, variable=control, text="Done",
                                    command=lambda: createTask(radio_button2, todo_frame, doing_frame, done_frame, root, all_task, priority))

    priority.append(False)
    radio_button1.grid(row=3, column=0)
    radio_button2.grid(row=3, column=2)
    radio_button3.grid(row = 3, column = 1)

    text_field1.bind("<KeyRelease-Return>", enter_release_text_handler_entry)
    text_field1.bind("<KeyRelease-Return>", save_database, add='+')
    text_field1.bind("<KeyRelease-Return>", collect_taskName, add='+')

    text_field2.bind("<KeyRelease-Return>", enter_release_text_handler_entry)
    text_field2.bind("<KeyRelease-Return>", collect_dueDate, add='+')

    combo_box1 = ttk.Combobox(root)
    combo_box1.state(["readonly"])

    combo_box1["values"] = ["To Do", "Doing", "Done"]

    combo_box1.grid(row=2, column=1)

    combo_box1.bind("<<ComboboxSelected>>", combobox_handler)
    combo_box1.bind("<<ComboboxSelected>>", collect_status, add='+')



    root.mainloop()
def delete_frame(frame, clmn, name, date):
    if clmn == "To Do":
        share_todo.remove([name, date])
    if clmn == "Doing":
        share_doing.remove([name, date])
    if clmn == "Done":
        share_done.remove([name, date])
    frame.destroy()

def update_frame(name_label, date_label, clmn, name, date):
    update = Tk()
    update.title("UPDATE!")

    label1 = ttk.Label(update)
    label1["text"] = "TaskName: "
    label1.grid(row=0, column=0, sticky=tk.W)

    label2 = ttk.Label(update)
    label2["text"] = "DueDate: "
    label2.grid(row=1, column=0, sticky=tk.W)

    label3 = ttk.Label(update)
    label3["text"] = "Status: "
    label3.grid(row=2, column=0, sticky=tk.W)

    text_field1 = ttk.Entry(update)
    text_field1.grid(row=0, column=1)
    submit_1 = ttk.Button(update, command=lambda: update_entry(text_field1, name_label, 1, clmn, name, date))
    submit_1.grid(row=0, column=2)

    text_field2 = ttk.Entry(update)
    text_field2.grid(row=1, column=1)
    submit_2 = ttk.Button(update, command=lambda: update_entry(text_field2, date_label, 2, clmn, name, date))
    submit_2.grid(row=1, column=2)

    combo_box1 = ttk.Combobox(update)
    combo_box1.state(["readonly"])

    combo_box1["values"] = ["To Do", "Doing", "Done"]

    combo_box1.grid(row=2, column=1)

    combo_box1.bind("<<ComboboxSelected>>", combobox_handler)
    combo_box1.bind("<<ComboboxSelected>>", collect_status, add='+')


    update.mainloop()
def update_entry(event, label, num, clmn, name, date):
    label["text"] = event.get()
    if num == 1:
        if clmn == "To Do":
            share_todo.remove([name, date])
            share_todo.append([label["text"], date])
        if clmn == "Doing":
            share_doing.remove([name, date])
            share_doing.append([label["text"], date])
        if clmn == "Done":
            share_done.remove([name, date])
            share_done.append([label["text"], date])
    if num == 2:
        if clmn == "To Do":
            share_todo.remove([name, date])
            share_todo.append([name, label["text"]])
        if clmn == "Doing":
            share_doing.remove([name, date])
            share_doing.append([name, label["text"]])
        if clmn == "Done":
            share_done.remove([name, date])
            share_done.append([name, label["text"]])

def share_tasks():
    with open("output.csv", 'w') as f:
        wrtr = csv.writer(f)
        head = ["Status", "Name", "Date"]
        wrtr.writerow(head)
        for i in share_todo:
            temp = ["To Do", i[0], i[1]]
            wrtr.writerow(temp)
        for i in share_doing:
            temp = ["Doing", i[0], i[1]]
            wrtr.writerow(temp)
        for i in share_done:
            temp = ["Done", i[0], i[1]]
            wrtr.writerow(temp)

def main():
    f = open("db1.txt", "a")

    app = Tk()
    app.title("Application")
    app.resizable(width=True, height=True)

    app.geometry('600x800')

# format main frame
    app.rowconfigure(0, weight=1)
    app.rowconfigure(1, weight=1)
    app.rowconfigure(2, weight=10)


    app.columnconfigure(0, weight=1)
    app.columnconfigure(1, weight=1)
    app.columnconfigure(2, weight=1)

    row11 = Frame(app, highlightcolor="black", highlightbackground="black", highlightthickness=5)
    row11.grid(row=1, column=0, sticky=N + S + E + W)

    row12 = Frame(app, highlightcolor="black", highlightbackground="black", highlightthickness=5)
    row12.grid(row=1, column=1, sticky=N + S + E + W)

    row13 = Frame(app, highlightcolor="black", highlightbackground="black", highlightthickness=5)
    row13.grid(row=1, column=2, sticky=N + S + E + W)

    row21 = Frame(app, highlightcolor="cyan", highlightbackground="cyan", highlightthickness=5)
    row21.grid(row=2, column=0, sticky=N + S + E + W)

    row22 = Frame(app, highlightcolor="yellow", highlightbackground="yellow", highlightthickness=5)
    row22.grid(row=2, column=1, sticky=N + S + E + W)

    row23 = Frame(app, highlightcolor="red", highlightbackground="red", highlightthickness=5)
    row23.grid(row=2, column=2, sticky=N + S + E + W)

    label1 = ttk.Label(app)
    label1["text"] = "TO DO"
    label1.grid(row=1, column=0)

    sort_button = ttk.Button(app, command=lambda: sort_doing(all_Doing_task, todo_frame, doing_frame, done_frame, sort_button))
    sort_button["text"] = "Sort DOING"
    sort_button.grid(row=0, column=1)


    label2 = ttk.Label(app)
    label2["text"] = "DOING"
    label2.grid(row=1, column=1)

    label3 = ttk.Label(app)
    label3["text"] = "DONE"
    label3.grid(row=1, column=2)

    add_button = ttk.Button(app, command=lambda: add_task_button(todo_frame, doing_frame, done_frame))
    add_button["text"] = "Add Task"
    add_button.grid(row=0, column=2)

    share_button = ttk.Button(app, command=lambda: share_tasks())
    share_button["text"] = "Share"
    share_button.grid(row=0, column=0)

# format each task frame

    todo_frame = Frame(app, highlightcolor="pink", highlightbackground="pink", highlightthickness=5)
    todo_frame.grid(row=2, column=0)

    doing_frame = Frame(app, highlightcolor="pink", highlightbackground="pink", highlightthickness=5)
    doing_frame.grid(row=2, column=1)

    done_frame = Frame(app, highlightcolor="pink", highlightbackground="pink", highlightthickness=5)
    done_frame.grid(row=2, column=2)



    app.mainloop()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()