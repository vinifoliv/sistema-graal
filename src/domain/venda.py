from typing import List

from domain.item import Item


class Venda:
    def __init__(
        self, codigo_funcionario: str, nome_cliente: str | None, itens: List[Item]
    ):
        self.codigo_funcionario = codigo_funcionario
        self.nome_cliente = nome_cliente
        self.itens = itens
