from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from . import schemas, crud
from . import database, get_db

router = APIRouter(prefix="/cidades", tags=["Cidades"])

@router.post("/", response_model=schemas.Cidade)
def create_cidade(cidade: schemas.CidadeCreate, db: Session = Depends(get_db)):
    return crud.create_cidade(db=db, cidade=cidade)

@router.get("/{cidade_id}", response_model=schemas.Cidade)
def get_cidade(cidade_id: int, db: Session = Depends(get_db)):
    db_cidade = crud.get_cidade(db=db, cidade_id=cidade_id)
    if db_cidade is None:
        raise HTTPException(status_code=404, detail="Cidade não encontrada")
    return db_cidade

@router.put("/{cidade_id}", response_model=schemas.Cidade)
def update_cidade(cidade_id: int, cidade: schemas.CidadeCreate, db: Session = Depends(get_db)):
    db_cidade = crud.get_cidade(db=db, cidade_id=cidade_id)
    if db_cidade is None:
        raise HTTPException(status_code=404, detail="Cidade não encontrada")
    return crud.update_cidade(db=db, cidade_id=cidade_id, cidade=cidade)

@router.put("/{cidade_id}", response_model=schemas.Cidade)
def update_cidade(cidade_id: int, cidade: schemas.CidadeCreate, db: Session = Depends(get_db)):
    db_cidade = crud.get_cidade(db=db, cidade_id=cidade_id)
    if db_cidade is None:
        raise HTTPException(status_code=404, detail="Cidade não encontrada")
    return crud.update_cidade(db=db, cidade_id=cidade_id, cidade=cidade)


@router.delete("/{cidade_id}")
def delete_cidade(cidade_id: int, db: Session = Depends(get_db)):
    db_cidade = crud.get_cidade(db=db, cidade_id=cidade_id)
    if db_cidade is None:
        raise HTTPException(status_code=404, detail="Cidade não encontrada")
    crud.delete_cidade(db=db, cidade_id=cidade_id)
    return {"message": "Cidade excluída com sucesso"}
