from models.configs.base import Base
from sqlalchemy import Column, Integer, String

class CategoriasDespesas(Base):
    __tablename__ = "categorias_despesas"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)