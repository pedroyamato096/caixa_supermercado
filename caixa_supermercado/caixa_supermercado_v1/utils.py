def validar_inteiros(mensagem, valor_minimo, valor_maximo, erro):
    while True:
        operacao = input(mensagem)
        if not operacao.isdigit():
            print("Erro: Digite apenas números!")
            continue
        valor = int(operacao)
        if valor_minimo <= valor <= valor_maximo:
            return valor
        print(erro)

def validar_quantidade_produtos(mensagem):
    while True:
        qtd = input(mensagem)

        if not qtd.isdigit():
            print("Erro: Digite apenas números!")
            continue

        qtd_total = int(qtd)

        if qtd_total <= 0:
            print("Erro: A quantidade precisa ser maior que 0")
            continue
        else:
            return qtd_total


            
        