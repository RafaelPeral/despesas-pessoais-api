from src.models.configs.base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class CategoriaReceita(Base):
    __tablename__ = "categoria_receita"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)

    receitas = relationship("Receita", back_populates="categoria_receita", lazy='subquery')