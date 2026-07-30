# 🛒 Sistema de Caixa de Supermercado

Sistema de caixa para um pequeno supermercado desenvolvido em Python durante a disciplina de Programação em Backend. O projeto foi construído em etapas ao longo do semestre, cada versão adicionando novas funcionalidades e refatorando o que já existia.

---

## 🚀 Evolução do projeto

### TP1 — Primeira versão
Lógica básica do caixa usando apenas listas e tuplas. O programa abre o caixa, atende vários clientes, emite nota fiscal para cada um e exibe um extrato no fechamento com o total de vendas e os produtos sem estoque.

### TP2 — Leitura de arquivo e dicionários
Os produtos passaram a ser carregados de um arquivo CSV e armazenados como dicionários. Ao fechar o caixa, o estoque atualizado é gravado de volta no arquivo.

### TP3 — Orientação a Objetos
Criação da classe Produto com construtor, métodos e __str__. Os produtos passaram a ser objetos instanciados a partir do CSV.

### TP4 — Banco de dados e arquitetura em camadas
Maior refatoração do projeto. Os produtos passaram a ser persistidos em um banco SQLite, com importação via Pandas e SQLAlchemy. O código foi reorganizado em camadas:

- produto_repository.py — acesso ao banco (CRUD)
- produto_service.py — regras de negócio e validações
- produto_crud.py — interface administrativa
- produto_cliente.py — testes da camada de serviço

A nota fiscal também ganhou agrupamento de itens duplicados usando Pandas.

---

## 🛠️ Tecnologias

- Python 3
- Pandas
- SQLAlchemy
- SQLite
- Tabulate

---

## ▶️ Como rodar

Instala as dependências:
pip install pandas sqlalchemy tabulate

Cria o banco antes de rodar pela primeira vez:
sqlite3 Dados/mercado.db < Dados/criar_banco.sql

Inicia o sistema:
python main.py

---

## 📌 Observações

- O banco não é criado pelo código, precisa rodar o script SQL antes
- A importação do CSV acontece automaticamente ao abrir o caixa
- Nenhuma variável global foi utilizada, tudo é feito por passagem de parâmetros