from Application import Application
from tkinter import *
from tkinter import ttk
import tkinter as tk

class Task:
    def __init__(self, taskName, dueDate, status):
        self.user = None
        self.taskName = taskName
        self.dueDate = dueDate
        self.status = status
        self.priority = None

    #def addTasktoApp(self, app):

    #    taskCard = Frame(app, highlightcolor="pink", highlightbackground="pink", highlightthickness=5)
    #    taskCard.grid(row=1, column=1, sticky=N + S + E + W)




    def getTaskName(self):
        return self.taskName

    def getDueDate(self):
        return self.dueDate

    def getStatus(self):
        return self.status





