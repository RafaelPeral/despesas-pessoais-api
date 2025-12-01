from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from app.schemas.receita import (
    ReceitaCreate,
    ReceitaUpdate,
    ReceitaResponse
)
from app.controllers import receita as controller

router = APIRouter(prefix="/receita", tags=["Receita"])


@router.post("/", response_model=ReceitaResponse, status_code=status.HTTP_201_CREATED)
async def create_receita(
    receita: ReceitaCreate,
    db: Session = Depends(get_db)
):
    return controller.create_receita(db, receita)


@router.get("/", response_model=List[ReceitaResponse])
async def list_receitas(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return controller.get_receitas(db, skip=skip, limit=limit)


@router.get("/{receita_id}", response_model=ReceitaResponse)
async def get_receita(
    receita_id: int,
    db: Session = Depends(get_db)
):
    receita = controller.get_receita(db, receita_id)
    if not receita:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Receita não encontrada"
        )
    return receita


@router.put("/{receita_id}", response_model=ReceitaResponse)
async def update_receita(
    receita_id: int,
    receita: ReceitaUpdate,
    db: Session = Depends(get_db)
):
    updated_receita = controller.update_receita(db, receita_id, receita)
    if not updated_receita:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Receita não encontrada"
        )
    return updated_receita


@router.delete("/{receita_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_receita(
    receita_id: int,
    db: Session = Depends(get_db)
):
    success = controller.delete_receita(db, receita_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Receita não encontrada"
        )
    return None

