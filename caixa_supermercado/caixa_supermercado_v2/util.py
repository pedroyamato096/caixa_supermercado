def entrar_id():
    while True:
        perguntar_id = "Entre o id do produto: " 
        erro_id = "Erro: Digite um id válido!"
        id = validar_inteiro(perguntar_id, erro_id)
        if 1 <= id <= 5:
            break
        else:
            print("Erro: id não encontrado!")    
    return id

def entrar_qtd():
    while True:
        perguntar_qtd = "Entre a quantidade do produto: " 
        erro_qtd = "Erro: Digite uma quantidade válida!"
        qtd = validar_inteiro(perguntar_qtd, erro_qtd)
        if qtd > 0:
            break
        else:
            print("Erro: quantidade deve ser maior que 0!")    
    return qtd
  
def pesquisar_produto(id, produtos):
    # essa função vai me retornar o produto pesquisado
    produto_procurado = []
    for produto in produtos:
        if produto[0] == id:
            produto_procurado = produto
            break
    return produto_procurado


def validar_inteiro(msg, erro):
    while True:
        try: 
            num = int(input(msg))
            break
        except:
            print(erro)
    return num 


def obter_opcao_valida(mensagem, opcoes_validas):
    while True:
        entrada = input(mensagem).strip()
        try:
            opcao_escolhida = int(entrada)
            if opcao_escolhida in opcoes_validas:
                return opcao_escolhida
            else:
                print(f"Erro: Opção inválida. Escolha uma das opções permitidas")          
        except ValueError:
            print("Erro: Entrada inválida. Por favor, digite apenas números inteiros.")