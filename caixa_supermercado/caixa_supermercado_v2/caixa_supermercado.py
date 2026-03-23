from tabulate import tabulate
from util import *
from estoque import *
from menus import *
from fechamento_caixa import *

def criar_lista_produtos():
    produtos = [
        [1, "Produto 1", 1, 10],
        [2, "Produto 2", 2, 20],
        [3, "Produto 3", 3, 30],
        [4, "Produto 4", 4, 40],
        [5, "Produto 5", 5, 50]
    ]
    return produtos

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

def realizar_atendimento(numero_cliente, produtos):
    carrinho_cliente = []
    atendimento_em_andamento = True
    while atendimento_em_andamento:
        opcao_atendimento = exibir_menu_atendimento(numero_cliente)
        if opcao_atendimento == OPCAO_INSERIR_ITEM:
            id = entrar_id(produtos)
            produto_encontrado = pesquisar_produto(id, produtos)
            while True:
                qtd = entrar_qtd()
                if produto_encontrado[PRODUTO_IDX_ESTOQUE] >= qtd:
                    break
                else:
                    print(f"Erro: Estoque insuficiente! Estoque atual: {produto_encontrado[PRODUTO_IDX_ESTOQUE]}")
                    
            id_item = len(carrinho_cliente) + 1
            novo_item = criar_item_compra(id_item, produto_encontrado, qtd )
            carrinho_cliente.append(novo_item)
            atualizar_estoque(produto_encontrado, qtd)
            print("Item adicionado com sucesso!")
        elif opcao_atendimento == OPCAO_FINALIZAR_ATENDIMENTO:
            atendimento_em_andamento = False    
            total_da_compra = calcular_total_compra(carrinho_cliente)
            data_hora_emissao = retornar_data_hora()
            exibir_nota_fiscal(carrinho_cliente, numero_cliente, total_da_compra, data_hora_emissao)
            return total_da_compra   
        else:
            print("Erro: Opção inválida. Tente novamente.")

produtos = criar_lista_produtos()
iniciar_sistema(produtos)
