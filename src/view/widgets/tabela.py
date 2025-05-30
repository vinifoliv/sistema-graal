from tkinter import END, VERTICAL, Scrollbar
from tkinter.ttk import Style, Treeview
from typing import List

from domain.produto import Produto


class Tabela(Treeview):
    def __init__(self, preencher_entries, master=None):
        self._preencher_entries = preencher_entries
        self._colunas = ("EAN", "DESCRIÇÃO", "PREÇO", "QUANTIDADE", "UNIDADE")

        super().__init__(master, columns=self._colunas, show="headings")

        self._configurar_estilo()
        self._configurar_scrollbar()

        for coluna in self._colunas:
            self.heading(coluna, text=coluna, anchor="center")
            self.column(coluna, anchor="center")

        self.bind("<Double-1>", self._preencher_entries)

    def _configurar_estilo(self):
        self._style = Style(self.master)
        self._style.configure("Treeview", font=("Arial", 16))
        self._style.configure("Treeview.Heading", font=("Arial", 20, "bold"))

    def _configurar_scrollbar(self):
        self._scroll_y = Scrollbar(self, orient=VERTICAL, command=self.yview)
        self.configure(yscrollcommand=self._scroll_y.set)

    def listar_produtos(self, produtos: List[Produto]):
        for produto in self.get_children():
            self.delete(produto)

        for produto in produtos:
            self.insert(
                "",
                END,
                values=(
                    produto.ean_produto,
                    produto.descricao,
                    produto.preco,
                    produto.quantidade,
                    produto.unidade,
                ),
            )
