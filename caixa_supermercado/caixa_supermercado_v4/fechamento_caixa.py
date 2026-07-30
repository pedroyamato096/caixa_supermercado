def calcular_total_vendas(historico_vendas: list) -> float:
    return sum(venda[1] for venda in historico_vendas)
