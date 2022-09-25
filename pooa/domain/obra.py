"""Defines obra's entities"""
from abc import ABC
from dataclasses import dataclass
from datetime import date
from enum import Enum
from typing import List
from pooa.domain.pessoas import Usuario


from pooa.shared.singleton import SingletonMeta


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


#@dataclass
class CopiaObra:
    id: int
    state: str
    locatario: str
    data_locacao: date
    data_devolucao: date
    funcionario: str

    def __init__(self,id,id_situacao,locatario,movimentacao):
        self.id = id
        if(id_situacao == 1):
            self.state = "Disponivel"
            self.locatario = '-1'
            self.funcionario = None
            self.data_devolucao = None
            self.data_locacao = None
        elif(id_situacao == 2):
            self.state = "Emprestado" 
            self.locatario = locatario
            self.funcionario = movimentacao[0]
            self.data_devolucao = movimentacao[2]
            self.data_locacao = movimentacao[1]
        elif(id_situacao == 3):
            self.state = "Atrasado" 
            self.locatario = locatario
            self.funcionario = movimentacao[0]
            self.data_devolucao = movimentacao[2]
            self.data_locacao = movimentacao[1]
        elif(id_situacao == 4):
            self.state = "Reservado"
            self.locatario = locatario
            self.funcionario = movimentacao[0]
            self.data_devolucao = movimentacao[2]
            self.data_locacao = movimentacao[1]
    def get_state(self):
        return self.state
    def get_locatario(self):
        return self.locatario 
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
    editora: str
    isbn: int
    autor: str
    palavras_chave: List[str]
    data_publi: date
    nro_paginas: int
    categoria_obra: TipoObra
    copias_obra: List[CopiaObra]

