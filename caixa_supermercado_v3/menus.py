from util import *
from tabulate import tabulate
from constantes import *
from estoque import *

def exibir_menu_caixa():
    msg = "Entre com a opção: "
    print("\n=== MENU DO CAIXA ===")
    print(f"{OPCAO_INICIAR_ATENDIMENTO} - Iniciar Atendimento")
    print(f"{OPCAO_FECHAR_CAIXA} - Fechar Caixa")
    opcao = obter_opcao_valida(msg, [1, 2])
    return opcao

def exibir_menu_atendimento(numero_cliente): 
    msg = "Entre com a opção: "
    print(f"\n=== ATENDIMENTO: Cliente {numero_cliente} ===")
    print(f"{OPCAO_INSERIR_ITEM} - Inserir item ") 
    print(f"{OPCAO_FINALIZAR_ATENDIMENTO} - Finalizar Atendimento")
    opcao = obter_opcao_valida(msg, [1, 2])
    return opcao

def exibir_nota_fiscal(carrinho_cliente, cliente, total_compra, data_hora):
    cabecalhos = ["Item", "Produto", "Quant.", "Preço", "Total"]
    print("\n" + "=" * 40)
    print("NOTA FISCAL".center(40))
    print("=" * 40)
    print(f"Cliente {cliente}")
    print(f"{data_hora}")
    print(tabulate(carrinho_cliente, headers=cabecalhos))
    print("-" * 40)
    print(f"Itens: {len(carrinho_cliente)}")
    print(f"TOTAL DA COMPRA: R$ {total_compra:.2f}")
    print("=" * 40 + "\n")
    

from tabulate import tabulate

def exibir_fechamento_caixa(historico_vendas, total_caixa, produtos_sem_estoque, data_hora):
    tabela_cabecalho = [["FECHAMENTO DO CAIXA", f"Emissão: {data_hora}"]]
    print("\n" + tabulate(tabela_cabecalho, tablefmt="fancy_grid"))
    
    if len(historico_vendas) > 0:
        dados_vendas = list(historico_vendas)
        dados_vendas.append(["TOTAL GERAL DO CAIXA", total_caixa])
        print(tabulate(dados_vendas, headers=["RESUMO DE VENDAS (Cliente)", "VALOR (R$)"], tablefmt="fancy_grid", floatfmt=".2f"))
    else:
        print(tabulate([["Nenhuma venda foi realizada neste turno."]], headers=["RESUMO DE VENDAS"], tablefmt="fancy_grid"))
       
    if len(produtos_sem_estoque) > 0:
        cabecalhos_estoque = ["ID", "PRODUTOS SEM ESTOQUE", "Estoque", "Preço (R$)"]
        dados_estoque = []
        for produto in produtos_sem_estoque:
            dados_estoque.append([
                produto.id,
                produto.produto,
                produto.qtd,
                produto.preco
            ])
        print(tabulate(dados_estoque, headers=cabecalhos_estoque, tablefmt="fancy_grid", floatfmt=".2f"))
    else:
        print(tabulate([["Todos os produtos possuem estoque disponível."]], headers=["PRODUTOS SEM ESTOQUE"], tablefmt="fancy_grid"))
    
    print("\n")
