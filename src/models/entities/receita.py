from models.configs.base import Base
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from datetime import datetime

class Receitas(Base):
    __tablename__ = "receitas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    categoria = Column(String(100), ForeignKey("categorias_receitas.nome"), nullable=False)
    nome = Column(String(100), nullable=False)
    data = Column(DateTime, default=datetime.utcnow,nullable=False)
    forma_pagamento = Column(String(100), ForeignKey("formas_pagamento.nome"), nullable=False)
    valor = Column(Float, nullable=False)