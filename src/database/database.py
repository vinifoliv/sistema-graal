import mysql.connector

class Database:
    def __init__(self):
        self._cnx = mysql.connector.connect(
            user="root",
            password="9572",
            host="localhost",
            database="sistema_graal"
        )
        self._cursor = self._cnx.cursor(buffered=True)

    def execute(self, query: str, params=()):
        self._cursor.execute(query, params)

    def fetchone(self):
        return self._cursor.fetchone()

    def fetchall(self):
        return self._cursor.fetchall()

    def commit(self):
        self._cnx.commit()  
