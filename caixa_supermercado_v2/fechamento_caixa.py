from constantes import *

def calcular_total_vendas(historico_vendas):
    """
    Recebe a lista de todas as vendas do dia e soma o total.
    O historico_vendas será uma lista de listas: [['Cliente 1', 150.0], ['Cliente 2', 80.0]]
    """
    total = 0.0
    for venda in historico_vendas:
        total += venda[1] 
    return total


