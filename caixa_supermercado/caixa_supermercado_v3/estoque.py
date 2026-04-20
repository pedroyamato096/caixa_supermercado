from util import *
from constantes import *
from arquivo import *

# def criar_lista_produtos():
#     produtos = [
#         [1, "Produto 1", 1, 10],
#         [2, "Produto 2", 2, 20],
#         [3, "Produto 3", 3, 30],
#         [4, "Produto 4", 4, 40],
#         [5, "Produto 5", 5, 50]
#     ]
#     return produtos

def atualizar_estoque(produto, qtd):
    produto["estoque"] -= qtd

def calcular_total_compra(carrinho_cliente):
    total = 0.0
    for item in carrinho_cliente:
        total += item[ITEM_IDX_PRECO_TOT] 
        
    return total

def pesquisar_produto(id, produtos):
    produto_procurado = []
    for produto in produtos:
        if produto["id"] == id:
            produto_procurado = produto
            break
    return produto_procurado

def criar_item_compra(id_item, produto, quantidade_comprada):
    nome_produto = produto["item"]
    preco_unitario = produto["preço"]
    preco_total = preco_unitario * quantidade_comprada
    novo_item = [id_item, nome_produto, quantidade_comprada, preco_unitario, preco_total]
    
    return novo_item

def obter_produtos_sem_estoque(lista_produtos):
    """
    Percorre o estoque e retorna uma nova lista contendo apenas 
    os produtos com quantidade menor ou igual a zero.
    """
    produtos_zerados = []
    for produto in lista_produtos:
        if produto["estoque"] <= 0:
            produtos_zerados.append(produto)
            
    return produtos_zerados