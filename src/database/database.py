import mysql.connector


class Database:
    def __init__(self):
        self._conexao = None
        self._cursor = None

    def conectar(self):
        if self._conexao:
           return 

        self._conexao = mysql.connector.connect(
            user="root", password="9572", host="localhost", database="sistema_graal"
        )
        self._cursor = self._conexao.cursor(buffered=True)

    def fechar_conexao(self):
        if not self._conexao:
            return

        self._conexao.close()

        self._conexao = None
        self._cursor = None

    def execute(self, query: str, params=()):
        if not self._conexao or not self._cursor:
            raise ValueError("Nenhuma conexão encontrada!")

        self._cursor.execute(query, params)

    def fetchone(self):
        if not self._conexao or not self._cursor:
            raise ValueError("Nenhuma conexão encontrada!")

        return self._cursor.fetchone()

    def fetchall(self):
        if not self._conexao or not self._cursor:
            raise ValueError("Nenhuma conexão encontrada!")

        return self._cursor.fetchall()

    def commit(self):
        if not self._conexao:
            raise ValueError("Nenhuma conexão encontrada!")

        self._conexao.commit()
