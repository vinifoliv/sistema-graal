from typing import List
from domain.funcionario import Funcionario
from domain.item import Item
from domain.venda import Venda
from model.produto_model import ProdutoModel
from model.venda_model import VendaModel


class VendaController:
    def __init__(self, produto_model: ProdutoModel, venda_model: VendaModel):
        self._produto_model = produto_model
        self._venda_model = venda_model

    def buscar_funcionario_por_codigo(
        self, codigo_funcionario: str
    ) -> Funcionario | None:
        funcionario = self._venda_model.buscar_funcionario_por_codigo(
            codigo_funcionario
        )
        return funcionario

    def cadastrar_venda(
        self, codigo_funcionario: str, nome_cliente: str | None, itens: List[Item]
    ):
        funcionario = self.buscar_funcionario_por_codigo(codigo_funcionario)
        if not funcionario:
            raise ValueError("Funcionário não encontrado!")

        for produto in itens:
            estoque_produto = self._produto_model.buscar_por_ean(produto.ean_produto)
            if produto.quantidade > estoque_produto.quantidade:
                raise ValueError(
                    f"Estoque insuficiente para {produto.quantidade} unidades de {produto.descricao} (estoque: {estoque_produto.quantidade})!"
                )

        venda = Venda(codigo_funcionario, nome_cliente, itens)

        self._venda_model.cadastrar_venda(venda)
