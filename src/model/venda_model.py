from database.database import Database
from domain.funcionario import Funcionario
from domain.venda import Venda


class VendaModel:
    def __init__(self, database: Database):
        self._database = database

    def buscar_funcionario_por_codigo(
        self, codigo_funcionario: str
    ) -> Funcionario | None:
        self._database.conectar()
        self._database.execute(
            """
            SELECT * FROM funcionario WHERE codigo_funcionario=%s
            """,
            (codigo_funcionario,),
        )

        funcionario = self._database.fetchone()
        self._database.fechar_conexao()

        if not funcionario:
            return None

        return self._montar_funcionario(funcionario)

    def cadastrar_venda(self, venda: Venda):
        self._database.conectar()
        self._database.execute(
            """
            INSERT INTO venda(codigo_funcionario, nome_cliente) VALUES(%s, %s)
            """,
            (venda.codigo_funcionario, venda.nome_cliente),
        )

        self._database.execute(
            """
            SELECT LAST_INSERT_ID();
            """,
        )
        venda_id = int(self._database.fetchone()[0])

        for item in venda.itens:
            self._database.execute(
                """
                INSERT INTO item(ean_produto, venda_id, quantidade) VALUES(%s, %s, %s)
                """,
                (item.ean_produto, venda_id, item.quantidade),
            )

        for item in venda.itens:
            self._database.execute(
                """
                UPDATE produto SET quantidade=quantidade-%s WHERE ean_produto=%s
                """,
                (item.quantidade, item.ean_produto),
            )

        self._database.commit()
        self._database.fechar_conexao()

    def _montar_funcionario(self, funcionario) -> Funcionario:
        codigo = funcionario[0]
        nome = funcionario[1]
        return Funcionario(codigo, nome)
