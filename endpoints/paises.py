from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from . import schemas, crud
from . import database, get_db

router = APIRouter(prefix="/paises", tags=["Países"])

@router.post("/", response_model=schemas.Pais)
def create_pais(pais: schemas.PaisCreate, db: Session = Depends(get_db)):
    return crud.create_pais(db=db, pais=pais)

@router.get("/{pais_id}", response_model=schemas.Pais)
def get_pais(pais_id: int, db: Session = Depends(get_db)):
    db_pais = crud.get_pais(db=db, pais_id=pais_id)
    if db_pais is None:
        raise HTTPException(status_code=404, detail="País não encontrado")
    return db_pais

@router.put("/{pais_id}", response_model=schemas.Pais)
def update_pais(pais_id: int, pais: schemas.PaisCreate, db: Session = Depends(get_db)):
    db_pais = crud.get_pais(db=db, pais_id=pais_id)
    if db_pais is None:
        raise HTTPException(status_code=404, detail="País não encontrado")
    return crud.update_pais(db=db, pais_id=pais_id, pais=pais)

@router.delete("/{pais_id}")
def delete_pais(pais_id: int, db: Session = Depends(get_db)):
    db_pais = crud.get_pais(db=db, pais_id=pais_id)
    if db_pais is None:
        raise HTTPException(status_code=404, detail="País não encontrado")
    crud.delete_pais(db=db, pais_id=pais_id)
    return {"message": "País excluído com sucesso"}

