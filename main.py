from fastapi import FastAPI
from database import Base, engine
from app.routes import api_router
from app.schemas import RootResponse, HealthResponse
from app.models import (
    CategoriaDespesa,
    CategoriaReceita,
    Despesa,
    FormaPagamento,
    Receita
)

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Despesas Pessoais API",
    description="API para gerenciamento de despesas pessoais",
    version="2.0.0"
)

# Include routers
app.include_router(api_router)


@app.get("/", response_model=RootResponse)
async def root():
    return RootResponse(
        message="Despesas Pessoais API",
        version="2.0.0",
        docs="/docs"
    )


@app.get("/health", response_model=HealthResponse)
async def health_check():
    return HealthResponse(status="healthy")

