import pandas as pd
from constantes import ITEM_IDX_PRECO_TOT


def criar_item_compra(id_item: int, id_produto: int, nome: str, preco: float, quantidade: int) -> list:
    return [id_item, nome, quantidade, preco, preco * quantidade]


def calcular_total_compra(carrinho: list) -> float:
    return sum(item[ITEM_IDX_PRECO_TOT] for item in carrinho)


def agrupar_carrinho(carrinho: list) -> list:
    if not carrinho:
        return []

    colunas  = ["id", "nome", "quantidade", "preco_un", "preco_tot"]
    df       = pd.DataFrame(carrinho, columns=colunas)

    agrupado = (
        df.groupby("nome", sort=True)
          .agg(quantidade=("quantidade", "sum"),
               preco_un=("preco_un", "first"))
          .reset_index()
    )
    agrupado["preco_tot"] = agrupado["quantidade"] * agrupado["preco_un"]
    agrupado.insert(0, "id", range(1, len(agrupado) + 1))

    return agrupado[["id", "nome", "quantidade", "preco_un", "preco_tot"]].values.tolist()
