from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
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
        gerar_caminho_imagem: Callable,
        master: Tk = None,
    ):
        super().__init__(master)
        self._produto_controller = produto_controller
        self._venda_controller = venda_controller
        self._gerar_caminho_imagem = gerar_caminho_imagem
        self._mostrar_tela = mostrar_tela

        self._itens_venda: List[Item] = []

        self.config(bg="#003095")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure([0, 1], weight=1)

        self._configurar_frame_venda()
        self._configurar_frame_produto()

    def _configurar_frame_venda(self):
        self._frame_venda = Frame(self, bg="#003095")
        self._frame_venda.grid(column=0, row=0, sticky="nsew")
        self._frame_venda.grid_columnconfigure([0, 1, 2, 3], weight=1)
        self._frame_venda.grid_rowconfigure(0, weight=1)

        self._tabela = Tabela(lambda: print(), self._frame_venda)
        self._tabela.grid(
            column=0, columnspan=4, row=0, sticky="nsew", padx=20, pady=20
        )

        Etiqueta(text="SUBTOTAL", master=self._frame_venda).grid(
            column=0, row=1, sticky="we", padx=20, pady=20
        )
        self._entry_subtotal = Input(master=self._frame_venda)
        self._entry_subtotal.grid(
            column=1, columnspan=3, row=1, sticky="we", padx=20, pady=20
        )

        Etiqueta(text="TOTAL RECEBIDO", master=self._frame_venda).grid(
            column=0, row=2, sticky="we", padx=20, pady=20
        )
        self._entry_total_recebido = Input(master=self._frame_venda)
        self._entry_total_recebido.grid(column=1, row=2, sticky="we", padx=20, pady=20)
        self._entry_total_recebido.bind(
            "<KeyRelease>", lambda _: self._atualizar_troco()
        )

        Etiqueta(text="TROCO", master=self._frame_venda).grid(
            column=2, row=2, sticky="we", padx=20, pady=20
        )
        self._entry_troco = Input(self._frame_venda)
        self._entry_troco.grid(column=3, row=2, sticky="we", padx=20, pady=20)

        self._atualizar_tabela()

    def _configurar_frame_produto(self):
        self._frame_produto = Frame(self, bg="#003095")

        self._frame_produto.grid(column=1, row=0, sticky="snew")
        self._frame_produto.grid_columnconfigure([0, 1, 2, 3], weight=1)
        self._frame_produto.grid_rowconfigure(0, weight=1)

        self.logotipo = PhotoImage(
            file=self._gerar_caminho_imagem("logotipo150x150.png"), width=150, height=150
        )
        Label(self._frame_produto, image=self.logotipo, bd=0, bg="#003095").grid(
            column=0, columnspan=4, row=0, sticky="snew", padx=20, pady=20
        )

        Etiqueta(text="FUNCIONÁRIO:", master=self._frame_produto).grid(
            column=0, columnspan=2, row=1, sticky="we", padx=20, pady=20
        )
        self._etiqueta_nome_funcionario = Etiqueta(text="", master=self._frame_produto)
        self._etiqueta_nome_funcionario.grid(
            column=2, columnspan=2, row=1, sticky="we", padx=20, pady=20
        )

        self._entry_codigo_funcionario = Input(self._frame_produto)
        self._entry_codigo_funcionario.grid(
            column=0, columnspan=4, row=2, sticky="we", padx=20, pady=20
        )
        self._entry_codigo_funcionario.bind(
            "<KeyRelease>", lambda _: self._atualizar_funcionario()
        )

        Etiqueta(text="EAN", master=self._frame_produto).grid(
            column=0, columnspan=2, row=3, sticky="we", padx=20, pady=20
        )
        self._entry_ean_produto = Input(self._frame_produto)
        self._entry_ean_produto.grid(
            column=0, columnspan=2, row=4, sticky="we", padx=20, pady=20
        )

        Etiqueta(text="PREÇO", master=self._frame_produto).grid(
            column=2, columnspan=2, row=3, sticky="we", padx=20, pady=20
        )
        self._entry_preco = Input(self._frame_produto)
        self._entry_preco.grid(
            column=2, columnspan=2, row=4, sticky="we", padx=20, pady=20
        )

        Etiqueta(text="DESCRIÇÃO", master=self._frame_produto).grid(
            column=0, columnspan=4, row=5, sticky="we", padx=20, pady=20
        )
        self._entry_descricao = Input(self._frame_produto)
        self._entry_descricao.grid(
            column=0, columnspan=4, row=6, sticky="we", padx=20, pady=20
        )

        Etiqueta(text="QUANTIDADE", master=self._frame_produto).grid(
            column=0, columnspan=2, row=7, sticky="we", padx=20, pady=20
        )
        self._entry_quantidade = Input(self._frame_produto)
        self._entry_quantidade.grid(
            column=0, columnspan=2, row=8, sticky="we", padx=20, pady=20
        )
        self._entry_quantidade.bind(
            "<KeyRelease>", lambda _: self._calcular_total_item()
        )

        Etiqueta(text="UNIDADE", master=self._frame_produto).grid(
            column=2, columnspan=2, row=7, sticky="we", padx=20, pady=20
        )
        self._entry_unidade = Input(master=self._frame_produto)
        self._entry_unidade.grid(
            column=2, columnspan=2, row=8, sticky="we", padx=20, pady=20
        )

        Etiqueta(text="TOTAL DO ITEM", master=self._frame_produto).grid(
            column=0, columnspan=4, row=9, sticky="we", padx=20, pady=20
        )
        self._entry_total_do_item = Input(master=self._frame_produto)
        self._entry_total_do_item.grid(
            column=0, row=10, columnspan=4, sticky="we", padx=20, pady=20
        )

        Botao(text="INCLUIR", command=self._incluir, master=self._frame_produto).grid(
            column=0, row=11, sticky="we", padx=20, pady=20
        )
        Botao(
            text="CONSULTAR", command=self._consultar, master=self._frame_produto
        ).grid(column=1, row=11, sticky="we", padx=20, pady=20)
        Botao(
            text="FINALIZAR", command=self._finalizar, master=self._frame_produto
        ).grid(column=2, row=11, sticky="we", padx=20, pady=20)
        Botao(
            text="ESTOQUE",
            command=lambda: self._mostrar_tela("controle-estoque"),
            master=self._frame_produto,
        ).grid(column=3, row=11, sticky="we", padx=20, pady=20)

    def _atualizar_funcionario(self):
        codigo_funcionario = self._entry_codigo_funcionario.get()
        funcionario = self._venda_controller.buscar_funcionario_por_codigo(
            codigo_funcionario
        )

        if not funcionario:
            self._etiqueta_nome_funcionario.limpar()
            return

        self._etiqueta_nome_funcionario.texto(funcionario.nome.upper())

    def _incluir(self):
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
            nome_cliente = simpledialog.askstring("Dados do cliente", "Nome:") or None

            self._venda_controller.cadastrar_venda(
                codigo_funcionario, nome_cliente, self._itens_venda
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
        total_item = round(quantidade * preco, 2)
        self._entry_total_do_item.texto(total_item)

    def _calcular_subtotal(self):
        subtotal = round(sum(item.preco * item.quantidade for item in self._itens_venda), 2)
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
        troco = round(max(total_recebido - subtotal, 0.0), 2)
        self._entry_troco.texto(troco)
