from tkinter import *


class CaixaEletronicoView(Frame):
    def __init__(self, master: Tk = None):
        super().__init__(master, bg="Red")
        # Label(self, text="Caixa Eletronico").pack()
        self.pack()

    def executar(self):
        self.mainloop()
