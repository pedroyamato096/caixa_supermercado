import os.path 
from constantes import *
from constantes import *

ARQ = "produtos.csv"
DIR = os.path.dirname(os.path.abspath(__file__))
ARQ = os.path.join(DIR, ARQ)

def ler_produtos():
    produtos = []
    try: 
        with open(ARQ, mode="r", encoding="UTF-8") as arquivo:
            for linha in arquivo:
                campos = linha.split(",")
                id, item, estoque, preco = int(campos[PRODUTO_IDX_ID]), campos[PRODUTO_IDX_NOME], int(campos[PRODUTO_IDX_ESTOQUE]), float(campos[PRODUTO_IDX_PRECO])
                produtos.append({"id": id, "item": item, "estoque": estoque, "preço": preco})
    except Exception as ex:
        print("Erro: leitura do arquivo", ex)
        exit
    return produtos

def gravar_produtos(produtos):
    try: 
        with open(ARQ, mode="w", encoding="UTF-8") as arquivo:
            for produto in produtos:
                linha_formatada = f"{produto['id']},{produto['item']},{produto['estoque']},{produto['preço']}\n"
                arquivo.write(linha_formatada)   
        print("Arquivo CSV atualizado com sucesso!")
    except Exception as ex:
        print("Erro: gravação do arquivo", ex)

        

# produtos = [
#     {"id": 1, "nome": "Produto 1", "quantidade": 1, "preco": 10},
#     {"id": 2, "nome": "Produto 2", "quantidade": 2, "preco": 20},
#     {"id": 3, "nome": "Produto 3", "quantidade": 3, "preco": 30},
#     {"id": 4, "nome": "Produto 4", "quantidade": 4, "preco": 40},
#     {"id": 5, "nome": "Produto 5", "quantidade": 5, "preco": 50}
# ]