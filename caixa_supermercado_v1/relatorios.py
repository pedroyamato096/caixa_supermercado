from tabulate import tabulate
from utils import retornar_data_hora


def emitir_nf(relatorio):
    id_cliente, data_hora, itens, total_itens, total = relatorio
    cabecalho = [
        "ID Item",
        "Produto",
        "Quantidade",
        "Preço Unit.",
        "Preço Total"
    ]
    print(f"\nCliente: {id_cliente}    {data_hora}\n")
    print(tabulate(
        itens,
        headers=cabecalho
    ))
    print(f"\nNúmero de itens: {total_itens}")
    print(f"Total da venda: R$ {total:.2f}\n")

def emitir_sangria(relatorios):
    header = ["Cliente", "Total"]
    dados = []
    total_vendas = 0
    for relatorio in relatorios:
        cliente = f"Cliente {relatorio[0]}"
        total = relatorio[4]
        dados.append(
            (cliente, total)
        )
        total_vendas += total
    print("\nFechamento do caixa")
    data = retornar_data_hora()
    print(f"Data: {data}\n")
    print(tabulate(
        dados,
        headers=header
    ))
    print(f"\nTotal geral: R$ {total_vendas:.2f}")