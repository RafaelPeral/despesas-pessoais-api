from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from app.schemas.categoria_despesa import (
    CategoriaDespesaCreate,
    CategoriaDespesaUpdate,
    CategoriaDespesaResponse
)
from app.controllers import categoria_despesa as controller

router = APIRouter(prefix="/categoria-despesa", tags=["Categoria Despesa"])


@router.post("/", response_model=CategoriaDespesaResponse, status_code=status.HTTP_201_CREATED)
async def create_categoria_despesa(
    categoria: CategoriaDespesaCreate,
    db: Session = Depends(get_db)
):
    return controller.create_categoria_despesa(db, categoria)


@router.get("/", response_model=List[CategoriaDespesaResponse])
async def list_categorias_despesa(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return controller.get_categorias_despesa(db, skip=skip, limit=limit)


@router.get("/{categoria_id}", response_model=CategoriaDespesaResponse)
async def get_categoria_despesa(
    categoria_id: int,
    db: Session = Depends(get_db)
):
    categoria = controller.get_categoria_despesa(db, categoria_id)
    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Categoria de despesa não encontrada"
        )
    return categoria


@router.put("/{categoria_id}", response_model=CategoriaDespesaResponse)
async def update_categoria_despesa(
    categoria_id: int,
    categoria: CategoriaDespesaUpdate,
    db: Session = Depends(get_db)
):
    updated_categoria = controller.update_categoria_despesa(db, categoria_id, categoria)
    if not updated_categoria:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Categoria de despesa não encontrada"
        )
    return updated_categoria


@router.delete("/{categoria_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_categoria_despesa(
    categoria_id: int,
    db: Session = Depends(get_db)
):
    success = controller.delete_categoria_despesa(db, categoria_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Categoria de despesa não encontrada"
        )
    return None

