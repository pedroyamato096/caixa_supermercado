from tabulate import tabulate

def abertura_caixa(titulo, op1, op2):
    largura = 50
    opcoes = f"{op1.ljust(largura)}\n{op2.ljust(largura)}"
    mensagens = [[titulo], [opcoes]]
    print(tabulate(mensagens, tablefmt="double_grid"))

titulo = "CAIXA DO SUPERMERCADO"
op1 = "1- Iniciar Atendimento"
op2 = "2- Fechar Caixa"
abertura_caixa(titulo, op1, op2)
