from datetime import date

from database.database import Database
from domain.funcionario import Funcionario


class VendaModel:
    def __init__(self, database: Database):
        self._database = database

    def buscar_funcionario_por_codigo(
        self, codigo_funcionario: str
    ) -> Funcionario | None:
        self._database.execute(
            """
            SELECT * FROM funcionario WHERE codigo_funcionario=%s
            """,
            (codigo_funcionario,),
        )

        funcionario = self._database.fetchone()
        if not funcionario:
            return None
        return self._montar_funcionario(funcionario)

    def _montar_funcionario(self, funcionario) -> Funcionario:
        codigo = funcionario[0]
        nome = funcionario[1]
        return Funcionario(codigo, nome)
