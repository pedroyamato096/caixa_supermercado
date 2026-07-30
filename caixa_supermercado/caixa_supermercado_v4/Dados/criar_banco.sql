-- Script de criação do banco de dados mercado.db
-- Execute: sqlite3 Dados/mercado.db < Dados/criar_banco.sql

CREATE TABLE IF NOT EXISTS produtos (
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    nome    TEXT    NOT NULL,
    quantidade INTEGER NOT NULL,
    preco   REAL    NOT NULL
);
