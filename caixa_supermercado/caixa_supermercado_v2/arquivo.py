import os.path 

ARQ = "produtos.csv"
DIR = os.path.dirname(os.path.abspath(__file__))
ARQ = os.path.join(DIR, ARQ)

def ler_produtos():
    produtos = []
    try: 
        with open(ARQ, mode="r", encoding="UTF-8") as arquivo:
            for linha in arquivo:
                campos = linha.split(",")
                id = int(campos[0])
                item = campos[1]
                estoque = int(campos[2])
                preco = float(campos[3])
                produtos.append({"id": id, "item": item, "estoque": estoque, "preço": preco})
    except Exception as ex:
        print("Erro: leitura do arquivo", ex)
        exit
    return produtos

# produtos = [
#     {"id": 1, "nome": "Produto 1", "quantidade": 1, "preco": 10},
#     {"id": 2, "nome": "Produto 2", "quantidade": 2, "preco": 20},
#     {"id": 3, "nome": "Produto 3", "quantidade": 3, "preco": 30},
#     {"id": 4, "nome": "Produto 4", "quantidade": 4, "preco": 40},
#     {"id": 5, "nome": "Produto 5", "quantidade": 5, "preco": 50}
# ]