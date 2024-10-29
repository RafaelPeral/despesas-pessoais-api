from models.configs.base import Base
from sqlalchemy import Column, Integer, String

class FormasPagamento(Base):
    __tablename__ = "formas_pagamento"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)