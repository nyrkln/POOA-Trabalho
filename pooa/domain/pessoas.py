"""Defines pessoas entities"""

from dataclasses import dataclass
from datetime import date
from enum import Enum
#import string


class TipoLeitor(Enum):
    ALUNO_POST = 1
    ALUNO_GRADUACAO = 2
    PROFESSOR = 3
    FUNC_EXTERNO = 4
    USUARIO_EXTERNO = 5


@dataclass
class Categoria:
    numero_dias: int
    descricao: str


@dataclass
class CatLeitor:
    tipo: TipoLeitor


class TipoUsuario(Enum):
    ADMINISTRADOR = 1
    FUNCIONARIO = 2
    LEITOR = 3
    LEITOR_ESPECIAL = 4


@dataclass
class Usario:
    nome: str
    cpf: str
    cep: str
    data_nasc: date
    telefone: str
    email: str
    usuario: TipoUsuario
    senha: str
