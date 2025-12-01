from pydantic import BaseModel
from typing import Optional


class CategoriaDespesaBase(BaseModel):
    nome: str
    descricao: Optional[str] = None


class CategoriaDespesaCreate(CategoriaDespesaBase):
    pass


class CategoriaDespesaUpdate(BaseModel):
    nome: Optional[str] = None
    descricao: Optional[str] = None


class CategoriaDespesaResponse(CategoriaDespesaBase):
    id: int

    class Config:
        from_attributes = True

