from util import *
from constantes import *
from arquivo import *

def atualizar_estoque(produto, qtd):
    produto.qtd -= qtd

def calcular_total_compra(carrinho_cliente):
    total = 0.0
    for item in carrinho_cliente:
        total += item[ITEM_IDX_PRECO_TOT] 
        
    return total

def pesquisar_produto(id, produtos):
    for produto in produtos:
        if produto.id == id:
            return produto
    return None

def criar_item_compra(id_item, produto, quantidade_comprada):
    nome_produto = produto.produto
    preco_unitario = produto.preco
    preco_total = preco_unitario * quantidade_comprada
    novo_item = [id_item, nome_produto, quantidade_comprada, preco_unitario, preco_total]
    
    return novo_item

def obter_produtos_sem_estoque(lista_produtos):
    produtos_zerados = []
    for produto in lista_produtos:
        if produto.qtd <= 0:
            produtos_zerados.append(produto)
            
    return produtos_zerados