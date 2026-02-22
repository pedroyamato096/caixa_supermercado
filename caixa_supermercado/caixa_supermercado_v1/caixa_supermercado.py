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
    mensagem = "Caixa aberto com sucesso!"
    print(tabulate(mensagem))
    return produtos

def menu_atendimento():
    mensagem = "1- Iniciar atendimento\n 2- finalizar atendimento"
    erro = "Operação inválida"
    operacao = validar_inteiros(mensagem, 1, 2, erro)
    return operacao

def ler_dados_produto():
    erro_id_produtos = "Erro: produto não cadastrado"
    id_produto = validar_inteiros("Insira o ID do produto (0 para finalizar): ", 1, 5, erro_id_produtos)
    qtd_produto = validar_quantidade_produtos("Insira a quantidade do produto:")
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
    return produto[2] - qtd_produto


def criar_lista_itens_cliente(produtos):
    itens_cliente = []
    id_item = 1
    while True:
        id_produto, qtd_produto = ler_dados_produto()
        if id_produto != 0:
            produto_encontrado = buscar_produto(produtos, id_produto)
            novo_item = criar_item(id_item, produto_encontrado, qtd_produto)
            itens_cliente.append(novo_item)
            id_item += 1
            atualizar_estoque(produto_encontrado, qtd_produto)
        else:
            return itens_cliente 


         

        
        

produtos = abrir_caixa()
while True:
    opcao_caixa = menu_atendimento()
    if opcao_caixa == 1:
        itens_cliente = criar_lista_itens_cliente()
        cabecalho = ["ID Item", "Produto", "Quantidade", "Preço Unit.", "Preço Total"]
        print(tabulate(itens_cliente, headers= cabecalho))
    elif opcao_caixa == 2:
        print("caixa finalizado")
        break
            


