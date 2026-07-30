from tabulate import tabulate

def buscar_produto(produtos, id_produto):
    for produto in produtos:
        if produto[0] == id_produto:
            return produto
    return None

def atualizar_estoque(produto, qtd_produto):
    produto[2] -= qtd_produto

def produtos_sem_estoque(produtos):
    sem_estoque = []
    for produto in produtos:
        if produto[2] <= 0:
            sem_estoque.append([
                produto[0],
                produto[1]
            ])
    if sem_estoque:
        print("\nProdutos sem estoque:\n")
        print(tabulate(
            sem_estoque,
            headers=["ID", "Produto"]
        ))
    else:
        print("\nNenhum produto sem estoque.\n")