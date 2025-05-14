from domain.funcionario import Funcionario
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
