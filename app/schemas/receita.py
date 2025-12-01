from pydantic import BaseModel
from datetime import date
from typing import Optional
from decimal import Decimal


class ReceitaBase(BaseModel):
    descricao: str
    valor: Decimal
    data: date
    categoria_receita_id: int


class ReceitaCreate(ReceitaBase):
    pass


class ReceitaUpdate(BaseModel):
    descricao: Optional[str] = None
    valor: Optional[Decimal] = None
    data: Optional[date] = None
    categoria_receita_id: Optional[int] = None


class ReceitaResponse(ReceitaBase):
    id: int

    class Config:
        from_attributes = True

