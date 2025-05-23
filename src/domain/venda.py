from typing import List

from domain.item import Item


class Venda:
    def __init__(
        self, codigo_funcionario: str, nome_cliente: str | None, itens: List[Item]
    ):
        self._validar_itens(itens)

        self.codigo_funcionario = codigo_funcionario
        self.nome_cliente = nome_cliente
        self.itens = itens

    def _validar_itens(self, itens: List[Item]):
        if not len(itens):
            raise ValueError("Não é permitida a venda sem itens!")
