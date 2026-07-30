import os
import sys
import json
import pandas as pd
import requests
from bs4 import BeautifulSoup

from constantes import (
    DADOS_DIR, CSV_NOME_ARQUIVO, JSON_CLIENTES_ARQUIVO,
    DB_TABELA_PRODUTOS, DB_TABELA_CLIENTES, URL_PRODUTOS
)
from db_conexao import criar_engine


def _caminho_dados(nome_arquivo: str) -> str:
    base = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base, DADOS_DIR, nome_arquivo)


def caminho_csv() -> str:
    return _caminho_dados(CSV_NOME_ARQUIVO)


def caminho_json_clientes() -> str:
    return _caminho_dados(JSON_CLIENTES_ARQUIVO)


def _buscar_html(url: str) -> str:
    resposta = requests.get(url, timeout=10)
    resposta.raise_for_status()
    return resposta.text


def _extrair_produtos_do_html(html: str) -> list[dict]:
    soup     = BeautifulSoup(html, "html.parser")
    lista    = soup.find("div", id="produtos-lista")
    produtos = []

    for item in lista.find_all("div", class_="product-item"):
        card_body  = item.find("div", class_="card-body")
        nome       = card_body.find("h5", class_="card-title").get_text(strip=True)
        preco_txt  = card_body.find("p", class_="card-price").get_text(strip=True)
        quantidade = int(item.find("p", attrs={"data-qtd": True})["data-qtd"])
        preco      = float(preco_txt.replace("Valor:", "").replace("R$", "").replace(",", ".").replace("\xa0", "").strip())

        produtos.append({
            "nome":       nome,
            "quantidade": quantidade,
            "preco":      preco,
        })

    return produtos


def _salvar_csv(produtos: list[dict], caminho: str):
    df = pd.DataFrame(produtos)
    df.to_csv(caminho, index=False)


def gerar_csv_por_scraping():
    try:
        html     = _buscar_html(URL_PRODUTOS)
        produtos = _extrair_produtos_do_html(html)
        _salvar_csv(produtos, caminho_csv())
        print(f"CSV gerado com {len(produtos)} produto(s).")
    except Exception as erro:
        print(f"Erro no web scraping: {erro}")
        sys.exit(1)


def _tabela_ja_populada(tabela: str) -> bool:
    engine = criar_engine()
    with engine.connect() as con:
        resultado = con.execute(
            __import__("sqlalchemy").text(f"SELECT COUNT(*) FROM {tabela}")
        )
        return resultado.scalar() > 0


def _ler_csv() -> pd.DataFrame:
    return pd.read_csv(caminho_csv())


def _inserir_dataframe(df: pd.DataFrame, tabela: str):
    engine = criar_engine()
    df.to_sql(tabela, engine, if_exists="append", index=False)


def importar_produtos():
    engine = criar_engine()
    with engine.connect() as con:
        con.execute(__import__("sqlalchemy").text(f"DELETE FROM {DB_TABELA_PRODUTOS}"))
        con.execute(__import__("sqlalchemy").text(f"DELETE FROM sqlite_sequence WHERE name='{DB_TABELA_PRODUTOS}'"))
        con.commit()
    df = _ler_csv()
    _inserir_dataframe(df, DB_TABELA_PRODUTOS)
    print(f"{len(df)} produto(s) importado(s) para o banco.")


def _ler_json_clientes() -> pd.DataFrame:
    with open(caminho_json_clientes(), encoding="utf-8") as f:
        dados = json.load(f)
    return pd.DataFrame(dados)


def importar_clientes():
    if _tabela_ja_populada(DB_TABELA_CLIENTES):
        return
    df = _ler_json_clientes()
    _inserir_dataframe(df, DB_TABELA_CLIENTES)
    print(f"{len(df)} cliente(s) importado(s) para o banco.")


def importar_dados_iniciais():
    try:
        gerar_csv_por_scraping()
        importar_produtos()
        importar_clientes()
    except Exception as erro:
        print(f"Erro ao importar dados iniciais: {erro}")
        sys.exit(1)
