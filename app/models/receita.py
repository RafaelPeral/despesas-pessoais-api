from sqlalchemy import Column, Integer, String, Numeric, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Receita(Base):
    __tablename__ = "receita"

    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String, nullable=False)
    valor = Column(Numeric(10, 2), nullable=False)
    data = Column(Date, nullable=False)
    categoria_receita_id = Column(Integer, ForeignKey("categoria_receita.id"), nullable=False)

    categoria_receita = relationship("CategoriaReceita", backref="receitas")

