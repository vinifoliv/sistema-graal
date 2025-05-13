from tkinter import Button
from typing import Callable


class Botao(Button):
    def __init__(self, text: str, command: Callable, master=None):
        super().__init__(
            master,
            text=text,
            command=command,
            bd=0,
            font=("Arial", 20),
            fg="white",
            bg="#b40022",
        )
