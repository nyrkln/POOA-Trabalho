
from abc import ABC, abstractmethod, ABCMeta, abstractstaticmethod

class IConsultarDisciplinasUseCase(ABC):
    @abstractmethod
    def consultarDisciplina(self,usuario):
        ...
class IConsultarPendenciasUseCase(ABC):
    def consultarPendencias(usuario,listadeobras):
        ...
class IConsultarLeitoresComPendenciasUseCase(ABC):
    def consultarLeitoresComPendencias(listadeobras,listadepessoas):
        ...                  


class IConsultarGruposAcademicosUseCase(ABC):
    @abstractmethod
    def consultarGruposAcademicos(self,usuario):
        ...

class IRemoverUsuarioUseCase(ABC):
    def removerUsuario(usuario,futuraListaDeUsuarios):
        ...

class IAlterarDadosUsuarioUseCase(ABC):
    @abstractmethod
    def alterarDadosUsuario(usuario,ListaDeUsuarios):
        ...

class IAdicionarUsuarioUseCase(ABC):
    @abstractmethod
    def AdicionarUsuario(ListaDeUsuarios,pessoa):
        ...        

class IUsuario(metaclass=ABCMeta):
    @abstractstaticmethod
    def usuario_method():
        ...
        
