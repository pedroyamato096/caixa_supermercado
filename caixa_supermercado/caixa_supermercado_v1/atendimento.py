from utils import validar_inteiros, validar_quantidade_produtos, retornar_data_hora, somar_total
from estoque import buscar_produto, atualizar_estoque


def ler_dados_produto():
    erro = "Erro: produto não cadastrado"
    id_produto = validar_inteiros("Insira o ID do produto (0 para finalizar): ", 0, 5, erro)
    if id_produto == 0:
        return 0, 0
    qtd_produto = validar_quantidade_produtos("Insira a quantidade do produto: ")
    return id_produto, qtd_produto

def criar_item(id_item, produto, qtd_produto):
    item = [id_item, produto[1], qtd_produto, produto[3], qtd_produto * produto[3]]
    return item


def criar_lista_itens_cliente(produtos):
    id_item = 1
    itens_cliente = []
    while True:
        id_produto, qtd_produto = ler_dados_produto()
        if id_produto == 0:
            return itens_cliente
        produto = buscar_produto(produtos, id_produto)
        novo_item = criar_item(id_item, produto, qtd_produto)
        itens_cliente.append(novo_item)
        atualizar_estoque(produto,qtd_produto)
        id_item += 1

def iniciar_atendimento(produtos, id_cliente):
    lista_items = criar_lista_itens_cliente(produtos)
    if not lista_items:
        print("Atendimento encerrado!")
        return None, id_cliente
    data_hora = retornar_data_hora()
    total = somar_total(lista_items)
    relatorio = [id_cliente, data_hora, lista_items, len(lista_items), total]
    id_cliente += 1
    return relatorio, id_cliente