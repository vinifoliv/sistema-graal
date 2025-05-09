from decimal import Decimal
from domain.produto import Produto
from model.produto_model import ProdutoModel


class ProdutoController:
    def __init__(self, produto_model: ProdutoModel):
        self._produto_model = produto_model

    def cadastrar(
        self,
        ean_produto: str,
        descricao: str,
        preco: float,
        quantidade: int,
        unidade: str,
    ):
        produto = Produto(ean_produto, descricao, Decimal(preco), quantidade, unidade)

        produto_existe = self._produto_model.buscar_por_descricao(produto.descricao)
        if produto_existe:
            raise ValueError("O produto já existe!")

        self._produto_model.cadastrar(produto)

    def alterar(
        self,
        ean_produto: str,
        descricao: str,
        preco: float,
        quantidade: int,
        unidade: str,
    ):
        produto = Produto(ean_produto, descricao, Decimal(preco), quantidade, unidade)

        produto_existe = self._produto_model.buscar_por_ean(produto.ean_produto)
        if not produto_existe:
            raise ValueError("O produto não existe!")

        self._produto_model.alterar(produto)

    def excluir(self, ean_produto: str):
        produto_existe = self._produto_model.buscar_por_ean(ean_produto)
        if not produto_existe:
            raise ValueError("O produto não existe!")

        self._produto_model.excluir(ean_produto)
