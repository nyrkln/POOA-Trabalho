
from abc import ABC, abstractmethod


class IConsultarDisciplinasUseCase(ABC):
    @abstractmethod
    def consultarDisciplina(self,usuario):
        ...


class IConsultarGruposAcademicosUseCase(ABC):
    @abstractmethod
    def consultarGruposAcademicos(self,usuario):
        ...


class IAlterarDadosUsuarioUseCase(ABC):
    @abstractmethod
    def alterarDadosUsuario(self,usuario):
        ...
