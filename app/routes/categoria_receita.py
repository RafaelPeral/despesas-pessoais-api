from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from app.schemas.categoria_receita import (
    CategoriaReceitaCreate,
    CategoriaReceitaUpdate,
    CategoriaReceitaResponse
)
from app.controllers import categoria_receita as controller

router = APIRouter(prefix="/categoria-receita", tags=["Categoria Receita"])


@router.post("/", response_model=CategoriaReceitaResponse, status_code=status.HTTP_201_CREATED)
async def create_categoria_receita(
    categoria: CategoriaReceitaCreate,
    db: Session = Depends(get_db)
):
    return controller.create_categoria_receita(db, categoria)


@router.get("/", response_model=List[CategoriaReceitaResponse])
async def list_categorias_receita(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return controller.get_categorias_receita(db, skip=skip, limit=limit)


@router.get("/{categoria_id}", response_model=CategoriaReceitaResponse)
async def get_categoria_receita(
    categoria_id: int,
    db: Session = Depends(get_db)
):
    categoria = controller.get_categoria_receita(db, categoria_id)
    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Categoria de receita não encontrada"
        )
    return categoria


@router.put("/{categoria_id}", response_model=CategoriaReceitaResponse)
async def update_categoria_receita(
    categoria_id: int,
    categoria: CategoriaReceitaUpdate,
    db: Session = Depends(get_db)
):
    updated_categoria = controller.update_categoria_receita(db, categoria_id, categoria)
    if not updated_categoria:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Categoria de receita não encontrada"
        )
    return updated_categoria


@router.delete("/{categoria_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_categoria_receita(
    categoria_id: int,
    db: Session = Depends(get_db)
):
    success = controller.delete_categoria_receita(db, categoria_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Categoria de receita não encontrada"
        )
    return None

