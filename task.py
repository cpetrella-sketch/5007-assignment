class Task:
    def __init__(self, taskName, dueDate, status):
        self.user = None
        self.taskName = taskName
        self.dueDate = dueDate
        self.status = status
        self.priority = None

    def getTaskName(self):
        return self.taskName

    def getDueDate(self):
        return self.dueDate

    def getStatus(self):
        return self.getStatus



