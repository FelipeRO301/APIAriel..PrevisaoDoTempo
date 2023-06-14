from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from . import schemas, crud
from . import database,get_db

router = APIRouter(prefix="/regioes", tags=["Regiões"])

@router.post("/", response_model=schemas.Regiao)
def create_regiao(regiao: schemas.RegiaoCreate, db: Session = Depends(get_db)):
    return crud.create_regiao(db=db, regiao=regiao)

@router.get("/{regiao_id}", response_model=schemas.Regiao)
def get_regiao(regiao_id: int, db: Session = Depends(get_db)):
    db_regiao = crud.get_regiao(db=db, regiao_id=regiao_id)
    if db_regiao is None:
        raise HTTPException(status_code=404, detail="Região não encontrada")
    return db_regiao

@router.put("/{regiao_id}", response_model=schemas.Regiao)
def update_regiao(regiao_id: int, regiao: schemas.RegiaoCreate, db: Session = Depends(get_db)):
    db_regiao = crud.get_regiao(db=db, regiao_id=regiao_id)
    if db_regiao is None:
        raise HTTPException(status_code=404, detail="Região não encontrada")
    return crud.update_regiao(db=db, regiao_id=regiao_id, regiao=regiao)

@router.delete("/{regiao_id}")
def delete_regiao(regiao_id: int, db: Session = Depends(get_db)):
    db_regiao = crud.get_regiao(db=db, regiao_id=regiao_id)
    if db_regiao is None:
        raise HTTPException(status_code=404, detail="Região não encontrada")
    crud.delete_regiao(db=db, regiao_id=regiao_id)
    return {"message": "Região excluída com sucesso"}
