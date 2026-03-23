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
    # lista de lista de compras
    carrinho_cliente = []
    atendimento_em_andamento = True
    while atendimento_em_andamento:
        opcao_atendimento = exibir_menu_atendimento(numero_cliente)
        if opcao_atendimento == OPCAO_INSERIR_ITEM:
            id = entrar_id()
            qtd = entrar_qtd()
            produto_encontrado = pesquisar_produto(id, produtos)
            id_item = len(carrinho_cliente) + 1
            novo_item = criar_item_compra(id_item, produto_encontrado, qtd )
            carrinho_cliente.append(novo_item)
            atualizar_estoque(produto_encontrado, qtd)
            print("Item adicionado com sucesso!")
        elif opcao_atendimento == OPCAO_FINALIZAR_ATENDIMENTO:
            total_da_compra = calcular_total_compra(carrinho_cliente)
            data_hora_emissao = retornar_data_hora()
            exibir_nota_fiscal(carrinho_cliente, numero_cliente, total_da_compra, data_hora_emissao)
            atendimento_em_andamento = False        
        else:
            print("Erro: Opção inválida. Tente novamente.")

produtos = criar_lista_produtos()
iniciar_sistema()
realizar_atendimento()

