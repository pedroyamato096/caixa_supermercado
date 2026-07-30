import service.cliente_service as service
from util import validar_inteiro
from models import Cliente


def _solicitar_id_cliente() -> int:
    return validar_inteiro("ID do cliente: ", "Erro: Digite um ID válido!")


def _solicitar_nome_cliente() -> str:
    return input("Nome do cliente: ").strip()


def _exibir_cliente(cliente: Cliente):
    print(f"Cliente encontrado: {cliente}")


def consultar_ou_cadastrar() -> Cliente:
    while True:
        id_cliente = _solicitar_id_cliente()
        cliente    = service.consultar(id_cliente)

        if cliente:
            _exibir_cliente(cliente)
            return cliente

        print(f"Cliente ID {id_cliente} não encontrado. Realize o cadastro.")
        nome = _solicitar_nome_cliente()
        try:
            id_novo = service.cadastrar(nome)
            cliente = service.consultar(id_novo)
            print(f"Cliente cadastrado com sucesso: {cliente}")
            return cliente
        except ValueError as e:
            print(f"Erro: {e}")
