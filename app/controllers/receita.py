from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.receita import Receita
from app.schemas.receita import ReceitaCreate, ReceitaUpdate


def get_receita(db: Session, receita_id: int) -> Optional[Receita]:
    return db.query(Receita).filter(Receita.id == receita_id).first()


def get_receitas(db: Session, skip: int = 0, limit: int = 100) -> List[Receita]:
    return db.query(Receita).offset(skip).limit(limit).all()


def create_receita(db: Session, receita: ReceitaCreate) -> Receita:
    db_receita = Receita(**receita.model_dump())
    db.add(db_receita)
    db.commit()
    db.refresh(db_receita)
    return db_receita


def update_receita(
    db: Session, receita_id: int, receita: ReceitaUpdate
) -> Optional[Receita]:
    db_receita = get_receita(db, receita_id)
    if not db_receita:
        return None
    
    update_data = receita.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_receita, field, value)
    
    db.commit()
    db.refresh(db_receita)
    return db_receita


def delete_receita(db: Session, receita_id: int) -> bool:
    db_receita = get_receita(db, receita_id)
    if not db_receita:
        return False
    
    db.delete(db_receita)
    db.commit()
    return True

