class Produto:
    def __init__(self, id, produto, qtd, preco):
        self.id = id
        self.produto = produto
        self.qtd = qtd
        self.preco = preco

    def __str__(self):
        return f"{self.id} {self.produto} {self.qtd} {self.preco}"