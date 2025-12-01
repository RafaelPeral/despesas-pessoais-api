from fastapi import APIRouter
from app.routes import categoria_despesa
from app.routes import categoria_receita
from app.routes import despesa
from app.routes import forma_pagamento
from app.routes import receita

# Create main router
api_router = APIRouter()

# Include all route modules
api_router.include_router(categoria_despesa.router)
api_router.include_router(categoria_receita.router)
api_router.include_router(despesa.router)
api_router.include_router(forma_pagamento.router)
api_router.include_router(receita.router)

__all__ = ["api_router"]

