from typing import Optional
from models import Cliente
from db_conexao import obter_sessao


def buscar_todos() -> list[Cliente]:
    with obter_sessao() as sessao:
        return sessao.query(Cliente).all()


def buscar_por_id(id: int) -> Optional[Cliente]:
    with obter_sessao() as sessao:
        return sessao.query(Cliente).filter(Cliente.id == id).first()


def inserir(cliente: Cliente) -> int:
    with obter_sessao() as sessao:
        sessao.add(cliente)
        sessao.commit()
        sessao.refresh(cliente)
        return cliente.id
