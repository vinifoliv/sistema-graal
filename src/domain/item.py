class Item:
    def __init__(
        self,
        ean_produto: str,
        descricao: str,
        preco: float,
        quantidade: int,
        unidade: str,
    ):
        self._validar(preco, quantidade)

        self.ean_produto = ean_produto
        self.descricao = descricao
        self.preco = preco
        self.quantidade = quantidade
        self.unidade = unidade

    def _validar(self, preco: float, quantidade: int):
        if preco < 0:
            raise ValueError("O preço não pode ser negativo!")
        
        if quantidade < 0:
            raise ValueError("A quantidade não pode ser negativo!")
