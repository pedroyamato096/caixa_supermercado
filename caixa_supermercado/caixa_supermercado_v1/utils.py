def validar_inteiros(mensagem, valor_minimo, valor_maximo):
    while True:
        operacao = input(mensagem)
        if not operacao.isdigit():
            print("Erro: Digite apenas números!")
            continue
        valor = int(operacao)
        if valor_minimo <= valor <= valor_maximo:
            return valor
        print(f"Erro: operação inválida! Entre apenas com as opções disponíveis")