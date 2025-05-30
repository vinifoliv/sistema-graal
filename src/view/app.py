from tkinter import *

from controller.produto_controller import ProdutoController
from controller.venda_controller import VendaController
from view.caixa_eletronico_view import CaixaEletronicoView
from view.controle_estoque_view import ControleEstoqueView


class App:
    def __init__(
        self, produto_controller: ProdutoController, venda_controller: VendaController
    ):
        self._root = Tk()
        self._root.title("Sistema Graal")
        self._root.state("zoomed")
        self._configurar_tela(self._root)

        self._telas = {
            "caixa-eletronico": CaixaEletronicoView(
                produto_controller,
                venda_controller,
                self._mostrar_tela,
                self._root,
            ),
            "controle-estoque": ControleEstoqueView(
                produto_controller,
                self._mostrar_tela,
                self._root,
            ),
        }

        for frame in self._telas.values():
            frame.grid(column=0, row=0, sticky="nsew")
            self._configurar_tela(frame)

        self._mostrar_tela("caixa-eletronico")

    def executar(self):
        self._root.mainloop()

    def _configurar_tela(self, tela: Widget):
        tela.grid_rowconfigure(0, weight=1)
        tela.grid_columnconfigure(0, weight=1)

    def _mostrar_tela(self, nome_tela: str):
        frame = self._telas[nome_tela]
        frame.tkraise()
