import sqlite3
from typing import Optional

from constantes import DB_TABELA_PRODUTOS
from db_conexao import obter_conexao
from models import Produto


def _linha_para_produto(linha: tuple) -> Produto:
    return Produto(linha[0], linha[1], linha[2], linha[3])


def buscar_todos() -> list[Produto]:
    with obter_conexao() as con:
        cursor = con.execute(
            f"SELECT id, nome, quantidade, preco FROM {DB_TABELA_PRODUTOS}"
        )
        return [_linha_para_produto(l) for l in cursor.fetchall()]


def buscar_por_id(id: int) -> Optional[Produto]:
    with obter_conexao() as con:
        cursor = con.execute(
            f"SELECT id, nome, quantidade, preco FROM {DB_TABELA_PRODUTOS} WHERE id = ?",
            (id,)
        )
        linha = cursor.fetchone()
        return _linha_para_produto(linha) if linha else None


def inserir(produto: Produto) -> int:
    with obter_conexao() as con:
        cursor = con.execute(
            f"INSERT INTO {DB_TABELA_PRODUTOS} (nome, quantidade, preco) VALUES (?, ?, ?)",
            (produto.nome, produto.quantidade, produto.preco)
        )
        con.commit()
        return cursor.lastrowid


def atualizar(produto: Produto):
    with obter_conexao() as con:
        con.execute(
            f"UPDATE {DB_TABELA_PRODUTOS} SET nome = ?, quantidade = ?, preco = ? WHERE id = ?",
            (produto.nome, produto.quantidade, produto.preco, produto.id)
        )
        con.commit()


def deletar(id: int):
    with obter_conexao() as con:
        con.execute(
            f"DELETE FROM {DB_TABELA_PRODUTOS} WHERE id = ?",
            (id,)
        )
        con.commit()
