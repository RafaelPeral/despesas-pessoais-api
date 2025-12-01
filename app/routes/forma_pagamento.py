from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from app.schemas.forma_pagamento import (
    FormaPagamentoCreate,
    FormaPagamentoUpdate,
    FormaPagamentoResponse
)
from app.controllers import forma_pagamento as controller

router = APIRouter(prefix="/forma-pagamento", tags=["Forma Pagamento"])


@router.post("/", response_model=FormaPagamentoResponse, status_code=status.HTTP_201_CREATED)
async def create_forma_pagamento(
    forma: FormaPagamentoCreate,
    db: Session = Depends(get_db)
):
    return controller.create_forma_pagamento(db, forma)


@router.get("/", response_model=List[FormaPagamentoResponse])
async def list_formas_pagamento(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return controller.get_formas_pagamento(db, skip=skip, limit=limit)


@router.get("/{forma_id}", response_model=FormaPagamentoResponse)
async def get_forma_pagamento(
    forma_id: int,
    db: Session = Depends(get_db)
):
    forma = controller.get_forma_pagamento(db, forma_id)
    if not forma:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Forma de pagamento não encontrada"
        )
    return forma


@router.put("/{forma_id}", response_model=FormaPagamentoResponse)
async def update_forma_pagamento(
    forma_id: int,
    forma: FormaPagamentoUpdate,
    db: Session = Depends(get_db)
):
    updated_forma = controller.update_forma_pagamento(db, forma_id, forma)
    if not updated_forma:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Forma de pagamento não encontrada"
        )
    return updated_forma


@router.delete("/{forma_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_forma_pagamento(
    forma_id: int,
    db: Session = Depends(get_db)
):
    success = controller.delete_forma_pagamento(db, forma_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Forma de pagamento não encontrada"
        )
    return None

