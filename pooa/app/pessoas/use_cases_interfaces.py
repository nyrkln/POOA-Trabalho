
from abc import ABC, abstractmethod, ABCMeta, abstractstaticmethod

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

class IUsuario(metaclass=ABCMeta):
    @abstractstaticmethod
    def usuario_method():
        ...
        
