from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Cidade(Base):
    __tablename__ = 'cidades'

    id_cidade = Column(Integer, primary_key=True, index=True)
    nome_cidade = Column(String)
    cod_regiao = Column(Integer, ForeignKey('regioes.id_regiao'))

    regiao = relationship("Regiao", back_populates="cidades")
