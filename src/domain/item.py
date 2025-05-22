class Item:
    def __init__(
        self,
        ean_produto: str,
        descricao: str,
        preco: float,
        quantidade: int,
        unidade: str,
    ):
        self.ean_produto = ean_produto
        self.descricao = descricao
        self.preco = preco
        self.quantidade = quantidade
        self.unidade = unidade
