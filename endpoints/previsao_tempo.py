from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from . import schemas, crud
from . import database, get_db

router = APIRouter(prefix="/previsao-tempo", tags=["Previsão do Tempo"])

@router.post("/", response_model=schemas.PrevisaoTempo)
def create_previsao_tempo(previsao: schemas.PrevisaoTempoCreate, db: Session = Depends(get_db)):
    return crud.create_previsao_tempo(db=db, previsao=previsao)

@router.get("/{previsao_id}", response_model=schemas.PrevisaoTempo)
def get_previsao_tempo(previsao_id: int, db: Session = Depends(get_db)):
    db_previsao = crud.get_previsao_tempo(db=db, previsao_id=previsao_id)
    if db_previsao is None:
        raise HTTPException(status_code=404, detail="Previsão do tempo não encontrada")
    return db_previsao

@router.put("/{previsao_id}", response_model=schemas.PrevisaoTempo)
def update_previsao_tempo(previsao_id: int, previsao: schemas.PrevisaoTempoCreate, db: Session = Depends(get_db)):
    db_previsao = crud.get_previsao_tempo(db=db, previsao_id=previsao_id)
    if db_previsao is None:
        raise HTTPException(status_code=404, detail="Previsão do tempo não encontrada")
    return crud.update_previsao_tempo(db=db, previsao_id=previsao_id, previsao=previsao)

@router.delete("/{previsao_id}")
def delete_previsao_tempo(previsao_id: int, db: Session = Depends(get_db)):
    db_previsao = crud.get_previsao_tempo(db=db, previsao_id=previsao_id)
    if db_previsao is None:
        raise HTTPException(status_code=404, detail="Previsão do tempo não encontrada")
    crud.delete_previsao_tempo(db=db, previsao_id=previsao_id)
    return {"message": "Previsão do tempo excluída com sucesso"}

