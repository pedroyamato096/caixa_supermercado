# 🛒 Sistema de Caixa de Supermercado

Sistema de caixa para um pequeno supermercado desenvolvido em Python, como projeto evolutivo da disciplina de Programação em Backend. O projeto passou por 4 etapas incrementais, cada uma adicionando novas funcionalidades e melhores práticas de desenvolvimento.

---

## 📋 Funcionalidades

- Abertura e fechamento de caixa
- Atendimento de múltiplos clientes sequencialmente
- Registro de produtos e quantidades por cliente
- Emissão de nota fiscal por atendimento (com agrupamento de itens duplicados)
- Extrato de fechamento com total de vendas e clientes atendidos
- Relatório de produtos sem estoque
- Controle de estoque com persistência em banco de dados SQLite
- Importação de produtos via arquivo CSV

---

## 🚀 Evolução do projeto

### TP1 — Base do sistema
- Estrutura inicial do caixa com lista de produtos hardcoded
- Atendimento de múltiplos clientes com identificação automática (Cliente 1, Cliente 2...)
- Nota fiscal por cliente com tabela de itens e total da compra
- Fechamento de caixa com extrato de vendas e produtos sem estoque
- Restrição: apenas listas e tuplas (sem dicionários)

### TP2 — Leitura de arquivo e dicionários
- Produtos carregados de arquivo `produtos.csv` no início do programa
- Cada produto passou a ser representado como **dicionário**
- Estoque atualizado e gravado de volta no CSV ao fechar o caixa

### TP3 — Orientação a Objetos
- Criação da **classe `Produto`** com construtor, métodos e `__str__`
- Produtos passaram a ser objetos instanciados a partir do CSV
- Manutenção de toda a lógica de negócio das versões anteriores

### TP4 — Arquitetura em camadas + banco de dados
- Banco de dados **SQLite** com script de criação separado
- Importação do CSV para o banco via **Pandas + SQLAlchemy**
- Arquitetura em camadas:
  - `produto_repository.py` — acesso direto ao banco (CRUD)
  - `produto_service.py` — regras de negócio e validações
  - `produto_crud.py` — interface administrativa
  - `produto_cliente.py` — testes das funcionalidades de serviço
- Nota fiscal com **agrupamento de produtos duplicados** via Pandas

---

## 🗂️ Estrutura do projeto (TP4)

```
projeto/
├── Dados/
│   ├── produtos.csv
│   ├── mercado.db
│   └── criar_banco.sql
├── produto_repository.py
├── produto_service.py
├── produto_crud.py
├── produto_cliente.py
├── importar_dados.py
└── main.py
```

---

## 🛠️ Tecnologias utilizadas

- **Python 3**
- **Pandas** — leitura de CSV e agrupamento de dados
- **SQLAlchemy** — engine de conexão com o banco
- **SQLite** — banco de dados local
- **Tabulate** — formatação de tabelas no terminal

---

## ▶️ Como executar

**Pré-requisitos:**
```bash
pip install pandas sqlalchemy tabulate
```

**Antes de rodar pela primeira vez**, execute o script de criação do banco:
```bash
sqlite3 Dados/mercado.db < Dados/criar_banco.sql
```

**Para iniciar o sistema:**
```bash
python main.py
```

---

## 📌 Observações

- O banco de dados **não é criado pelo código** — use o script SQL antes de rodar
- A importação do CSV para o banco ocorre automaticamente na abertura do caixa
- O sistema evita duplicação de produtos no banco em reinicializações consecutivas
- Nenhuma variável global é utilizada — toda comunicação é por passagem de parâmetros
