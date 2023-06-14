from pydantic import BaseModel

class CidadeBase(BaseModel):
    nome_cidade: str

class CidadeCreate(CidadeBase):
    cod_regiao: int

class Cidade(CidadeBase):
    id_cidade: int
    cod_regiao: int

    class Config:
        orm_mode = True
