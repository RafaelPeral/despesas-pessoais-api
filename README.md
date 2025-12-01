# Despesas Pessoais API

API para gerenciamento de despesas pessoais construída com FastAPI, SQLAlchemy e Docker.

## 🚀 Tecnologias

- **FastAPI**: Framework web moderno e rápido para Python
- **SQLAlchemy**: ORM para Python
- **PostgreSQL**: Banco de dados relacional
- **Docker & Docker Compose**: Containerização da aplicação

## 📋 Pré-requisitos

- Docker
- Docker Compose

## 🔧 Instalação e Execução

1. **Clone o repositório** (se aplicável)

2. **Configure as variáveis de ambiente**:
   ```bash
   cp env.example .env
   ```
   Edite o arquivo `.env` conforme necessário.

3. **Inicie os containers**:
   ```bash
   docker-compose up --build
   ```

4. **Acesse a API**:
   - API: http://localhost:8000
   - Documentação interativa (Swagger): http://localhost:8000/docs
   - Documentação alternativa (ReDoc): http://localhost:8000/redoc

## 📚 Endpoints

### GET `/`
Retorna informações básicas da API.

### GET `/health`
Verifica o status de saúde da API.

### POST `/expenses`
Cria uma nova despesa.
```json
{
  "description": "Compras no supermercado",
  "amount": 150.50,
  "category": "Alimentação"
}
```

### GET `/expenses`
Lista todas as despesas (com paginação: `skip` e `limit`).

### GET `/expenses/{expense_id}`
Retorna uma despesa específica pelo ID.

### DELETE `/expenses/{expense_id}`
Remove uma despesa pelo ID.

## 🛠️ Desenvolvimento

Para desenvolvimento local sem Docker:

1. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure o banco de dados PostgreSQL** e atualize o `.env`

3. **Execute a aplicação**:
   ```bash
   uvicorn main:app --reload
   ```

## 📝 Estrutura do Projeto

```
.
├── main.py              # Aplicação FastAPI principal
├── database.py          # Configuração do SQLAlchemy
├── models.py            # Modelos do banco de dados
├── requirements.txt     # Dependências Python
├── Dockerfile           # Imagem Docker da aplicação
├── docker-compose.yml   # Orquestração dos containers
├── env.example           # Exemplo de variáveis de ambiente
└── README.md            # Este arquivo
```

## 🔐 Variáveis de Ambiente

- `DB_HOST`: Host do banco de dados (padrão: `db`)
- `DB_PORT`: Porta do banco de dados (padrão: `5432`)
- `DB_USER`: Usuário do banco de dados (padrão: `postgres`)
- `DB_PASSWORD`: Senha do banco de dados (padrão: `postgres`)
- `DB_NAME`: Nome do banco de dados (padrão: `despesas_db`)
- `API_PORT`: Porta da API (padrão: `8000`)

## 📄 Licença

Este projeto está sob a licença MIT.

