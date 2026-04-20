import os.path 
from constantes import *
from constantes import *
from models import *

ARQ = "produtos.csv"
DIR = os.path.dirname(os.path.abspath(__file__))
ARQ = os.path.join(DIR, ARQ)

def ler_produtos():
    produtos = []
    try: 
        with open(ARQ, mode="r", encoding="UTF-8") as arquivo:
            for linha in arquivo:
                campos = linha.strip().split(",")
                id, item, estoque, preco = int(campos[PRODUTO_IDX_ID]), campos[PRODUTO_IDX_NOME], int(campos[PRODUTO_IDX_ESTOQUE]), float(campos[PRODUTO_IDX_PRECO])
                produtos.append(Produto(id, item, estoque, preco))
    except Exception as ex:
        print("Erro: leitura do arquivo", ex)
        exit()
    return produtos

def gravar_produtos(produtos):
    try: 
        with open(ARQ, mode="w", encoding="UTF-8") as arquivo:
            for produto in produtos:
                linha_formatada = f"{produto.id},{produto.produto},{produto.qtd},{produto.preco}\n"
                arquivo.write(linha_formatada)   
        print("Arquivo CSV atualizado com sucesso!")
    except Exception as ex:
        print("Erro: gravação do arquivo", ex)
