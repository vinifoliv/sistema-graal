class Produto:
    def __init__(
        self,
        ean_produto: str,
        descricao: str,
        preco: float,
        quantidade: int,
        unidade: str,
    ):
        self._validar(ean_produto, preco, quantidade)

        self.ean_produto = ean_produto
        self.descricao = descricao
        self.preco = preco
        self.quantidade = quantidade
        self.unidade = unidade

    def _validar(self, ean_produto: str, preco: float, quantidade: int):
        if len(ean_produto) != 13:
            raise ValueError("O EAN deve conter 13 caracteres")
            
        if preco < 0:
            raise ValueError("O preço não pode ser negativo")
        
        if quantidade < 0:
            raise ValueError("A quantidade não pode ser negativa")