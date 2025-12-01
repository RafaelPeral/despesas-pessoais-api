from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.despesa import Despesa
from app.schemas.despesa import DespesaCreate, DespesaUpdate


def get_despesa(db: Session, despesa_id: int) -> Optional[Despesa]:
    return db.query(Despesa).filter(Despesa.id == despesa_id).first()


def get_despesas(db: Session, skip: int = 0, limit: int = 100) -> List[Despesa]:
    return db.query(Despesa).offset(skip).limit(limit).all()


def create_despesa(db: Session, despesa: DespesaCreate) -> Despesa:
    db_despesa = Despesa(**despesa.model_dump())
    db.add(db_despesa)
    db.commit()
    db.refresh(db_despesa)
    return db_despesa


def update_despesa(
    db: Session, despesa_id: int, despesa: DespesaUpdate
) -> Optional[Despesa]:
    db_despesa = get_despesa(db, despesa_id)
    if not db_despesa:
        return None
    
    update_data = despesa.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_despesa, field, value)
    
    db.commit()
    db.refresh(db_despesa)
    return db_despesa


def delete_despesa(db: Session, despesa_id: int) -> bool:
    db_despesa = get_despesa(db, despesa_id)
    if not db_despesa:
        return False
    
    db.delete(db_despesa)
    db.commit()
    return True

