"""Defines pessoas entities"""

from dataclasses import dataclass
from datetime import date
from enum import Enum
import os
import requests
import random
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
    identificador: int
    nome: str
    cpf: str
    cep: str
    data_nasc: date
    telefone: str
    email: str
    usuario: TipoUsuario
    senha: str
    

class Funcionario(Usuario):
    identificacao: int
    def __init__(self,usuario_parametro,parametro_dif):
        Usuario.__init__(self,usuario_parametro.identificador,usuario_parametro.nome,usuario_parametro.cpf,usuario_parametro.cep,usuario_parametro.data_nasc,usuario_parametro.telefone,usuario_parametro.email,usuario_parametro.usuario,usuario_parametro.senha)
        self.identificacao = parametro_dif    

@dataclass
class Administrador(Funcionario):
    pass
    
class Leitor(Usuario):
    grupoAcademico: bool
    idGrupoAcademico: int
    tipoLeitor: TipoLeitor
    materias: int
    def __init__(self,usuario_parametro,parametro_dif):
        Usuario.__init__(self,usuario_parametro.identificador,usuario_parametro.nome,usuario_parametro.cpf,usuario_parametro.cep,usuario_parametro.data_nasc,usuario_parametro.telefone,usuario_parametro.email,usuario_parametro.usuario,usuario_parametro.senha)
        if parametro_dif[0] == -1:
            self.grupoAcademico = False
            self.idGrupoAcademico = -1
        else:
            self.grupoAcademico = True
            self.idGrupoAcademico = parametro_dif[0]
        self.tipoLeitor = parametro_dif[1]
        '''if (self.tipoLeitor == TipoLeitor.ALUNO_GRADUACAO or self.tipoLeitor == TipoLeitor.ALUNO_GRADUACAO):
            x = random.randint(1,3)
            if(x==1):    
                url = 'https://inscricaodisciplinas.herokuapp.com/aluno/03dec7a5-9b4e-4d73-a87f-c00ff03d71b7/disciplinas'
            else:
                url = 'https://inscricaodisciplinas.herokuapp.com/aluno/3fa85f64-5717-4562-b3fc-2c963f66afa6/disciplinas'
            y = requests.get(url)
            self.materias = int(y.text)'''





    
class UsuarioFactory:
    def build_usuario(tipo_usuario,identificador,nome,cpf,cep,data_nasc,telefone,email,senha,parametro_dif):
        parametro = Usuario(identificador,nome,cpf,cep,data_nasc,telefone,email,tipo_usuario,senha)    
        if tipo_usuario == TipoUsuario.FUNCIONARIO:
            return Funcionario(parametro,parametro_dif)
        if tipo_usuario == TipoUsuario.LEITOR:
            return Leitor(parametro,parametro_dif)
        #if tipo_usuario == TipoUsuario.ADMINISTRADOR:
        #    return Administrador(parametro)    
        print("Tipo Inválido")
        return -1


        
