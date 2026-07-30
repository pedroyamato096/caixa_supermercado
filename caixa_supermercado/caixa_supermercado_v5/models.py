from sqlalchemy import Column, Integer, String, Float
from db_conexao import Base
from constantes import DB_TABELA_PRODUTOS, DB_TABELA_CLIENTES


class Produto(Base):
    __tablename__ = DB_TABELA_PRODUTOS

    id         = Column(Integer, primary_key=True, autoincrement=True)
    nome       = Column(String, nullable=False)
    quantidade = Column(Integer, nullable=False)
    preco      = Column(Float, nullable=False)

    def __str__(self):
        return f"[{self.id}] {self.nome} | Qtd: {self.quantidade} | R$ {self.preco:.2f}"

    def tem_estoque_para(self, quantidade: int) -> bool:
        return self.quantidade >= quantidade

    def descontar(self, quantidade: int):
        self.quantidade -= quantidade

    @classmethod
    def from_row(cls, linha: tuple) -> "Produto":
        return cls(id=linha[0], nome=linha[1], quantidade=linha[2], preco=linha[3])


class Cliente(Base):
    __tablename__ = DB_TABELA_CLIENTES

    id   = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)

    def __str__(self):
        return f"[{self.id}] {self.nome}"
