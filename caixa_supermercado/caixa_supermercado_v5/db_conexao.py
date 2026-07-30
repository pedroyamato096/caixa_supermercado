import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from constantes import DADOS_DIR, DB_NOME_ARQUIVO


class Base(DeclarativeBase):
    pass


def caminho_banco() -> str:
    base = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base, DADOS_DIR, DB_NOME_ARQUIVO)


def criar_engine():
    return create_engine(f"sqlite:///{caminho_banco()}", echo=False)


def obter_sessao():
    engine = criar_engine()
    Session = sessionmaker(bind=engine)
    return Session()
