class ItemModel:
    def __init__(self, item_id: int, ean_produto: str, venda_id: int, quantidade: int):
        self.item_id = item_id
        self.ean_produto = ean_produto
        self.venda_id = venda_id
        self.quantidade = quantidade
