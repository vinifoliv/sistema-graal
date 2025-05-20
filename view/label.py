from tkinter import Label


class Etiqueta(Label):
    def __init__(self, text: str, master=None):
        super().__init__(
            master=master,
            text=text,
            bd=0,
            font=("Arial", 20, "bold"),
            fg="white",
            bg="#003095",
        )

    def texto(self, valor: str):
        self.config(text=valor)
