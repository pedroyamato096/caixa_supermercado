from tabulate import tabulate

def menu_abertura_caixa():
    largura = 50
    opcoes = f"{'1- Iniciar Atendimento'.ljust(largura)}\n{'2- Fechar Caixa'.ljust(largura)}"
    mensagens = [["CAIXA DO SUPERMERCADO"], [opcoes]]
    print(tabulate(mensagens, tablefmt="double_grid"))


def entrar_operacao_caixa():
    menu_abertura_caixa() 
    while True:
        opcao = input("Entre com a operação desejada: ")
        if opcao.isdigit():
            opcao_caixa = int(opcao)
            if 1 <= opcao_caixa <= 2:
                break
            else:
                print("Erro: operação inválida!")
        else:
            print("Erro: Digite apenas números!")  
    return opcao_caixa

entrar_operacao_caixa()
