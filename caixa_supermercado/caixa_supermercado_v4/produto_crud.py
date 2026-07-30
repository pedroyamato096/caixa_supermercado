from tabulate import tabulate
import produto_service as service
from util import validar_inteiro, validar_float, obter_opcao_valida


OPCAO_LISTAR  = 1
OPCAO_BUSCAR  = 2
OPCAO_CRIAR   = 3
OPCAO_EDITAR  = 4
OPCAO_REMOVER = 5
OPCAO_SAIR    = 6


def exibir_menu_crud() -> int:
    print("\n=== ADMINISTRAÇÃO DE PRODUTOS ===")
    print("1 - Listar todos os produtos")
    print("2 - Buscar produto por ID")
    print("3 - Criar produto")
    print("4 - Editar produto")
    print("5 - Remover produto")
    print("6 - Sair")
    return obter_opcao_valida("Opção: ", list(range(1, 7)))


def exibir_produtos(produtos):
    if not produtos:
        print("Nenhum produto cadastrado.")
        return
    dados = [[p.id, p.nome, p.quantidade, f"R$ {p.preco:.2f}"] for p in produtos]
    print(tabulate(dados, headers=["ID", "Nome", "Quantidade", "Preço"], tablefmt="fancy_grid"))


def executar_listar():
    exibir_produtos(service.listar_todos())


def executar_buscar():
    id = validar_inteiro("ID do produto: ", "ID inválido!")
    try:
        produto = service.consultar(id)
        exibir_produtos([produto])
    except ValueError as e:
        print(f"Erro: {e}")


def ler_dados_produto() -> tuple:
    nome       = input("Nome: ").strip()
    quantidade = validar_inteiro("Quantidade: ", "Quantidade inválida!")
    preco      = validar_float("Preço: ", "Preço inválido!")
    return nome, quantidade, preco


def executar_criar():
    nome, quantidade, preco = ler_dados_produto()
    try:
        id_novo = service.criar(nome, quantidade, preco)
        print(f"Produto criado com ID {id_novo}.")
    except ValueError as e:
        print(f"Erro: {e}")


def executar_editar():
    id = validar_inteiro("ID do produto a editar: ", "ID inválido!")
    nome, quantidade, preco = ler_dados_produto()
    try:
        service.atualizar(id, nome, quantidade, preco)
        print("Produto atualizado com sucesso.")
    except ValueError as e:
        print(f"Erro: {e}")


def executar_remover():
    id = validar_inteiro("ID do produto a remover: ", "ID inválido!")
    try:
        service.remover(id)
        print("Produto removido com sucesso.")
    except ValueError as e:
        print(f"Erro: {e}")


ACOES = {
    OPCAO_LISTAR:  executar_listar,
    OPCAO_BUSCAR:  executar_buscar,
    OPCAO_CRIAR:   executar_criar,
    OPCAO_EDITAR:  executar_editar,
    OPCAO_REMOVER: executar_remover,
}


def iniciar_crud():
    rodando = True
    while rodando:
        opcao = exibir_menu_crud()
        if opcao == OPCAO_SAIR:
            rodando = False
        else:
            ACOES[opcao]()


if __name__ == "__main__":
    iniciar_crud()
