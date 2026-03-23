from menus import *

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