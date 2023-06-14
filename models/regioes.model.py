from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Regiao(Base):
    __tablename__ = 'regioes'

    id_regiao = Column(Integer, primary_key=True, index=True)
    nome_regiao = Column(String)
    cod_pais = Column(Integer, ForeignKey('paises.id_pais'))

    pais = relationship("Pais", back_populates="regioes")
