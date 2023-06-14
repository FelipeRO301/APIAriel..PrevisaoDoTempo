from pydantic import BaseModel

class RegiaoBase(BaseModel):
    nome_regiao: str

class RegiaoCreate(RegiaoBase):
    cod_pais: int

class Regiao(RegiaoBase):
    id_regiao: int
    cod_pais: int

    class Config:
        orm_mode = True
