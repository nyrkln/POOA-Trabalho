
from abc import ABC, abstractmethod, ABCMeta, abstractstaticmethod
from ctypes.wintypes import BOOL
from xmlrpc.client import Boolean

class IConsultarDisciplinasUseCase(ABC):
    @abstractmethod
    def consultarDisciplina(usuario) -> Boolean:
        pass

class IConsultarPendenciasUseCase(ABC):
    @abstractmethod
    def consultarPendencias(usuario,listadeobras) -> Boolean:
        pass

class IConsultarLeitoresComPendenciasUseCase(ABC):
    @abstractmethod
    def consultarLeitoresComPendencias(listadeobras,listadepessoas) -> Boolean:
        pass                  

class IConsultarGruposAcademicosUseCase(ABC):
    @abstractmethod
    def consultarGruposAcademicos(usuario) -> bool:
        pass

class IRemoverUsuarioUseCase(ABC):
    @abstractmethod
    def removerUsuario(usuario,ListaDeUsuarios) -> list:
        pass

class IAlterarDadosUsuarioUseCase(ABC):
    @abstractmethod
    def alterarDadosUsuario(usuario,listaDeUsuarios) -> list:
        pass

class IAdicionarUsuarioUseCase(ABC):
    @abstractmethod
    def AdicionarUsuario(ListaDePessoas,pessoa,id) -> list:
        pass        

class IUsuario(metaclass=ABCMeta):
    @abstractstaticmethod
    def usuario_method():
        pass
        
