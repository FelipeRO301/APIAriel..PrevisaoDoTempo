from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from . import schemas, crud
from . import database, get_db

router = APIRouter(prefix="/condicoes-climaticas", tags=["Condições Climáticas"])

@router.post("/", response_model=schemas.CondicaoClimatica)
def create_condicao_climatica(condicao: schemas.CondicaoClimaticaCreate, db: Session = Depends(get_db)):
    return crud.create_condicao_climatica(db=db, condicao=condicao)


@router.get("/{condicao_id}", response_model=schemas.CondicaoClimatica)
def get_condicao_climatica(condicao_id: int, db: Session = Depends(get_db)):
    db_condicao = crud.get_condicao_climatica(db=db, condicao_id=condicao_id)
    if db_condicao is None:
        raise HTTPException(status_code=404, detail="Condição climática não encontrada")
    return db_condicao

@router.put("/{condicao_id}", response_model=schemas.CondicaoClimatica)
def update_condicao_climatica(condicao_id: int, condicao: schemas.CondicaoClimaticaCreate, db: Session = Depends(get_db)):
    db_condicao = crud.get_condicao_climatica(db=db, condicao_id=condicao_id)
    if db_condicao is None:
        raise HTTPException(status_code=404, detail="Condição climática não encontrada")
    return crud.update_condicao_climatica(db=db, condicao_id=condicao_id, condicao=condicao)

@router.delete("/{condicao_id}")
def delete_condicao_climatica(condicao_id: int, db: Session = Depends(get_db)):
    db_condicao = crud.get_condicao_climatica(db=db, condicao_id=condicao_id)
    if db_condicao is None:
        raise HTTPException(status_code=404, detail="Condição climática não encontrada")
    crud.delete_condicao_climatica(db=db, condicao_id=condicao_id)
    return {"message": "Condição climática excluída com sucesso"}

