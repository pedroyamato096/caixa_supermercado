from util import *
from tabulate import tabulate
from constantes import *
from estoque import *

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

def exibir_nota_fiscal(carrinho_cliente, cliente, total_compra, data_hora):
    cabecalhos = ["Item", "Produto", "Quant.", "Preço", "Total"]
    print("\n" + "=" * 40)
    print("NOTA FISCAL".center(40))
    print("=" * 40)
    print(f"Cliente {cliente}")
    print(f"{data_hora}")
    print(tabulate(carrinho_cliente, headers=cabecalhos))
    print("-" * 40)
    print(f"Itens: {len(carrinho_cliente)}")
    print(f"TOTAL DA COMPRA: R$ {total_compra:.2f}")
    print("=" * 40 + "\n")
    

    
