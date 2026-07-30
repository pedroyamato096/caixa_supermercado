from importar_dados import importar_dados_iniciais
from menus import exibir_menu_caixa, exibir_fechamento_caixa
from atendimento import realizar_atendimento
from fechamento_caixa import calcular_total_vendas
from constantes import OPCAO_INICIAR_ATENDIMENTO, OPCAO_FECHAR_CAIXA
from util import retornar_data_hora
from crud.cliente_crud import consultar_ou_cadastrar
import service.produto_service as service


def _registrar_venda(historico: list, nome_cliente: str, total: float):
    historico.append([nome_cliente, total])


def _processar_fechamento(historico: list):
    total_caixa = calcular_total_vendas(historico)
    sem_estoque = service.obter_produtos_sem_estoque()
    data_hora   = retornar_data_hora()
    exibir_fechamento_caixa(historico, total_caixa, sem_estoque, data_hora)


def iniciar_sistema():
    importar_dados_iniciais()

    historico    = []
    caixa_aberto = True

    while caixa_aberto:
        opcao = exibir_menu_caixa()

        if opcao == OPCAO_INICIAR_ATENDIMENTO:
            cliente = consultar_ou_cadastrar()
            total   = realizar_atendimento(cliente)
            _registrar_venda(historico, cliente.nome, total)

        elif opcao == OPCAO_FECHAR_CAIXA:
            _processar_fechamento(historico)
            caixa_aberto = False

        else:
            print("Erro: Opção inválida. Tente novamente.")


if __name__ == "__main__":
    iniciar_sistema()
