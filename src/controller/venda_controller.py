from typing import List
from domain.funcionario import Funcionario
from domain.item import Item
from domain.venda import Venda
from model.venda_model import VendaModel


class VendaController:
    def __init__(self, venda_model: VendaModel):
        self._venda_model = venda_model

    def buscar_funcionario_por_codigo(
        self, codigo_funcionario: str
    ) -> Funcionario | None:
        funcionario = self._venda_model.buscar_funcionario_por_codigo(
            codigo_funcionario
        )
        return funcionario

    def cadastrar_venda(self, codigo_funcionario: str, itens: List[Item]):
        funcionario = self.buscar_funcionario_por_codigo(codigo_funcionario)
        if not funcionario:
            raise ValueError("Funcionário não encontrado!")

        venda = Venda(funcionario.codigo_funcionario, itens)

        self._venda_model.cadastrar_venda(venda)
