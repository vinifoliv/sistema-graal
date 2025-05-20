from typing import List

from domain.item import Item


class Venda:
    def __init__(self, codigo_funcionario: str, itens: List[Item]):
        self.codigo_funcionario = codigo_funcionario
        self.itens = itens
