from typing import Optional
from models import Produto
from db_conexao import obter_sessao


def buscar_todos() -> list[Produto]:
    with obter_sessao() as sessao:
        return sessao.query(Produto).all()


def buscar_por_id(id: int) -> Optional[Produto]:
    with obter_sessao() as sessao:
        return sessao.query(Produto).filter(Produto.id == id).first()


def inserir(produto: Produto) -> int:
    with obter_sessao() as sessao:
        sessao.add(produto)
        sessao.commit()
        sessao.refresh(produto)
        return produto.id


def atualizar(produto: Produto):
    with obter_sessao() as sessao:
        sessao.merge(produto)
        sessao.commit()


def deletar(id: int):
    with obter_sessao() as sessao:
        produto = sessao.query(Produto).filter(Produto.id == id).first()
        if produto:
            sessao.delete(produto)
            sessao.commit()
