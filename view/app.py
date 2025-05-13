from tkinter import *
import tkinter as tk

from controller.produto_controller import ProdutoController
from view.caixa_eletronico_view import CaixaEletronicoView
from view.controle_estoque_view import ControleEstoqueView


class App:
    def __init__(self, produto_controller: ProdutoController):
        self._root = Tk()
        self._root.state("zoomed")
        self._controle_estoque = ControleEstoqueView(produto_controller, self._root)

    def executar(self):
        self._root.mainloop()
