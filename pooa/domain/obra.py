"""Defines obra's entities"""
from abc import ABC
from dataclasses import dataclass
from datetime import date
from enum import Enum
from typing import List

from pooa.shared.singleton import SingletonMeta


@dataclass
class Autor:
    """Autor entity"""
    primeiro_nome: str
    nacionalidade: str
    segundo_nome: str


@dataclass
class Editora:
    """Editora entity"""
    nome: str
    cnpj: str


class TipoObra(Enum):
    """Tipo obra enum"""
    DISSERT_MESTRADO = 1
    TESE_DOUTORADO = 2
    RELATORIO_TECNICO = 3
    PERIODICO = 4
    LIVRO = 5
    JORNAL = 6
    NOTA_DIDATICA = 7
    REVISTA = 8


@dataclass
class CategoriaObra:
    """Categoria da Obra"""
    taxa: float
    obra: TipoObra


@dataclass
class Obra:
    """Obra concreta"""
    titulo: str
    editora: Editora
    isbn: int
    editora: Autor
    palavras_chave: List[str]
    data_publi: date
    nro_paginas: int
    categoria_obra: CategoriaObra
    copias_obra: List[CopiaObra]



class TipoSituacao:
    def __init__(self):
        self._state = Disponivel


class Disponivel(TipoSituacao, metaclass=SingletonMeta):
    def __init__(self, tipo_state: TipoSituacao):
        self._tipo_state = tipo_state

    def trocar_situacao(self):
        self._tipo_state._state = self


class Emprestado(TipoSituacao, metaclass=SingletonMeta):
    def __init__(self, tipo_state: TipoSituacao):
        self._tipo_state = tipo_state

    def trocar_situacao(self):
        self._tipo_state._state = self


class Reservado(TipoSituacao, metaclass=SingletonMeta):
    def __init__(self, tipo_state: TipoSituacao):
        self._tipo_state = tipo_state

    def trocar_situacao(self):
        self._tipo_state._state = self


class Atrasado(TipoSituacao, metaclass=SingletonMeta):
    def __init__(self, tipo_state: TipoSituacao):
        self._tipo_state = tipo_state

    def trocar_situacao(self):
        self._tipo_state._state = self



