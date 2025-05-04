from tkinter import *


class ControleEstoqueView(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.entry_config = {
            "bd": 0,
            "font": ("Arial", 30),
        }

        self._button_config = {
            "bd": 0,
            "font": ("Arial", 30),
            "fg": "white",
            "bg": "#b40022"
        }

        self._background()
        self._dados_produto()
        self._botoes()
        self.pack(fill=BOTH, expand=True)

    def _background(self):
        # Plano de fundo
        self.config(bg="#003095")
        self.config(padx=15, pady=15)

        # Logotipo
        self.logotipo = PhotoImage(file="./static/logotipo.png", width=300, height=300)
        Label(self, image=self.logotipo, bd=0).grid(
            column=0, row=0, columnspan=2, rowspan=2, padx=10, pady=10
        )

    def _dados_produto(self):
        Entry(self, **self.entry_config).grid(column=2, row=0, padx=10, pady=10)
        Entry(self, **self.entry_config).grid(column=3, row=0, padx=10, pady=10)
        Entry(self, **self.entry_config).grid(column=4, row=0, padx=10, pady=10)
        Entry(self, **self.entry_config).grid(
            column=2, row=1, columnspan=3, padx=10, pady=10, sticky="we"
        )

    def _botoes(self):
        Entry(self, **self.entry_config).grid(
            column=0, columnspan=3, row=3, padx=10, pady=10, sticky="we"
        )
        Button(self, **self._button_config, text="Cadastrar").grid(column=3, row=3, padx=10, pady=10)
        Button(self, **self._button_config, text="Alterar").grid(column=4, row=3, padx=10, pady=10)
        Button(self, **self._button_config, text="Excluir").grid(column=5, row=3, padx=10, pady=10)
