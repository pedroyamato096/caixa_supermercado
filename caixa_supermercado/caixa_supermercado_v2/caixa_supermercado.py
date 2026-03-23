from tabulate import tabulate
from util import *
from estoque import *
from menus import *
from fechamento_caixa import *
from atendimento import *

def iniciar_sistema(produtos):
    numero_cliente_atual = 1
    caixa_aberto = True
    historico_vendas = []
    while caixa_aberto:
        opcao_caixa = exibir_menu_caixa()
        if opcao_caixa == OPCAO_INICIAR_ATENDIMENTO:
            total_gasto = realizar_atendimento(numero_cliente_atual, produtos)
            nome_cliente = f"Cliente {numero_cliente_atual}"
            historico_vendas.append([nome_cliente, total_gasto])
            numero_cliente_atual += 1 
        elif opcao_caixa == OPCAO_FECHAR_CAIXA:
            total_geral_caixa = calcular_total_vendas(historico_vendas)
            produtos_zerados = obter_produtos_sem_estoque(produtos)
            data_hora = retornar_data_hora() 
            exibir_fechamento_caixa(historico_vendas, total_geral_caixa, produtos_zerados, data_hora)
            caixa_aberto = False
        else:
            print("Erro: Opção inválida. Tente novamente.")

produtos = criar_lista_produtos()
iniciar_sistema(produtos)
