from tabulate import tabulate
from util import *
from estoque import *
from menus import *

def criar_lista_produtos():
    produtos = [
        [1, "Produto 1", 1, 10],
        [2, "Produto 2", 2, 20],
        [3, "Produto 3", 3, 30],
        [4, "Produto 4", 4, 40],
        [5, "Produto 5", 5, 50]
    ]
    return produtos

def iniciar_sistema():
    numero_cliente_atual = 1
    caixa_aberto = True
    while caixa_aberto:
        opcao_caixa = exibir_menu_caixa()
        if opcao_caixa == OPCAO_INICIAR_ATENDIMENTO:
            realizar_atendimento(numero_cliente_atual)
            numero_cliente_atual += 1 
        elif opcao_caixa == OPCAO_FECHAR_CAIXA:
            caixa_aberto = False
        else:
            print("Erro: Opção inválida. Tente novamente.")

def realizar_atendimento(numero_cliente):
    atendimento_em_andamento = True
    while atendimento_em_andamento:
        opcao_atendimento = exibir_menu_atendimento(numero_cliente)
        if opcao_atendimento == OPCAO_INSERIR_ITEM:
            print("Inserindo item...") 
        elif opcao_atendimento == OPCAO_FINALIZAR_ATENDIMENTO:
            atendimento_em_andamento = False        
        else:
            print("Erro: Opção inválida. Tente novamente.")

# produtos = criar_lista_produtos()
# abrir_caixa = exibir_menu_caixa()
# realizar_atendimento = exibir_menu_atendimento(1)
# id = entrar_id()
# qtd = entrar_qtd()
# produto_encontrado = pesquisar_produto(id, produtos)
# atualizar_estoque(produto_encontrado, qtd)
# print(produtos)
