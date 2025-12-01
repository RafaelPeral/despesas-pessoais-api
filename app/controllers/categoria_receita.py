from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.categoria_receita import CategoriaReceita
from app.schemas.categoria_receita import CategoriaReceitaCreate, CategoriaReceitaUpdate


def get_categoria_receita(db: Session, categoria_id: int) -> Optional[CategoriaReceita]:
    return db.query(CategoriaReceita).filter(CategoriaReceita.id == categoria_id).first()


def get_categorias_receita(db: Session, skip: int = 0, limit: int = 100) -> List[CategoriaReceita]:
    return db.query(CategoriaReceita).offset(skip).limit(limit).all()


def create_categoria_receita(db: Session, categoria: CategoriaReceitaCreate) -> CategoriaReceita:
    db_categoria = CategoriaReceita(**categoria.model_dump())
    db.add(db_categoria)
    db.commit()
    db.refresh(db_categoria)
    return db_categoria


def update_categoria_receita(
    db: Session, categoria_id: int, categoria: CategoriaReceitaUpdate
) -> Optional[CategoriaReceita]:
    db_categoria = get_categoria_receita(db, categoria_id)
    if not db_categoria:
        return None
    
    update_data = categoria.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_categoria, field, value)
    
    db.commit()
    db.refresh(db_categoria)
    return db_categoria


def delete_categoria_receita(db: Session, categoria_id: int) -> bool:
    db_categoria = get_categoria_receita(db, categoria_id)
    if not db_categoria:
        return False
    
    db.delete(db_categoria)
    db.commit()
    return True

