from models.configs.base import Base
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from datetime import datetime

class Despesa(Base):
    __tablename__ = "despesa"

    id = Column(Integer, primary_key=True, autoincrement=True)
    categoria = Column(String(100), ForeignKey("categoria_despesa.name"), nullable=False)
    name = Column(String(100), nullable=False)
    date = Column(DateTime, default=datetime.utcnow,nullable=False)
    forma_pagamento = Column(String(100), ForeignKey("forma_pagamento.name"), nullable=False)
    valor = Column(Float, nullable=False)
