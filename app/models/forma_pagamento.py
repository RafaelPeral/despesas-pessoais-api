from sqlalchemy import Column, Integer, String
from database import Base


class FormaPagamento(Base):
    __tablename__ = "forma_pagamento"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False, unique=True)
    descricao = Column(String, nullable=True)

