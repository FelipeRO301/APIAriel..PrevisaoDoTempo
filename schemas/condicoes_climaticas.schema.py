from pydantic import BaseModel

class CondicaoClimaticaBase(BaseModel):
    descricao_condicao: str

class CondicaoClimaticaCreate(CondicaoClimaticaBase):
    pass

class CondicaoClimatica(CondicaoClimaticaBase):
    id_condicao: int

    class Config:
        orm_mode = True
