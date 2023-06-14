from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Pais(Base):
    __tablename__ = 'paises'

    id_pais = Column(Integer, primary_key=True, index=True)
    nome_pais = Column(String)

    regioes = relationship("Regiao", back_populates="pais")
