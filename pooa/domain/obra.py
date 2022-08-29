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

#@dataclass
class CopiaObra:
    id: int
    state: str
    def __init__(self,id,id_situacao):
        self.id = id
        if(id_situacao == 1):
            self.state = "Disponivel"
        elif(id_situacao == 2):
            self.state = "Emprestado" 
        elif(id_situacao == 3):
            self.state = "Atrasado" 
        elif(id_situacao == 4):
            self.state = "Reservado"
    def get_state(self):
        return self.state
    def get_id(self):
        return self.id
    def mudar_state(self,situacao):
        if(situacao == 1):
            self.state = "Disponivel"
        elif(situacao == 2):
            self.state = "Emprestado" 
        elif(situacao == 3):
            self.state = "Atrasado" 
        elif(situacao == 4):
            self.state = "Reservado"       

@dataclass
class Obra:
    """Obra concreta"""
    titulo: str
    editora: Editora
    isbn: int
    autor: Autor
    palavras_chave: List[str]
    data_publi: date
    nro_paginas: int
    categoria_obra: CategoriaObra
    copias_obra: List[CopiaObra]
