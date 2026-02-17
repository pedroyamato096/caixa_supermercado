from tabulate import tabulate
from utils import validar_inteiros

def menu_abertura_caixa():
    largura = 50
    opcoes = f"{'1- Iniciar Atendimento'.ljust(largura)}\n{'2- Fechar Caixa'.ljust(largura)}"
    mensagens = [["CAIXA DO SUPERMERCADO"], [opcoes]]
    print(tabulate(mensagens, tablefmt="double_grid"))


def entrar_operacao_caixa():
    menu_abertura_caixa() 
    return validar_inteiros("Entre com a operação desejada:", 1, 2)

def menu_caixa_aberto():
    mensagem = [["CAIXA ABERTO"]]
    print(tabulate(mensagem, tablefmt="simple"))