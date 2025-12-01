from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from app.schemas.despesa import (
    DespesaCreate,
    DespesaUpdate,
    DespesaResponse
)
from app.controllers import despesa as controller

router = APIRouter(prefix="/despesa", tags=["Despesa"])


@router.post("/", response_model=DespesaResponse, status_code=status.HTTP_201_CREATED)
async def create_despesa(
    despesa: DespesaCreate,
    db: Session = Depends(get_db)
):
    return controller.create_despesa(db, despesa)


@router.get("/", response_model=List[DespesaResponse])
async def list_despesas(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return controller.get_despesas(db, skip=skip, limit=limit)


@router.get("/{despesa_id}", response_model=DespesaResponse)
async def get_despesa(
    despesa_id: int,
    db: Session = Depends(get_db)
):
    despesa = controller.get_despesa(db, despesa_id)
    if not despesa:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Despesa não encontrada"
        )
    return despesa


@router.put("/{despesa_id}", response_model=DespesaResponse)
async def update_despesa(
    despesa_id: int,
    despesa: DespesaUpdate,
    db: Session = Depends(get_db)
):
    updated_despesa = controller.update_despesa(db, despesa_id, despesa)
    if not updated_despesa:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Despesa não encontrada"
        )
    return updated_despesa


@router.delete("/{despesa_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_despesa(
    despesa_id: int,
    db: Session = Depends(get_db)
):
    success = controller.delete_despesa(db, despesa_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Despesa não encontrada"
        )
    return None

