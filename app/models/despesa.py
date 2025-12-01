from sqlalchemy import Column, Integer, String, Numeric, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Despesa(Base):
    __tablename__ = "despesa"

    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String, nullable=False)
    valor = Column(Numeric(10, 2), nullable=False)
    data = Column(Date, nullable=False)
    categoria_despesa_id = Column(Integer, ForeignKey("categoria_despesa.id"), nullable=False)
    forma_pagamento_id = Column(Integer, ForeignKey("forma_pagamento.id"), nullable=False)

    categoria_despesa = relationship("CategoriaDespesa", backref="despesas")
    forma_pagamento = relationship("FormaPagamento", backref="despesas")

