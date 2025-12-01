from sqlalchemy import Column, Integer, String
from database import Base


class CategoriaDespesa(Base):
    __tablename__ = "categoria_despesa"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False, unique=True)
    descricao = Column(String, nullable=True)

