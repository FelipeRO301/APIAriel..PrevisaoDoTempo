from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class CondicaoClimatica(Base):
    __tablename__ = 'condicoes_climaticas'

    id_condicao = Column(Integer, primary_key=True, index=True)
    descricao_condicao = Column(String)
