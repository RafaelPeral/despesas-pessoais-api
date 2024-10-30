from models.configs.base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class CategoriaDespesa(Base):
    __tablename__ = "categoria_despesa"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    
    despesas = relationship("Despesa", back_populates="categoria_despesa", lazy='subquery')