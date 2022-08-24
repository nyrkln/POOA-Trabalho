"""Defines obra abstract interfaces"""
from abc import ABC, abstractmethod
from typing import List
from pooa.app.obra.use_cases_concrect import CopiaObra

from pooa.domain.obra import Obra


class IConsultarCopiaObraUseCase(ABC):
    @abstractmethod
    def execute(self) -> CopiaObra:
        ...


class IAlterarDadosObraUseCase(ABC):
    @abstractmethod
    def execute(self) -> CopiaObra:
        ...


class IConsultarCopiaObraSituacaoUseCase(ABC):
    @abstractmethod
    def execute(self) -> List[CopiaObra]:
        ...


class ICadastrarObraUseCase(ABC):
    @abstractmethod
    def execute(self) -> Obra:
        ...


class ICadastrarCopiaObraUseCase(ABC):
    @abstractmethod
    def execute(self) -> CopiaObra:
        ...


class IListarSituacaoCopiaObraUseCase(ABC):
    @abstractmethod
    def execute(self) -> None:
        ...


class ICopiaObra(ABC):
    @abstractmethod
    def criar_obra(self) -> Obra:
        ...


class IReservarObraUseCase(ABC):
    @abstractmethod
    def execute(self):
        ...


class IEmprestarObraUseCase(ABC):
    @abstractmethod
    def execute(self):
        ...


class IDevolverObraUseCase(ABC):
    @abstractmethod
    def execute(self):
        ...
