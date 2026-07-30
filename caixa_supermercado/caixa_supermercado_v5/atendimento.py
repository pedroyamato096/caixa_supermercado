from constantes import OPCAO_INSERIR_ITEM, OPCAO_FINALIZAR_ATENDIMENTO
from menus import exibir_menu_atendimento, exibir_nota_fiscal
from estoque import criar_item_compra, calcular_total_compra, agrupar_carrinho
from util import entrar_id_produto, entrar_qtd, retornar_data_hora
from models import Cliente
import service.produto_service as service


def _tentar_adicionar_item(carrinho: list) -> list:
    id_produto = entrar_id_produto()
    produto    = service.consultar(id_produto)
    quantidade = entrar_qtd()

    try:
        service.descontar_estoque(id_produto, quantidade)
        id_item = len(carrinho) + 1
        item    = criar_item_compra(id_item, id_produto, produto.nome, produto.preco, quantidade)
        carrinho.append(item)
        print("Item adicionado com sucesso!")
    except ValueError as e:
        print(f"Erro: {e}")

    return carrinho


def _finalizar_atendimento(carrinho: list, cliente: Cliente) -> float:
    carrinho_agrupado = agrupar_carrinho(carrinho)
    total             = calcular_total_compra(carrinho_agrupado)
    data_hora         = retornar_data_hora()
    exibir_nota_fiscal(carrinho_agrupado, cliente, total, data_hora)
    return total


def realizar_atendimento(cliente: Cliente) -> float:
    carrinho     = []
    em_andamento = True

    while em_andamento:
        opcao = exibir_menu_atendimento(cliente)

        if opcao == OPCAO_INSERIR_ITEM:
            carrinho = _tentar_adicionar_item(carrinho)
        elif opcao == OPCAO_FINALIZAR_ATENDIMENTO:
            em_andamento = False
            return _finalizar_atendimento(carrinho, cliente)
        else:
            print("Erro: Opção inválida. Tente novamente.")

    return 0.0
