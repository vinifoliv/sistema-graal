from tkinter import *
from typing import Callable

from controller.produto_controller import ProdutoController
from view.widgets.button import Botao
from view.widgets.input import Input
from view.widgets.label import Etiqueta
from view.widgets.tabela import Tabela


class ControleEstoqueView(Frame):
    def __init__(
        self,
        produto_controller: ProdutoController,
        mostrar_telas: Callable,
        master=None,
    ):
        super().__init__(master)
        self._produto_controller = produto_controller
        self._mostrar_telas = mostrar_telas

        self._background()
        self._dados_produto()
        self._botoes()
        self._tabela_de_produtos()

    def _background(self):
        # Plano de fundo
        self.config(bg="#003095")
        self.config(padx=15, pady=15)

        # Logotipo
        self.logotipo = PhotoImage(file="./src/static/logotipo.png", width=300, height=300)
        Label(self, image=self.logotipo, bd=0).grid(
            column=0, row=0, columnspan=2, rowspan=2, padx=10, pady=10
        )

    def _dados_produto(self):
        Etiqueta(text="EAN", master=self).grid(
            column=2, row=0, sticky="we", padx=10, pady=10
        )
        self._entry_ean_produto = Input(self)
        self._entry_ean_produto.grid(
            column=3, row=0, columnspan=1, padx=10, pady=10, sticky="we"
        )

        Etiqueta(text="PREÇO", master=self).grid(
            column=4, row=0, sticky="we", padx=10, pady=10
        )
        self._entry_preco = Input(self)
        self._entry_preco.grid(
            column=5, row=0, columnspan=1, padx=10, pady=10, sticky="we"
        )

        Etiqueta(text="QUANTIDADE", master=self).grid(
            column=6, row=0, sticky="we", padx=10, pady=10
        )
        self._entry_quantidade = Input(self)
        self._entry_quantidade.grid(
            column=7, row=0, columnspan=1, padx=10, pady=10, sticky="we"
        )

        Etiqueta(text="DESCRIÇÃO", master=self).grid(
            column=2, row=1, sticky="we", padx=10, pady=10
        )
        self._entry_descricao = Input(self)
        self._entry_descricao.grid(
            column=3, row=1, columnspan=3, padx=10, pady=10, sticky="we"
        )

        Etiqueta(text="UNIDADE", master=self).grid(
            column=6, row=1, sticky="we", padx=10, pady=10
        )
        self._entry_unidade = Input(self)
        self._entry_unidade.grid(
            column=7, row=1, columnspan=1, padx=10, pady=10, sticky="we"
        )

    def _botoes(self):
        Etiqueta(text="PEQUISA", master=self).grid(
            column=0, row=3, sticky="we", padx=10, pady=10
        )
        self._entry_pesquisa = Input(self)
        self._entry_pesquisa.grid(column=1, row=3, padx=10, pady=10, sticky="we")
        self._entry_pesquisa.bind("<KeyRelease>", lambda _: self._filtrar_produtos())

        Botao(text="CADASTRAR", command=self._cadastrar, master=self).grid(
            column=2, row=3, sticky="we", padx=10, pady=10
        )

        Botao(text="ALTERAR", command=self._alterar, master=self).grid(
            column=3, row=3, sticky="we", padx=10, pady=10
        )

        Botao(text="EXCLUIR", command=self._excluir, master=self).grid(
            column=4, row=3, sticky="we", padx=10, pady=10
        )

        Botao(
            text="CAIXA",
            command=lambda: self._mostrar_telas("caixa-eletronico"),
            master=self,
        ).grid(column=5, row=3, sticky="we", padx=10, pady=10)

    def _tabela_de_produtos(self):
        self._tabela = Tabela(self._preencher_entries, self)
        self._tabela.grid(column=0, row=4, columnspan=8, rowspan=7, sticky="nsew")
        produtos = self._produto_controller.buscar()
        self._tabela.listar_produtos(produtos)

    def _filtrar_produtos(self):
        pesquisa = self._entry_pesquisa.get()

        produtos = []
        if pesquisa == "":
            produtos = self._produto_controller.buscar()
        else:
            produtos = self._produto_controller.filtrar_por_descricao(pesquisa)

        self._tabela.listar_produtos(produtos)

    def _preencher_entries(self, _):
        item_selecionado = self._tabela.focus()
        if not item_selecionado:
            return

        produto = self._tabela.item(item_selecionado, "values")
        if not produto:
            return

        self._entry_ean_produto.texto(produto[0])
        self._entry_descricao.texto(produto[1])
        self._entry_preco.texto(produto[2])
        self._entry_quantidade.texto(produto[3])
        self._entry_unidade.texto(produto[4])

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
        self._filtrar_produtos()

    def _alterar(self):
        ean_produto = self._entry_ean_produto.get()
        descricao = self._entry_descricao.get()
        preco = float(self._entry_preco.get())
        quantidade = int(self._entry_quantidade.get())
        unidade = self._entry_unidade.get()

        self._produto_controller.alterar(
            ean_produto, descricao, preco, quantidade, unidade
        )

        self._limpar_dados()

    def _excluir(self):
        ean_produto = self._entry_ean_produto.get()
        self._produto_controller.excluir(ean_produto)
        self._limpar_dados()

    def _limpar_dados(self):
        self._entry_ean_produto.limpar()
        self._entry_preco.limpar()
        self._entry_quantidade.limpar()
        self._entry_descricao.limpar()
        self._entry_unidade.limpar()
        self._filtrar_produtos()
