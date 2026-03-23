from util import *
from tabulate import tabulate
from constantes import *

def exibir_menu_caixa():
    msg = "Entre com a opção: "
    print("\n=== MENU DO CAIXA ===")
    print(f"{OPCAO_INICIAR_ATENDIMENTO} - Iniciar Atendimento")
    print(f"{OPCAO_FECHAR_CAIXA} - Fechar Caixa")
    opcao = obter_opcao_valida(msg, [1, 2])
    return opcao

def exibir_menu_atendimento(numero_cliente): 
    msg = "Entre com a opção: "
    print(f"\n=== ATENDIMENTO: Cliente {numero_cliente} ===")
    print(f"{OPCAO_INSERIR_ITEM} - Inserir item ") 
    print(f"{OPCAO_FINALIZAR_ATENDIMENTO} - Finalizar Atendimento")
    opcao = obter_opcao_valida(msg, [1, 2])
    return opcao

    
