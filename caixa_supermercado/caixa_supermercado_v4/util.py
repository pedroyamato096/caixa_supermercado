from datetime import datetime


def validar_inteiro(msg: str, erro: str) -> int:
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print(erro)


def validar_float(msg: str, erro: str) -> float:
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print(erro)


def obter_opcao_valida(mensagem: str, opcoes_validas: list) -> int:
    while True:
        try:
            opcao = int(input(mensagem).strip())
            if opcao in opcoes_validas:
                return opcao
            print("Erro: Opção inválida. Tente novamente.")
        except ValueError:
            print("Erro: Digite apenas números inteiros.")


def retornar_data_hora() -> str:
    return datetime.now().strftime("%d/%m/%Y %H:%M")


def entrar_id_produto(produtos: list) -> int:
    import produto_service as service
    while True:
        id = validar_inteiro("ID do produto: ", "Erro: Digite um id válido!")
        try:
            service.consultar(id)
            return id
        except ValueError:
            print("Erro: Produto não encontrado! Tente novamente.")


def entrar_qtd() -> int:
    while True:
        qtd = validar_inteiro("Quantidade: ", "Erro: Digite uma quantidade válida!")
        if qtd > 0:
            return qtd
        print("Erro: Quantidade deve ser maior que 0!")
