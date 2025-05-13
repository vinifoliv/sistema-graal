from tkinter import *

from view.button import Botao
from view.input import Input
from view.label import Etiqueta
from view.tabela import Tabela


class CaixaEletronicoView(Frame):
    def __init__(self, master: Tk = None):
        super().__init__(master, bg="Red")

        self._lista_de_itens()
        self._resumo_da_venda()
        self._dados_do_produto()
        self._botoes()
        self._background()

        self.pack(fill=BOTH, expand=True)

    def _lista_de_itens(self):
        self._tabela = Tabela(lambda: print("Hello, world!"), self)
        self._tabela.grid(column=0, columnspan=2, row=0, rowspan=8, sticky="nsew")
        # produtos = self._produto_controller.buscar()
        # self._tabela.listar_produtos(produtos)

    def _resumo_da_venda(self):
        Etiqueta(text="SUBTOTAL", master=self).grid(
            column=0, columnspan=2, row=8, sticky="we", padx=10, pady=10
        )
        self._entry_subtotal = Input(master=self)
        self._entry_subtotal.grid(
            column=0, columnspan=2, row=9, sticky="we", padx=10, pady=10
        )

        Etiqueta(text="TOTAL RECEBIDO", master=self).grid(
            column=0, row=10, sticky="we", padx=10, pady=10
        )
        self._entry_total_recebido = Input(master=self)
        self._entry_total_recebido.grid(column=0, row=11, sticky="we", padx=10, pady=10)

        Etiqueta(text="TROCO", master=self).grid(
            column=1, row=10, sticky="we", padx=10, pady=10
        )
        self._entry_subtotal = Input(self)
        self._entry_subtotal.grid(column=1, row=11, sticky="we", padx=10, pady=10)

    def _dados_do_produto(self):
        Etiqueta(text="EAN", master=self).grid(
            column=2, columnspan=3, row=3, sticky="we", padx=10, pady=10
        )
        self._ean_produto = Input(self)
        self._ean_produto.grid(
            column=2, columnspan=3, row=4, sticky="we", padx=10, pady=10
        )

        Etiqueta(text="Preço", master=self).grid(
            column=5, columnspan=3, row=3, sticky="we", padx=10, pady=10
        )
        self._entry_preco = Input(self)
        self._entry_preco.grid(
            column=5, columnspan=3, row=4, sticky="we", padx=10, pady=10
        )

        Etiqueta(text="DESCRIÇÃO", master=self).grid(
            column=2, columnspan=6, row=5, sticky="we", padx=10, pady=10
        )
        self._entry_descricao = Input(self)
        self._entry_descricao.grid(
            column=2, columnspan=6, row=6, sticky="we", padx=10, pady=10
        )

        Etiqueta(text="QUANTIDADE", master=self).grid(
            column=2, columnspan=3, row=7, sticky="we", padx=10, pady=10
        )
        self._entry_quantidade = Input(self)
        self._entry_quantidade.grid(
            column=2, columnspan=3, row=8, sticky="we", padx=10, pady=10
        )

        Etiqueta(text="UNIDADE", master=self).grid(
            column=5, columnspan=3, row=7, sticky="we", padx=10, pady=10
        )
        self._entry_unidade = Input(master=self)
        self._entry_unidade.grid(
            column=5, columnspan=3, row=8, sticky="we", padx=10, pady=10
        )

        Etiqueta(text="TOTAL DO ITEM", master=self).grid(
            column=2, columnspan=6, row=9, sticky="we", padx=10, pady=10
        )
        self._entry_total_do_item = Input(master=self)
        self._entry_total_do_item.grid(
            column=2, row=10, columnspan=6, sticky="we", padx=10, pady=10
        )

    def _botoes(self):
        Botao(text="CADASTRAR", command=self._cadastrar, master=self).grid(
            column=2, row=11, columnspan=2, sticky="we", padx=10, pady=10
        )
        Botao(text="CONSULTAR", command=self._consultar, master=self).grid(
            column=4, row=11, columnspan=2, sticky="we", padx=10, pady=10
        )
        Botao(text="FINALIZAR", command=self._finalizar, master=self).grid(
            column=6, row=11, columnspan=2, sticky="we", padx=10, pady=10
        )

    def _background(self):
        self.config(bg="#003095")
        self.config(padx=15, pady=15)

        self.logotipo = PhotoImage(file="./static/logotipo.png", width=300, height=300)
        Label(self, image=self.logotipo, bd=0, bg="#003095").grid(
            column=2, columnspan=6, row=0, rowspan=3, padx=10, pady=10, sticky="we"
        )

    def _cadastrar(self):
        pass

    def _consultar(self):
        pass

    def _finalizar(self):
        pass
