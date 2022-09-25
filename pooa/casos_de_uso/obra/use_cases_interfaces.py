"""Defines obra abstract interfaces"""
from abc import ABC, abstractmethod
from typing import List
from pooa.entidades.obra import Obra, CopiaObra


class IConsultarCopiaObraUseCase(ABC):
    @abstractmethod
    def consultarCopiaObra(obra,id) -> CopiaObra:
        pass

class IAlterarDadosObraUseCase(ABC):
    @abstractmethod
    def alterarDadosObra(self) -> Obra:
        pass

class IConsultarObrasAtrasadasUseCase(ABC): 
    @abstractmethod
    def consultarObrasAtrasadas(listadeobras,listadepessoas) -> list:
        pass    

class IConsultarCopiaObraSituacaoUseCase(ABC): 
    @abstractmethod
    def consultarCopiaObraSituacao(obra,listaDeObras) -> List[int]:
        pass

class ICadastrarObraUseCase(ABC):
    @abstractmethod
    def cadastrarObra(obraNova,futuraListaDeObras, id) -> list:
        pass

class IRemoverObraUseCase(ABC):
    @abstractmethod
    def removerObra(obra,listaDeObras) -> List:
        pass

class ICadastrarCopiaObraUseCase(ABC):
    @abstractmethod
    def cadastrarCopiaObra(obra,novaCopia,id) -> Obra:
        pass

class IListarSituacaoCopiaObraUseCase(ABC):
    @abstractmethod
    def listarCopiaObraSituacao(obra,listaDeObras) -> list:
        pass

class IReservarObraUseCase(ABC):
    @abstractmethod
    def reservarObra(obra,listaDeObras,locatario,funcionario) -> list: 
        pass

class IEmprestarObraUseCase(ABC):
    @abstractmethod
    def emprestarObra(obra,listaDeObras,locatario,funcionario) -> list: 
        pass

class IDevolverObraUseCase(ABC):
    @abstractmethod
    def devolverObra(obra,listaDeObras,idCopia) -> list:
        pass
