from tkinter import *
from typing import Callable

from controller.produto_controller import ProdutoController
from view.widgets.botao import Botao
from view.widgets.input import Input
from view.widgets.etiqueta import Etiqueta
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

        self.config(bg="#003095")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self._configurar_frame_logotipo()
        self._configurar_frame_produto()
        self._configurar_frame_tabela()

    def _configurar_frame_logotipo(self):
        self._frame_logotipo = Frame(self, bg="#000000")

        self._logotipo = PhotoImage(
            file="./src/static/logotipo.png", width=300, height=300
        )
        Label(self._frame_logotipo, image=self._logotipo, bd=0, bg="#003095").grid()

        self._frame_logotipo.grid(row=0, column=0)

    def _configurar_frame_produto(self):
        self._frame_produto = Frame(self, bg="gray")

        self._frame_produto.config(bg="#003095")
        self._frame_produto.grid_columnconfigure([0, 1, 2, 3], weight=1)
        self._frame_produto.grid_rowconfigure([0, 1, 2], weight=1)

        Etiqueta(text="EAN:", master=self._frame_produto).grid(
            column=0, row=0, sticky="we", padx=20, pady=20
        )
        self._entry_ean_produto = Input(self._frame_produto)
        self._entry_ean_produto.grid(
            column=1,
            row=0,
            sticky="we",
            padx=20,
            pady=20,
        )

        Etiqueta(text="PREÇO:", master=self._frame_produto).grid(
            column=2, row=0, sticky="we", padx=20, pady=20
        )
        self._entry_preco = Input(self._frame_produto)
        self._entry_preco.grid(
            column=3,
            row=0,
            sticky="we",
            padx=20,
            pady=20,
        )

        Etiqueta(text="DESCRIÇÃO:", master=self._frame_produto).grid(
            column=0, row=1, sticky="we", padx=20, pady=20
        )
        self._entry_descricao = Input(self._frame_produto)
        self._entry_descricao.grid(
            column=1, row=1, columnspan=3, padx=20, pady=20, sticky="we"
        )

        Etiqueta(text="QUANTIDADE:", master=self._frame_produto).grid(
            column=0, row=2, sticky="we", padx=20, pady=20
        )
        self._entry_quantidade = Input(self._frame_produto)
        self._entry_quantidade.grid(
            column=1,
            row=2,
            sticky="we",
            padx=20,
            pady=20,
        )

        Etiqueta(text="UNIDADE:", master=self._frame_produto).grid(
            column=2, row=2, sticky="we", padx=20, pady=20
        )
        self._entry_unidade = Input(self._frame_produto)
        self._entry_unidade.grid(
            column=3, row=2, columnspan=1, padx=20, pady=20, sticky="we"
        )

        self._frame_produto.grid(column=1, row=0, sticky="nsew")

    def _configurar_frame_tabela(self):
        self._frame_tabela = Frame(self)

        self._frame_tabela.config(bg="#003095")
        self._frame_tabela.grid_columnconfigure([0, 1, 2, 3, 4, 5], weight=1)
        self._frame_tabela.grid_rowconfigure(1, weight=1)

        Etiqueta(text="PESQUISA", master=self._frame_tabela, anchor="center").grid(
            column=0, row=0, sticky="we", padx=20, pady=20
        )
        self._entry_pesquisa = Input(self._frame_tabela)
        self._entry_pesquisa.grid(column=1, row=0, sticky="we", padx=20, pady=20)
        self._entry_pesquisa.bind("<KeyRelease>", lambda _: self._filtrar_produtos())

        Botao(
            text="CADASTRAR", command=self._cadastrar, master=self._frame_tabela
        ).grid(column=2, row=0, sticky="we", padx=20, pady=20)

        Botao(text="ALTERAR", command=self._alterar, master=self._frame_tabela).grid(
            column=3, row=0, sticky="we", padx=20, pady=20
        )

        Botao(text="EXCLUIR", command=self._excluir, master=self._frame_tabela).grid(
            column=4, row=0, sticky="we", padx=20, pady=20
        )

        Botao(
            text="CAIXA",
            command=lambda: self._mostrar_telas("caixa-eletronico"),
            master=self._frame_tabela,
        ).grid(column=5, row=0, sticky="we", padx=20, pady=20)

        self._tabela = Tabela(self._preencher_entries, self._frame_tabela)
        self._tabela.grid(
            column=0, columnspan=6, sticky="nsew", row=1, padx=20, pady=20
        )
        produtos = self._produto_controller.buscar()
        self._tabela.listar_produtos(produtos)

        self._frame_tabela.grid(column=0, columnspan=6, row=1, sticky="nsew")

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
