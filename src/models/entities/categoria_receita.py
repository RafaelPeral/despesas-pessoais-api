from models.configs.base import Base
from sqlalchemy import Column, Integer, String

class CategoriaReceita(Base):
    __tablename__ = "categoria_receita"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)