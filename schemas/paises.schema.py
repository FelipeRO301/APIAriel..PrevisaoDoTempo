from pydantic import BaseModel

class PaisBase(BaseModel):
    nome_pais: str

class PaisCreate(PaisBase):
    pass

class Pais(PaisBase):
    id_pais: int

    class Config:
        orm_mode = True
