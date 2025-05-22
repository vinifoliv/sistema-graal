from tkinter import END, Entry
from typing import Any


class Input(Entry):
    def __init__(self, master=None):
        super().__init__(master=master, bd=0, font=("Arial", 20))

    def texto(self, valor: Any):
        self.limpar()
        self.insert(0, valor)

    def limpar(self):
        self.delete(0, END)
