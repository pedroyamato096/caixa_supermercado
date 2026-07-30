from caixa import abrir_caixa, menu_atendimento
from atendimento import iniciar_atendimento
from relatorios import emitir_nf, emitir_sangria
from estoque import produtos_sem_estoque


def main():
    produtos = abrir_caixa()
    id_cliente = 1
    relatorios = []
    while True:
        opcao = menu_atendimento()
        if opcao == 1:
            relatorio, id_cliente = iniciar_atendimento(produtos, id_cliente)
            if relatorio:
                emitir_nf(relatorio)
                relatorios.append(relatorio)
        elif opcao == 2:
            emitir_sangria(relatorios)
            produtos_sem_estoque(produtos)
            print("\nCaixa finalizado")
            break
main()