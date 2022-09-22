"""Defines obra abstract interfaces"""
from abc import ABC, abstractmethod
from typing import List
#from pooa.app.obra.use_cases_concrect import CopiaObra

from pooa.domain.obra import Obra


class IConsultarCopiaObraUseCase(ABC):
    @abstractmethod
    def consultarCopiaObra(self):
        pass


class IAlterarDadosObraUseCase(ABC):
    @abstractmethod
    def alterarDadosObra(self) -> Obra:
        pass

class IAlterarDadosCopiaObraUseCase(ABC):
    @abstractmethod
    def alterarDadosCopiaObra(self):
        pass

class IConsultarObrasAtrasadasUseCase(ABC): 
    @abstractmethod
    def consultarObrasAtrasadas(listadeobras,listadepessoas):
        pass    


class IConsultarCopiaObraSituacaoUseCase(ABC): 
    @abstractmethod
    def consultarCopiaObraSituacao(self):
        pass


class ICadastrarObraUseCase(ABC):
    @abstractmethod
    def cadastrarObra(self,obraNova) -> Obra:
        pass

class IRemoverObraUseCase(ABC):
    @abstractmethod
    def removerObra(obra,listaDeObras) -> Obra:
        pass

class ICadastrarCopiaObraUseCase(ABC):
    @abstractmethod
    def cadastrarCopiaObra(self):
        pass


class IListarSituacaoCopiaObraUseCase(ABC):
    @abstractmethod
    def listarCopiaObraSituacao(self) -> None:
        pass


class ICopiaObra(ABC):
    @abstractmethod
    def criar_obra(self) -> Obra:
        pass


class IReservarObraUseCase(ABC):
    @abstractmethod
    def reservarObra(self) -> Obra: 
        pass


class IEmprestarObraUseCase(ABC):
    @abstractmethod
    def emprestarObra(self) -> Obra: 
        pass


class IDevolverObraUseCase(ABC):
    @abstractmethod
    def devolverObra(self) -> Obra:
        pass
