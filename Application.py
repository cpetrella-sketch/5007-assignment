import tkinter as tk
from LoginPage import LoginPage
from RegisterPage import RegisterPage
from ToDo import ToDo


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a window
        window = tk.Frame(self)
        window.pack()

        window.grid_rowconfigure(0, minsize=600)
        window.grid_columnconfigure(0, minsize=900)

        self.frames = {}
        for element in (LoginPage, RegisterPage, ToDo):
            frame = element(window, self)
            self.frames[element] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LoginPage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title("Workflow Application")


app = Application()
app.maxsize(1000, 600)
app.mainloop()



