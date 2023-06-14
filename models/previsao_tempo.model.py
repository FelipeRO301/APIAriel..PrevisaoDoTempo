from sqlalchemy import Column, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class PrevisaoTempo(Base):
    __tablename__ = 'previsao_tempo'

    id_previsao = Column(Integer, primary_key=True, index=True)
    temperatura = Column(Float)
    umidade = Column(Float)
    velocidade_vento = Column(Float)
    cod_cidade = Column(Integer, ForeignKey('cidades.id_cidade'))
    cod_pais = Column(Integer, ForeignKey('paises.id_pais'))
    cod_regiao = Column(Integer, ForeignKey('regioes.id_regiao'))
    cod_condicao = Column(Integer, ForeignKey('condicoes_climaticas.id_condicao'))

    cidade = relationship("Cidade", back_populates="previsoes_tempo")
    pais = relationship("Pais", back_populates="previsoes_tempo")
    regiao = relationship("Regiao", back_populates="previsoes_tempo")
    condicao_climatica = relationship("CondicaoClimatica", back_populates="previsoes_tempo")
