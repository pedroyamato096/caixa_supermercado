from util import *
from constantes import *

def atualizar_estoque(produto, qtd):
    produto[PRODUTO_IDX_ESTOQUE] -= qtd

def calcular_total_compra(carrinho_cliente):
    total = 0.0
    for item in carrinho_cliente:
        total += item[ITEM_IDX_PRECO_TOT] 
        
    return total