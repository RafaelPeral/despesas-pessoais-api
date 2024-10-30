from models.configs.base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class FormaPagamento(Base):
    __tablename__ = "forma_pagamento"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)

    receitas = relationship("Receita", back_populates="forma_pagamento", lazy='subquery')
    despesas = relationship("Despesa", back_populates="forma_pagamento", lazy='subquery')