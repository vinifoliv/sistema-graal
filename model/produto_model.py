from decimal import Decimal


class ProdutoModel:
    def __init__(self, ean_produto: str, descricao: str, preco: Decimal, unidade: str):
        self.ean_produto = ean_produto
        self.descricao = descricao
        self.preco = preco
        self.unidade = unidade
