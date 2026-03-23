from util import *
from constantes import *

def atualizar_estoque(produto, qtd):
    produto[PRODUTO_IDX_ESTOQUE] -= qtd