from tabulate import tabulate
from utils import *

def abrir_caixa():
    produtos = [
    [1, "Produto 1", 1, 10],
    [2, "Produto 2", 2, 20],
    [3, "Produto 3", 3, 30],
    [4, "Produto 4", 4, 40],
    [5, "Produto 5", 5, 50]
    ]
    mensagem = [["Caixa aberto com sucesso!"]]
    print(tabulate(mensagem))
    return produtos

def menu_atendimento():
    mensagem = "1- Iniciar atendimento\n2- finalizar atendimento\n\nDigite uma das opções: "
    erro = "Operação inválida"
    operacao = validar_inteiros(mensagem, 1, 2, erro)
    return operacao

def ler_dados_produto():
    erro_id_produtos = "Erro: produto não cadastrado"
    id_produto = validar_inteiros("Insira o ID do produto (0 para finalizar): ", 0, 5, erro_id_produtos)
    if id_produto == 0:
        return 0, 0
    qtd_produto = validar_quantidade_produtos("Insira a quantidade do produto: ")
    return id_produto, qtd_produto

def buscar_produto(produtos, id_produto):
    for produto in produtos:
        if produto[0] == id_produto:
           return produto
    return None


def criar_item(id_item, produto, qtd_produto,):
    item = [id_item, produto[1], qtd_produto, produto[-1], qtd_produto * produto[-1]]
    return item


def atualizar_estoque(produto, qtd_produto):
    produto[2] -= qtd_produto

def emitir_nf(lista):

    id_cliente, data_hora, itens, total_itens, total_vendas = lista

    cabecalho = ["ID Item", "Produto", "Quantidade", "Preço Unit.", "Preço Total"]

    print(f"\nCliente: {id_cliente}    {data_hora}\n")

    print(tabulate(itens, headers=cabecalho))

    print(f"\nNúmero de itens: {total_itens}")
    print(f"Total da venda: R$ {total_vendas:.2f}\n")


def iniciar_atendimento(produtos, id_cliente):
    lista_items = criar_lista_itens_cliente(produtos)
    if not lista_items:
        print("Atendimento encerrado!")
        return None, id_cliente
    data_hora= retornar_data_hora()
    itens = lista_items
    num_itens = len(lista_items)   
    valor_total = somar_total(lista_items)
    relatorio = [id_cliente, data_hora, itens, num_itens, valor_total]
    id_cliente +=1 
    return relatorio, id_cliente 

def criar_lista_itens_cliente(produtos):
    id_item = 1
    itens_cliente = []
    while True:
        id_produto, qtd_produto = ler_dados_produto()
        if id_produto != 0:
            produto_encontrado = buscar_produto(produtos, id_produto)
            novo_item = criar_item(id_item, produto_encontrado, qtd_produto)
            itens_cliente.append(novo_item)
            atualizar_estoque(produto_encontrado, qtd_produto)
            id_item += 1  
        else:
            return itens_cliente
        
def emitir_sangria(relatorio):
    header = ["Cliente", "Total"]
    dados = []
    total_vendas = 0
    for item in relatorio:
        cliente = f"Cliente {item[0]}" 
        total = item[4]
        dados.append((cliente, total))
        total_vendas += total
    print("\nFechamento do caixa")
    data_hora = retornar_data_hora()
    print(f"Data: {data_hora}\n")
    print(tabulate(dados, headers=header))
    print(f"\nTotal geral: R$ {total_vendas:.2f}")

def produtos_sem_estoque(produtos):
    sem_estoque = []

    for produto in produtos:
        if produto[2] <= 0:
            sem_estoque.append([produto[0], produto[1]])  # ID e Nome
    if sem_estoque:  # só printa se houver produtos sem estoque
        print("\nProdutos sem estoque:\n")
        print(tabulate(sem_estoque, headers=["ID", "Produto"]))
    else:
        print("\nNenhum produto sem estoque.\n")
        

produtos = abrir_caixa()
id_cliente = 1
relatorios = []   
while True:
    opcao_caixa = menu_atendimento()
    if opcao_caixa == 1:
        relatorio, id_cliente = iniciar_atendimento(produtos, id_cliente)
        if not relatorio:
            continue
        emitir_nf(relatorio)
        relatorios.append(relatorio)   
    elif opcao_caixa == 2:
        emitir_sangria(relatorios)
        produtos_sem_estoque(produtos)
        print("\nCaixa finalizado")
        break
            



