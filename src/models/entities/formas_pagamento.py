from models.configs.base import Base
from sqlalchemy import Column, Integer, String

class CategoriasReceitas(Base):
    __tablename__ = "categorias_receitas"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)