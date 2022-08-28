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


class IConsultarCopiaObraSituacaoUseCase(ABC): #precisa desse ou do listar?
    @abstractmethod
    def consultarCopiaObraSituacao(self):
        pass


class ICadastrarObraUseCase(ABC):
    @abstractmethod
    def cadastrarObra(self) -> Obra:
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
    def emprestarObra(self) -> Obra: #realmente é tipo Obra? ou copia obra?
        pass


class IDevolverObraUseCase(ABC):
    @abstractmethod
    def devolverObra(self) -> Obra:
        pass
