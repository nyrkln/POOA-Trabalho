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
class CategoriaLeitor(Categoria):
    tipo: TipoLeitor


class TipoUsuario(Enum):
    ADMINISTRADOR = 1
    FUNCIONARIO = 2
    LEITOR = 3
    LEITOR_ESPECIAL = 4


@dataclass
class Usuario:
    nome: str
    cpf: str
    cep: str
    data_nasc: date
    telefone: str
    email: str
    usuario: TipoUsuario
    senha: str
    
@dataclass
class Funcionario(Usuario):
    identificacao: int
    
@dataclass
class Leitor(Usuario):
    grupoAcademico: bool
    
class UsuarioFactory:
    def build_usuario(tipo_usuario):
        if tipo_usuario == Funcionario:
            return Funcionario()
        if tipo_usuario == Leitor:
            return Leitor()
        print("Tipo Inválido")
        return -1
        
