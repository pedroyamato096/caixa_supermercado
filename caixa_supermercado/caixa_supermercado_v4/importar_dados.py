import os
import sys
import pandas as pd
import sqlite3

from constantes import CSV_DIR, CSV_NOME_ARQUIVO, DB_TABELA_PRODUTOS
from db_conexao import caminho_banco, obter_conexao


def caminho_csv() -> str:
    base = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base, CSV_DIR, CSV_NOME_ARQUIVO)


def banco_ja_populado(conexao: sqlite3.Connection) -> bool:
    cursor = conexao.execute(f"SELECT COUNT(*) FROM {DB_TABELA_PRODUTOS}")
    return cursor.fetchone()[0] > 0


def ler_csv() -> pd.DataFrame:
    return pd.read_csv(caminho_csv())


def inserir_dataframe(df: pd.DataFrame, conexao: sqlite3.Connection):
    df.to_sql(DB_TABELA_PRODUTOS, conexao, if_exists="append", index=False)


def importar_csv_para_banco():
    try:
        conexao = obter_conexao()
        if banco_ja_populado(conexao):
            return
        df = ler_csv()
        inserir_dataframe(df, conexao)
        conexao.commit()
        conexao.close()
    except Exception as erro:
        print(f"Erro ao importar produtos para o banco de dados: {erro}")
        sys.exit(1)
