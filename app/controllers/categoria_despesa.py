from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.categoria_despesa import CategoriaDespesa
from app.schemas.categoria_despesa import CategoriaDespesaCreate, CategoriaDespesaUpdate


def get_categoria_despesa(db: Session, categoria_id: int) -> Optional[CategoriaDespesa]:
    return db.query(CategoriaDespesa).filter(CategoriaDespesa.id == categoria_id).first()


def get_categorias_despesa(db: Session, skip: int = 0, limit: int = 100) -> List[CategoriaDespesa]:
    return db.query(CategoriaDespesa).offset(skip).limit(limit).all()


def create_categoria_despesa(db: Session, categoria: CategoriaDespesaCreate) -> CategoriaDespesa:
    db_categoria = CategoriaDespesa(**categoria.model_dump())
    db.add(db_categoria)
    db.commit()
    db.refresh(db_categoria)
    return db_categoria


def update_categoria_despesa(
    db: Session, categoria_id: int, categoria: CategoriaDespesaUpdate
) -> Optional[CategoriaDespesa]:
    db_categoria = get_categoria_despesa(db, categoria_id)
    if not db_categoria:
        return None
    
    update_data = categoria.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_categoria, field, value)
    
    db.commit()
    db.refresh(db_categoria)
    return db_categoria


def delete_categoria_despesa(db: Session, categoria_id: int) -> bool:
    db_categoria = get_categoria_despesa(db, categoria_id)
    if not db_categoria:
        return False
    
    db.delete(db_categoria)
    db.commit()
    return True

