import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

config = {
    "user": os.getenv("DATABASE_USER"),
    "password": os.getenv("DATABASE_PASSWORD"),
    "host": os.getenv("DATABASE_HOST"),
    "database": os.getenv("DATABASE_DB"),
    "raise_on_warnings": True,
}


class Database:
    def __init__(self):
        self._cnx = mysql.connector.connect(**config)
        self._cursor = self._cnx.cursor(buffered=True)

    def execute(self, query: str, params=()):
        self._cursor.execute(query, params)

    def fetchone(self):
        return self._cursor.fetchone()

    def fetchall(self):
        return self._cursor.fetchall()
