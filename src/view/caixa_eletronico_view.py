from tkinter import *
from tkinter import messagebox
from typing import Callable, List

from controller.produto_controller import ProdutoController
from controller.venda_controller import VendaController
from domain.item import Item
from domain.produto import Produto
from view.widgets.etiqueta import Etiqueta
from view.widgets.tabela import Tabela
from view.widgets.botao import Botao
from view.widgets.input import Input


class CaixaEletronicoView(Frame):
    def __init__(
        self,
        produto_controller: ProdutoController,
        venda_controller: VendaController,
        mostrar_tela: Callable,
        master: Tk = None,
    ):
        super().__init__(master, bg="Red")
        self._produto_controller = produto_controller
        self._venda_controller = venda_controller
        self._mostrar_tela = mostrar_tela

        self._itens_venda: List[Item] = []

        self._resumo_da_venda()
        self._dados_do_produto()
        self._botoes()
        self._lista_de_itens()
        self._background()

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def _lista_de_itens(self):
        self._tabela = Tabela(lambda: print("Hello, world!"), self)
        self._tabela.grid(column=0, columnspan=2, row=0, rowspan=8, sticky="nsew")
        self._atualizar_tabela()

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
        self._entry_total_recebido.bind(
            "<KeyRelease>", lambda _: self._atualizar_troco()
        )

        Etiqueta(text="TROCO", master=self).grid(
            column=1, row=10, sticky="we", padx=10, pady=10
        )
        self._entry_troco = Input(self)
        self._entry_troco.grid(column=1, row=11, sticky="we", padx=10, pady=10)

    def _dados_do_produto(self):
        Etiqueta(text="FUNCIONÁRIO:", master=self).grid(
            column=2, columnspan=3, row=1, sticky="we", padx=10, pady=10
        )
        self._etiqueta_nome_funcionario = Etiqueta(text="", master=self)
        self._etiqueta_nome_funcionario.grid(
            column=5, columnspan=3, row=1, sticky="we", padx=10, pady=10
        )

        self._entry_codigo_funcionario = Input(self)
        self._entry_codigo_funcionario.grid(
            column=2, columnspan=6, row=2, sticky="we", padx=10, pady=10
        )
        self._entry_codigo_funcionario.bind(
            "<KeyRelease>", lambda _: self._atualizar_funcionario()
        )

        Etiqueta(text="EAN", master=self).grid(
            column=2, columnspan=3, row=3, sticky="we", padx=10, pady=10
        )
        self._entry_ean_produto = Input(self)
        self._entry_ean_produto.grid(
            column=2, columnspan=3, row=4, sticky="we", padx=10, pady=10
        )

        Etiqueta(text="PREÇO", master=self).grid(
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
        self._entry_quantidade.bind(
            "<KeyRelease>", lambda _: self._calcular_total_item()
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
            column=2, row=11, sticky="we", padx=10, pady=10
        )
        Botao(text="CONSULTAR", command=self._consultar, master=self).grid(
            column=3, row=11, sticky="we", padx=10, pady=10
        )
        Botao(text="FINALIZAR", command=self._finalizar, master=self).grid(
            column=4, row=11, sticky="we", padx=10, pady=10
        )
        Botao(
            text="GESTÃO",
            command=lambda: self._mostrar_tela("controle-estoque"),
            master=self,
        ).grid(column=5, row=11, sticky="we", padx=10, pady=10)

    def _background(self):
        self.config(bg="#003095")
        self.config(padx=15, pady=15)

        self.logotipo = PhotoImage(
            file="./src/static/logotipo.png", width=300, height=300
        )
        Label(self, image=self.logotipo, bd=0, bg="#003095").grid(
            column=2, columnspan=6, row=0, padx=10, pady=10, sticky="we"
        )

    def _atualizar_funcionario(self):
        codigo_funcionario = self._entry_codigo_funcionario.get()
        funcionario = self._venda_controller.buscar_funcionario_por_codigo(
            codigo_funcionario
        )

        if not funcionario:
            self._etiqueta_nome_funcionario.limpar()
            return

        self._etiqueta_nome_funcionario.texto(funcionario.nome.upper())

    def _cadastrar(self):
        ean_produto = self._entry_ean_produto.get()
        descricao = self._entry_descricao.get()
        preco = float(self._entry_preco.get())
        quantidade = int(self._entry_quantidade.get())
        unidade = self._entry_unidade.get()

        novo_item = Item(ean_produto, descricao, preco, quantidade, unidade)

        self._itens_venda.append(novo_item)
        self._atualizar_tabela()
        self._limpar_dados_produtos()

    def _consultar(self):
        try:
            ean_produto = self._entry_ean_produto.get()
            produto = self._produto_controller.buscar_por_ean(ean_produto)
            self._preencher_dados_produto(produto)
        except ValueError as e:
            messagebox.showerror("Erro", e.args[0])
            self._limpar_dados_produtos()

    def _finalizar(self):
        try:
            codigo_funcionario = self._entry_codigo_funcionario.get()
            self._venda_controller.cadastrar_venda(
                codigo_funcionario, self._itens_venda
            )
            self._itens_venda.clear()
            self._atualizar_tabela()
        except ValueError as e:
            messagebox.showerror("Erro", e.args[0])

    def _calcular_total_item(self):
        quantidade = self._entry_quantidade.get()
        if not quantidade:
            self._entry_total_do_item.texto(0.0)
            return

        quantidade = int(quantidade)
        preco = float(self._entry_preco.get())
        total_item = quantidade * preco
        self._entry_total_do_item.texto(total_item)

    def _calcular_subtotal(self):
        subtotal = sum(item.preco * item.quantidade for item in self._itens_venda)
        return subtotal

    def _preencher_dados_produto(self, produto: Produto):
        self._entry_ean_produto.texto(produto.ean_produto)
        self._entry_descricao.texto(produto.descricao)
        self._entry_preco.texto(produto.preco)
        self._entry_unidade.texto(produto.unidade)

    def _limpar_dados_produtos(self):
        self._entry_ean_produto.limpar()
        self._entry_preco.limpar()
        self._entry_descricao.limpar()
        self._entry_quantidade.limpar()
        self._entry_unidade.limpar()
        self._entry_total_do_item.limpar()

    def _atualizar_tabela(self):
        self._tabela.listar_produtos(self._itens_venda)

        subtotal = self._calcular_subtotal()
        self._entry_subtotal.texto(subtotal)

        self._atualizar_troco()

    def _atualizar_troco(self):
        subtotal = self._calcular_subtotal()
        total_recebido = float(self._entry_total_recebido.get() or 0)
        troco = max(total_recebido - subtotal, 0.0)
        self._entry_troco.texto(troco)
