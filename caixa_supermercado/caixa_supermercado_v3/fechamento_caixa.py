from constantes import *

def calcular_total_vendas(historico_vendas):
    total = 0.0
    for venda in historico_vendas:
        total += venda[1] 
    return total


