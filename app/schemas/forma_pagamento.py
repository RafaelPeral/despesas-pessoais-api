from pydantic import BaseModel
from typing import Optional


class FormaPagamentoBase(BaseModel):
    nome: str
    descricao: Optional[str] = None


class FormaPagamentoCreate(FormaPagamentoBase):
    pass


class FormaPagamentoUpdate(BaseModel):
    nome: Optional[str] = None
    descricao: Optional[str] = None


class FormaPagamentoResponse(FormaPagamentoBase):
    id: int

    class Config:
        from_attributes = True

