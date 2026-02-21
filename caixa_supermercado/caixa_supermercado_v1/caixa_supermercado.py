from tabulate import tabulate

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


    


     


def criar_lista_itens_cliente(produtos):
    itens_cliente = []
    id_item = 1

    while True:
        
        item = []
        id_produto = int(input("Insira o ID do produto: "))
        qtd_produto = int(input("Digite a quantidade do produto: "))
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
