from sqlalchemy import Column, Integer, String
from database import Base


class CategoriaReceita(Base):
    __tablename__ = "categoria_receita"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False, unique=True)
    descricao = Column(String, nullable=True)

