from pydantic import BaseModel
from typing import Optional


class CategoriaReceitaBase(BaseModel):
    nome: str
    descricao: Optional[str] = None


class CategoriaReceitaCreate(CategoriaReceitaBase):
    pass


class CategoriaReceitaUpdate(BaseModel):
    nome: Optional[str] = None
    descricao: Optional[str] = None


class CategoriaReceitaResponse(CategoriaReceitaBase):
    id: int

    class Config:
        from_attributes = True

