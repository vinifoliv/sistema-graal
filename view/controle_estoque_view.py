from tkinter import *
from tkinter.ttk import Style, Treeview
from typing import Callable

from controller.produto_controller import ProdutoController


class ControleEstoqueView(Frame):
    def __init__(
        self,
        produto_controller: ProdutoController,
        master=None,
    ):
        super().__init__(master)
        self._produto_controller = produto_controller

        self._entry_config = {
            "bd": 0,
            "font": ("Arial", 20),
        }

        self._button_config = {
            "bd": 0,
            "font": ("Arial", 20),
            "fg": "white",
            "bg": "#b40022",
        }

        self._label_config = {
            "bd": 0,
            "font": ("Arial", 20, "bold"),
            "fg": "white",
            "bg": "#003095",
        }

        self._background()
        self._dados_produto()
        self._botoes()
        self._tabela_de_produtos()
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
        self._label(text="EAN", column=2, row=0)
        self._entry_ean_produto = Entry(self, **self._entry_config)
        self._entry_ean_produto.grid(
            column=3, row=0, columnspan=1, padx=10, pady=10, sticky="we"
        )

        self._label(text="PREÇO", column=4, row=0)
        self._entry_preco = Entry(self, **self._entry_config)
        self._entry_preco.grid(
            column=5, row=0, columnspan=1, padx=10, pady=10, sticky="we"
        )

        self._label(text="QUANTIDADE", column=6, row=0)
        self._entry_quantidade = Entry(self, **self._entry_config)
        self._entry_quantidade.grid(
            column=7, row=0, columnspan=1, padx=10, pady=10, sticky="we"
        )

        self._label(text="DESCRIÇÃO", column=2, row=1)
        self._entry_descricao = Entry(self, **self._entry_config)
        self._entry_descricao.grid(
            column=3, row=1, columnspan=3, padx=10, pady=10, sticky="we"
        )

        self._label(text="UNIDADE", column=6, row=1)
        self._entry_unidade = Entry(self, **self._entry_config)
        self._entry_unidade.grid(
            column=7, row=1, columnspan=1, padx=10, pady=10, sticky="we"
        )

    def _botoes(self):
        self._label(text="PESQUISA", column=0, row=3)
        self._entry(column=1, row=3)

        self._button(
            text="CADASTRAR", column=2, row=3, columnspan=2, command=self._cadastrar
        )
        self._button(
            text="ALTERAR", column=4, row=3, columnspan=2, command=self._alterar
        )
        self._button(
            text="EXCLUIR", column=6, row=3, columnspan=2, command=self._excluir
        )

    def _tabela_de_produtos(self):
        # ESTILIZAÇÃO DA TABELA
        style = Style(self)
        style.configure("Treeview", font=("Arial", 16))
        style.configure("Treeview.Heading", font=("Arial", 20, "bold"))

        produtos = self._produto_controller.buscar()

        colunas = ("EAN", "DESCRIÇÃO", "PREÇO", "QUANTIDADE", "UNIDADE")
        self._tabela = Treeview(self, columns=colunas, show="headings")

        for coluna in colunas:
            self._tabela.heading(coluna, text=coluna, anchor="center")
            self._tabela.column(coluna, anchor="center")

        for produto in produtos:
            
            self._tabela.insert(
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

        # SCROLLBAR
        scroll_y = Scrollbar(self._tabela, orient=VERTICAL, command=self._tabela.yview)
        self._tabela.configure(yscrollcommand=scroll_y.set)

        self._tabela.bind("<Double-1>", self._preencher_entries)
        self._tabela.grid(column=0, row=4, columnspan=8, rowspan=7, sticky="nsew")

    def _button(self, text: str, column: int, row: int, columnspan=1, command=Callable):
        Button(self, **self._button_config, text=text, command=command).grid(
            column=column, row=row, columnspan=columnspan, padx=5, pady=5, sticky="we"
        )

    def _entry(self, column: int, row: int, columnspan=1):
        Entry(self, **self._entry_config).grid(
            column=column, row=row, columnspan=columnspan, padx=10, pady=10, sticky="we"
        )

    def _label(self, text: str, column: int, row: int):
        Label(self, **self._label_config, text=text).grid(column=column, row=row)

    def _preencher_entries(self, _):
        item_selecionado = self._tabela.focus()
        if not item_selecionado:
            return

        produto = self._tabela.item(item_selecionado, "values")
        if not produto:
            return

        self._entry_ean_produto.delete(0, END)
        self._entry_ean_produto.insert(0, produto[0])

        self._entry_descricao.delete(0, END)
        self._entry_descricao.insert(0, produto[1])

        self._entry_preco.delete(0, END)
        self._entry_preco.insert(0, produto[2])

        self._entry_quantidade.delete(0, END)
        self._entry_quantidade.insert(0, produto[3])

        self._entry_unidade.delete(0, END)
        self._entry_unidade.insert(0, produto[4])

    def _cadastrar(self):
        ean_produto = self._entry_ean_produto.get()
        descricao = self._entry_descricao.get()
        preco = float(self._entry_preco.get())
        quantidade = int(self._entry_quantidade.get())
        unidade = self._entry_unidade.get()

        self._produto_controller.cadastrar(
            ean_produto, descricao, preco, quantidade, unidade
        )

        self._limpar_dados()

    def _alterar(self):
        ean_produto = self._entry_ean_produto.get()
        descricao = self._entry_descricao.get()
        preco = float(self._entry_preco.get())
        quantidade = int(self._entry_quantidade.get())
        unidade = self._entry_unidade.get()

        print(ean_produto, descricao, preco, quantidade, unidade)

        self._produto_controller.alterar(
            ean_produto, descricao, preco, quantidade, unidade
        )

        self._limpar_dados()

    def _excluir(self):
        ean_produto = self._entry_ean_produto.get()
        self._produto_controller.excluir(ean_produto)

        self._limpar_dados()

    def _limpar_dados(self):
        self._entry_ean_produto.delete(0, END)
        self._entry_preco.delete(0, END)
        self._entry_quantidade.delete(0, END)
        self._entry_descricao.delete(0, END)
        self._entry_unidade.delete(0, END)
