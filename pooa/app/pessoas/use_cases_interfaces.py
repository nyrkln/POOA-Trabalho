
from abc import ABC, abstractmethod


class IConsultarDisciplinasUseCase(ABC):
    @abstractmethod
    def execute(self):
        ...


class IConsultarGruposAcademicosUseCase(ABC):
    @abstractmethod
    def execute(self):
        ...


class IAlterarDadosUsuarioUseCase(ABC):
    @abstractmethod
    def execute(self):
        ...
