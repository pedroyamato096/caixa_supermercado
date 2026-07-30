from importar_dados import importar_csv_para_banco
from menus import exibir_menu_caixa, exibir_fechamento_caixa
from atendimento import realizar_atendimento
from fechamento_caixa import calcular_total_vendas
from constantes import OPCAO_INICIAR_ATENDIMENTO, OPCAO_FECHAR_CAIXA
from util import retornar_data_hora
import produto_service as service


def _registrar_venda(historico: list, numero_cliente: int, total: float):
    historico.append([f"Cliente {numero_cliente}", total])


def _processar_fechamento(historico: list):
    total_caixa  = calcular_total_vendas(historico)
    sem_estoque  = service.obter_produtos_sem_estoque()
    data_hora    = retornar_data_hora()
    exibir_fechamento_caixa(historico, total_caixa, sem_estoque, data_hora)


def iniciar_sistema():
    importar_csv_para_banco()

    numero_cliente = 1
    historico      = []
    caixa_aberto   = True

    while caixa_aberto:
        opcao = exibir_menu_caixa()

        if opcao == OPCAO_INICIAR_ATENDIMENTO:
            total = realizar_atendimento(numero_cliente)
            _registrar_venda(historico, numero_cliente, total)
            numero_cliente += 1

        elif opcao == OPCAO_FECHAR_CAIXA:
            _processar_fechamento(historico)
            caixa_aberto = False

        else:
            print("Erro: Opção inválida. Tente novamente.")


if __name__ == "__main__":
    iniciar_sistema()
