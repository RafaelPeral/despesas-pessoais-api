from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.forma_pagamento import FormaPagamento
from app.schemas.forma_pagamento import FormaPagamentoCreate, FormaPagamentoUpdate


def get_forma_pagamento(db: Session, forma_id: int) -> Optional[FormaPagamento]:
    return db.query(FormaPagamento).filter(FormaPagamento.id == forma_id).first()


def get_formas_pagamento(db: Session, skip: int = 0, limit: int = 100) -> List[FormaPagamento]:
    return db.query(FormaPagamento).offset(skip).limit(limit).all()


def create_forma_pagamento(db: Session, forma: FormaPagamentoCreate) -> FormaPagamento:
    db_forma = FormaPagamento(**forma.model_dump())
    db.add(db_forma)
    db.commit()
    db.refresh(db_forma)
    return db_forma


def update_forma_pagamento(
    db: Session, forma_id: int, forma: FormaPagamentoUpdate
) -> Optional[FormaPagamento]:
    db_forma = get_forma_pagamento(db, forma_id)
    if not db_forma:
        return None
    
    update_data = forma.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_forma, field, value)
    
    db.commit()
    db.refresh(db_forma)
    return db_forma


def delete_forma_pagamento(db: Session, forma_id: int) -> bool:
    db_forma = get_forma_pagamento(db, forma_id)
    if not db_forma:
        return False
    
    db.delete(db_forma)
    db.commit()
    return True

