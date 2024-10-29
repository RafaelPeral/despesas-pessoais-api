from models.configs.base import Base
from sqlalchemy import Column, Integer, String

class FormaPagamento(Base):
    __tablename__ = "forma_pagamento"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)