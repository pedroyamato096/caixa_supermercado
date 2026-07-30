import os
import sqlite3
from constantes import DB_DIR, DB_NOME_ARQUIVO

def caminho_banco() -> str:
    base = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base, DB_DIR, DB_NOME_ARQUIVO)

def obter_conexao() -> sqlite3.Connection:
    return sqlite3.connect(caminho_banco())
