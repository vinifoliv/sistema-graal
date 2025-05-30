from typing import List
from database.database import Database
from domain.produto import Produto


class ProdutoModel:
    def __init__(self, database: Database):
        self._database = database

    def cadastrar(self, produto: Produto):
        self._database.conectar()
        self._database.execute(
            """
            INSERT INTO produto(ean_produto, descricao, preco, quantidade, unidade)
            VALUES(%s, %s, %s, %s, %s)
            """,
            (
                produto.ean_produto,
                produto.descricao,
                float(produto.preco),
                produto.quantidade,
                produto.unidade,
            ),
        )
        self._database.commit()
        self._database.fechar_conexao()

    def alterar(self, produto: Produto):
        self._database.conectar()
        self._database.execute(
            """
            UPDATE produto SET descricao=%s, preco=%s, quantidade=%s, unidade=%s
            WHERE ean_produto=%s
            """,
            (
                produto.descricao,
                produto.preco,
                produto.quantidade,
                produto.unidade,
                produto.ean_produto,
            ),
        )
        self._database.commit()
        self._database.fechar_conexao()

    def buscar(self) -> List[Produto]:
        self._database.conectar()
        self._database.execute(
            """
            SELECT * FROM produto
            """
        )
        produtos = self._database.fetchall()
        self._database.fechar_conexao()
        return list(map(lambda p: self._montar_produto(p), produtos))

    def buscar_por_descricao(self, descricao: str) -> Produto | None:
        self._database.conectar()
        self._database.execute(
            """
            SELECT * FROM produto WHERE descricao=%s
            """,
            (descricao,),
        )

        produto = self._database.fetchone()
        if not produto:
            return None

        self._database.fechar_conexao()
        return self._montar_produto(produto)

    def buscar_por_ean(self, ean_produto: str) -> Produto | None:
        self._database.conectar()
        self._database.execute(
            """
            SELECT * FROM produto WHERE ean_produto=%s
            """,
            (ean_produto,),
        )

        produto = self._database.fetchone()
        if not produto:
            return None

        self._database.fechar_conexao()
        return self._montar_produto(produto)

    def filtrar_por_descricao(self, descricao: str) -> List[Produto]:
        self._database.conectar()
        self._database.execute(
            """
            SELECT * FROM produto WHERE LOWER(descricao) LIKE LOWER(%s)
            """,
            ("%" + descricao + "%",),
        )

        produtos = self._database.fetchall()
        self._database.fechar_conexao()
        return list(map(lambda p: self._montar_produto(p), produtos))

    def excluir(self, ean_produto: str):
        self._database.conectar()
        self._database.execute(
            """
            DELETE FROM produto WHERE ean_produto=%s
            """,
            (ean_produto,),
        )
        self._database.commit()
        self._database.fechar_conexao()

    def _montar_produto(self, produto) -> Produto:
        ean_produto = produto[0]
        descricao = produto[1]
        preco = produto[2]
        quantidade = produto[3]
        unidade = produto[4]
        return Produto(ean_produto, descricao, preco, quantidade, unidade)
