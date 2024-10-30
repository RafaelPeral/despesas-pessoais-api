from models.configs.base import Base
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship

class Receita(Base):
    __tablename__ = "receita"

    id = Column(Integer, primary_key=True, autoincrement=True)
    categoria = Column(String(100), ForeignKey("categoria_receita.name"), nullable=False)
    name = Column(String(100), nullable=False)
    date = Column(DateTime, default=datetime.utcnow, nullable=False)
    forma_pagamento_id = Column(Integer, ForeignKey("forma_pagamento.id"), nullable=False)
    valor = Column(Float, nullable=False)

    categoria_receita = relationship("CategoriaReceita", back_populates="receitas")
    forma_pagamento = relationship("FormaPagamento", back_populates="receitas")