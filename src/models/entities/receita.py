from models.configs.base import Base
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from datetime import datetime

class Receitas(Base):
    __tablename__ = "receitas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    categoria = Column(String(100), ForeignKey("categorias_receitas.name"), nullable=False)
    name = Column(String(100), nullable=False)
    data = Column(DateTime, default=datetime.utcnow,nullable=False)
    forma_pagamento = Column(String(100), ForeignKey("formas_pagamento.name"), nullable=False)
    valor = Column(Float, nullable=False)