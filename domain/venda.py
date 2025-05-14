from datetime import date
from typing import List

from domain.item import Item


class Venda:
    def __init__(self, codigo_funcionario: str, data: date):
        self.codigo_funcionario = codigo_funcionario
        self.data = data
        self.items: List[Item] = []

    def adicionar_item(self, ean_produto: str, quantidade: int):
        item = Item(ean_produto, quantidade)
        self.itens.push(item)
