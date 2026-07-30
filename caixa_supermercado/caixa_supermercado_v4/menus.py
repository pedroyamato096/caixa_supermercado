from tabulate import tabulate
from constantes import (
    OPCAO_INICIAR_ATENDIMENTO, OPCAO_FECHAR_CAIXA,
    OPCAO_INSERIR_ITEM, OPCAO_FINALIZAR_ATENDIMENTO
)
from util import obter_opcao_valida


def exibir_menu_caixa() -> int:
    print("\n=== MENU DO CAIXA ===")
    print(f"{OPCAO_INICIAR_ATENDIMENTO} - Iniciar Atendimento")
    print(f"{OPCAO_FECHAR_CAIXA} - Fechar Caixa")
    return obter_opcao_valida("Entre com a opção: ", [1, 2])


def exibir_menu_atendimento(numero_cliente: int) -> int:
    print(f"\n=== ATENDIMENTO: Cliente {numero_cliente} ===")
    print(f"{OPCAO_INSERIR_ITEM} - Inserir item")
    print(f"{OPCAO_FINALIZAR_ATENDIMENTO} - Finalizar Atendimento")
    return obter_opcao_valida("Entre com a opção: ", [1, 2])


def exibir_nota_fiscal(carrinho: list, numero_cliente: int, total: float, data_hora: str):
    cabecalhos = ["Item", "Produto", "Quant.", "Preço Un.", "Total"]
    print("\n" + "=" * 44)
    print("NOTA FISCAL".center(44))
    print("=" * 44)
    print(f"Cliente {numero_cliente}")
    print(f"{data_hora}")
    print(tabulate(carrinho, headers=cabecalhos, floatfmt=".2f"))
    print("-" * 44)
    print(f"Itens: {len(carrinho)}")
    print(f"TOTAL DA COMPRA: R$ {total:.2f}")
    print("=" * 44 + "\n")


def exibir_fechamento_caixa(historico: list, total_caixa: float, sem_estoque: list, data_hora: str):
    cabecalho = [["FECHAMENTO DO CAIXA", f"Emissão: {data_hora}"]]
    print("\n" + tabulate(cabecalho, tablefmt="fancy_grid"))

    _exibir_resumo_vendas(historico, total_caixa)
    _exibir_produtos_sem_estoque(sem_estoque)
    print()


def _exibir_resumo_vendas(historico: list, total_caixa: float):
    if historico:
        dados = list(historico) + [["TOTAL GERAL DO CAIXA", total_caixa]]
        print(tabulate(dados, headers=["Cliente", "Valor (R$)"], tablefmt="fancy_grid", floatfmt=".2f"))
    else:
        print(tabulate([["Nenhuma venda realizada neste turno."]], headers=["RESUMO DE VENDAS"], tablefmt="fancy_grid"))


def _exibir_produtos_sem_estoque(sem_estoque: list):
    if sem_estoque:
        dados = [[p.id, p.nome, p.quantidade, p.preco] for p in sem_estoque]
        print(tabulate(dados, headers=["ID", "Produto", "Estoque", "Preço (R$)"], tablefmt="fancy_grid", floatfmt=".2f"))
    else:
        print(tabulate([["Todos os produtos possuem estoque disponível."]], headers=["PRODUTOS SEM ESTOQUE"], tablefmt="fancy_grid"))
