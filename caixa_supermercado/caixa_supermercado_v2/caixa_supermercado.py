from tabulate import tabulate
from util import *
from estoque import *
def criar_lista_produtos():
    produtos = [
        [1, "Produto 1", 1, 10],
        [2, "Produto 2", 2, 20],
        [3, "Produto 3", 3, 30],
        [4, "Produto 4", 4, 40],
        [5, "Produto 5", 5, 50]
    ]
    return produtos

produtos = criar_lista_produtos()
id = entrar_id()
qtd = entrar_qtd()
produto_encontrado = pesquisar_produto(id, produtos)
atualizar_estoque(produto_encontrado, qtd)
print(produtos)
