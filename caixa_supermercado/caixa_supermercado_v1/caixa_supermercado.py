from tabulate import tabulate
from utils import *

def abrir_caixa():
    print("Caixa aberto com sucesso!")
    produtos = [
    [1, "Produto 1", 1, 10],
    [2, "Produto 2", 2, 20],
    [3, "Produto 3", 3, 30],
    [4, "Produto 4", 4, 40],
    [5, "Produto 5", 5, 50]
]
    return produtos

def ler_dados_produto():
    erro_id_produtos = "Erro: produto não cadastrado"
    id_produto = validar_inteiros("Insira o ID do produto: ", 1, 5, erro_id_produtos)
    qtd_produto = validar_quantidade_produtos("Insira a quantidade do produto:")
    return id_produto, qtd_produto


def criar_lista_itens_cliente(produtos):
    itens_cliente = []
    id_item = 1
    id_produto, qtd_produto = ler_dados_produto()
    while True:
        
        item = []
        
        encontrado = False

        for produto in produtos:
            if produto[0] == id_produto:
                encontrado = True
                item = [id_item, produto[1], qtd_produto, produto[-1], qtd_produto * produto[-1]]
                itens_cliente.append(item)
                produto[2] -= qtd_produto
                id_item += 1
                break

        if not encontrado:
            print("Item não encontrado")
            continue
        
        continuar = input("""Deseja ler mais produtos?
[1] sim | [2] não
""")

        if continuar == "1":
            continue
        else:
            return itens_cliente

produtos = abrir_caixa()
lista = criar_lista_itens_cliente(produtos)
cabecalho = ["ID Item", "Produto", "Quantidade", "Preço Unit.", "Preço Total"]
print(tabulate(lista, headers= cabecalho))
