from tkinter import Entry


class Input(Entry):
    def __init__(self, master=None):
        super().__init__(master=master, bd=0, font=("Arial", 20))
