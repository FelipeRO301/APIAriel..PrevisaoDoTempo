from models import Cidade, Regiao, Pais, CondicaoClimatica, PrevisaoTempo
from schemas import (
    CidadeBase, CidadeCreate,
    RegiaoBase, RegiaoCreate,
    PaisBase, PaisCreate,
    CondicaoClimaticaBase, CondicaoClimaticaCreate,
    PrevisaoTempoBase, PrevisaoTempoCreate
)

__all__ = [
    "Cidade",
    "CidadeBase",
    "CidadeCreate",
    "Regiao",
    "RegiaoBase",
    "RegiaoCreate",
    "Pais",
    "PaisBase",
    "PaisCreate",
    "CondicaoClimatica",
    "CondicaoClimaticaBase",
    "CondicaoClimaticaCreate",
    "PrevisaoTempo",
    "PrevisaoTempoBase",
    "PrevisaoTempoCreate",
]
