from typing import Optional
from models import Produto
import produto_repository as repo


def _validar_id(id: int):
    if id <= 0:
        raise ValueError("O id do produto deve ser maior que zero.")


def _validar_produto_existe(produto: Optional[Produto]) -> Produto:
    if produto is None:
        raise ValueError("Produto não encontrado.")
    return produto


def _validar_estoque(produto: Produto, quantidade: int):
    if produto.quantidade < quantidade:
        raise ValueError(
            f"Estoque insuficiente. Disponível: {produto.quantidade}"
        )


def _validar_dados_produto(nome: str, quantidade: int, preco: float):
    if not nome or not nome.strip():
        raise ValueError("O nome do produto não pode ser vazio.")
    if quantidade < 0:
        raise ValueError("A quantidade não pode ser negativa.")
    if preco <= 0:
        raise ValueError("O preço deve ser maior que zero.")



def listar_todos() -> list[Produto]:
    return repo.buscar_todos()


def consultar(id: int) -> Produto:
    _validar_id(id)
    produto = repo.buscar_por_id(id)
    return _validar_produto_existe(produto)


def criar(nome: str, quantidade: int, preco: float) -> int:
    _validar_dados_produto(nome, quantidade, preco)
    novo = Produto(0, nome, quantidade, preco)
    return repo.inserir(novo)


def atualizar(id: int, nome: str, quantidade: int, preco: float):
    _validar_id(id)
    _validar_produto_existe(repo.buscar_por_id(id))
    _validar_dados_produto(nome, quantidade, preco)
    produto = Produto(id, nome, quantidade, preco)
    repo.atualizar(produto)


def remover(id: int):
    _validar_id(id)
    _validar_produto_existe(repo.buscar_por_id(id))
    repo.deletar(id)


def descontar_estoque(id: int, quantidade: int):
    _validar_id(id)
    produto = _validar_produto_existe(repo.buscar_por_id(id))
    _validar_estoque(produto, quantidade)
    produto.quantidade -= quantidade
    repo.atualizar(produto)


def obter_produtos_sem_estoque() -> list[Produto]:
    return [p for p in repo.buscar_todos() if p.quantidade <= 0]
