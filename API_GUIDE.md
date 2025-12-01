# API Guide - Frontend Integration

## Base URL
```
http://localhost:8000
```

## Endpoints Overview

### Health & Info
- `GET /` - API information
- `GET /health` - Health check

### Despesa (Expenses)
- `POST /despesa` - Create expense
- `GET /despesa` - List expenses (with pagination)
- `GET /despesa/{id}` - Get expense by ID
- `PUT /despesa/{id}` - Update expense
- `DELETE /despesa/{id}` - Delete expense

### Receita (Income)
- `POST /receita` - Create income
- `GET /receita` - List income (with pagination)
- `GET /receita/{id}` - Get income by ID
- `PUT /receita/{id}` - Update income
- `DELETE /receita/{id}` - Delete income

### Categoria Despesa (Expense Category)
- `POST /categoria-despesa` - Create category
- `GET /categoria-despesa` - List categories
- `GET /categoria-despesa/{id}` - Get category by ID
- `PUT /categoria-despesa/{id}` - Update category
- `DELETE /categoria-despesa/{id}` - Delete category

### Categoria Receita (Income Category)
- `POST /categoria-receita` - Create category
- `GET /categoria-receita` - List categories
- `GET /categoria-receita/{id}` - Get category by ID
- `PUT /categoria-receita/{id}` - Update category
- `DELETE /categoria-receita/{id}` - Delete category

### Forma Pagamento (Payment Method)
- `POST /forma-pagamento` - Create payment method
- `GET /forma-pagamento` - List payment methods
- `GET /forma-pagamento/{id}` - Get payment method by ID
- `PUT /forma-pagamento/{id}` - Update payment method
- `DELETE /forma-pagamento/{id}` - Delete payment method

---

## Request/Response Formats

### Despesa

**Create/Update Request:**
```json
{
  "descricao": "Compras no supermercado",
  "valor": 150.50,
  "data": "2024-01-15",
  "categoria_despesa_id": 1,
  "forma_pagamento_id": 2
}
```

**Response:**
```json
{
  "id": 1,
  "descricao": "Compras no supermercado",
  "valor": 150.50,
  "data": "2024-01-15",
  "categoria_despesa_id": 1,
  "forma_pagamento_id": 2
}
```

**Update (partial - all fields optional):**
```json
{
  "descricao": "Compras atualizadas",
  "valor": 200.00
}
```

### Receita

**Create/Update Request:**
```json
{
  "descricao": "Salário",
  "valor": 5000.00,
  "data": "2024-01-01",
  "categoria_receita_id": 1
}
```

**Response:**
```json
{
  "id": 1,
  "descricao": "Salário",
  "valor": 5000.00,
  "data": "2024-01-01",
  "categoria_receita_id": 1
}
```

### Categoria Despesa / Categoria Receita / Forma Pagamento

**Create Request:**
```json
{
  "nome": "Alimentação",
  "descricao": "Gastos com comida"
}
```

**Response:**
```json
{
  "id": 1,
  "nome": "Alimentação",
  "descricao": "Gastos com comida"
}
```

**Update (partial - all fields optional):**
```json
{
  "nome": "Alimentação Atualizada"
}
```

---

## Pagination

List endpoints support pagination via query parameters:
```
GET /despesa?skip=0&limit=10
```

- `skip`: Number of records to skip (default: 0)
- `limit`: Maximum number of records to return (default: 100)

---

## HTTP Status Codes

- `200 OK` - Success (GET, PUT)
- `201 Created` - Resource created (POST)
- `204 No Content` - Success with no body (DELETE)
- `404 Not Found` - Resource not found
- `422 Unprocessable Entity` - Validation error

---

## Error Response Format

```json
{
  "detail": "Despesa não encontrada"
}
```

---

## Example Requests

### Create Expense
```javascript
fetch('http://localhost:8000/despesa', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    descricao: "Compras",
    valor: 150.50,
    data: "2024-01-15",
    categoria_despesa_id: 1,
    forma_pagamento_id: 2
  })
})
```

### List Expenses with Pagination
```javascript
fetch('http://localhost:8000/despesa?skip=0&limit=20')
```

### Update Expense
```javascript
fetch('http://localhost:8000/despesa/1', {
  method: 'PUT',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    descricao: "Compras atualizadas",
    valor: 200.00
  })
})
```

### Delete Expense
```javascript
fetch('http://localhost:8000/despesa/1', {
  method: 'DELETE'
})
```

---

## Interactive Documentation

Access Swagger UI at: `http://localhost:8000/docs`

