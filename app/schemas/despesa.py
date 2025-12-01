from pydantic import BaseModel
from datetime import date
from typing import Optional
from decimal import Decimal


class DespesaBase(BaseModel):
    descricao: str
    valor: Decimal
    data: date
    categoria_despesa_id: int
    forma_pagamento_id: int


class DespesaCreate(DespesaBase):
    pass


class DespesaUpdate(BaseModel):
    descricao: Optional[str] = None
    valor: Optional[Decimal] = None
    data: Optional[date] = None
    categoria_despesa_id: Optional[int] = None
    forma_pagamento_id: Optional[int] = None


class DespesaResponse(DespesaBase):
    id: int

    class Config:
        from_attributes = True

