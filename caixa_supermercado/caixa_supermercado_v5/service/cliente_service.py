from typing import Optional
from models import Cliente
import repository.cliente_repository as repo


def _validar_id(id: int):
    if id <= 0:
        raise ValueError("O id do cliente deve ser maior que zero.")


def _validar_nome(nome: str):
    if not nome or not nome.strip():
        raise ValueError("O nome do cliente não pode ser vazio.")
    if len(nome.strip()) > 50:
        raise ValueError("O nome do cliente deve ter no máximo 50 caracteres.")


def consultar(id: int) -> Optional[Cliente]:
    _validar_id(id)
    return repo.buscar_por_id(id)


def cadastrar(nome: str) -> int:
    _validar_nome(nome)
    novo = Cliente(nome=nome.strip())
    return repo.inserir(novo)


def listar_todos() -> list[Cliente]:
    return repo.buscar_todos()
