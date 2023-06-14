from pydantic import BaseModel

class PrevisaoTempoBase(BaseModel):
    temperatura: float
    umidade: float
    velocidade_vento: float
    cod_cidade: int
    cod_pais: int
    cod_regiao: int
    cod_condicao: int

class PrevisaoTempoCreate(PrevisaoTempoBase):
    pass

class PrevisaoTempo(PrevisaoTempoBase):
    id_previsao: int

    class Config:
        orm_mode = True
