from models.configs.base import Base
from sqlalchemy import Column, Integer, String

class categoriadespesa(Base):
    __tablename__ = "categoria_despesa"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)