from tabulate import tabulate
from utils import validar_inteiros

def abrir_caixa():
    produtos = [
        [1, "Produto 1", 1, 10],
        [2, "Produto 2", 2, 20],
        [3, "Produto 3", 3, 30],
        [4, "Produto 4", 4, 40],
        [5, "Produto 5", 5, 50]
    ]
    mensagem = [["Caixa aberto com sucesso!"]]
    print(tabulate(mensagem))
    return produtos

def menu_atendimento():
    mensagem = "1- Iniciar atendimento\n2- Finalizar atendimento\n\nDigite uma das opções: "
    erro = "Operação inválida"
    operacao = validar_inteiros(mensagem, 1, 2, erro)
    return operacao