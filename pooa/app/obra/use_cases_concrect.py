from typing import List
from pooa.app.obra.use_cases_interfaces import (
    IAlterarDadosCopiaObraUseCase,
    IAlterarDadosObraUseCase,
    ICadastrarCopiaObraUseCase,
    ICadastrarObraUseCase,
    IConsultarCopiaObraSituacaoUseCase,
    IConsultarCopiaObraUseCase,
    ICopiaObra,
    IDevolverObraUseCase,
    IEmprestarObraUseCase,
    IListarSituacaoCopiaObraUseCase,
    IReservarObraUseCase
)
from pooa.domain.obra import Obra, TipoSituacao


class CopiaObra(ICopiaObra):
    def __init__(self):
        self._situacao: TipoSituacao = None
        self._id: int = 0

    def get_situacao(self):
        return self._situacao


class ConsultarCopiaObraUseCase(IConsultarCopiaObraUseCase):
    def consultarCopiaObra(self) -> CopiaObra:
        


class AlterarDadosObraUseCase(IAlterarDadosObraUseCase):
    def alterarDadosObra(self,obra) -> Obra:
        self = obra
        ...

class AlterarDadosCopiaObraUseCase(IAlterarDadosCopiaObraUseCase):
    def alterarDadosCopiaObra(self,copiaObra)  -> CopiaObra:
        self = copiaObra
        pass

class ConsultarCopiaObraSituacaoUseCase(IConsultarCopiaObraSituacaoUseCase):
    def consultarCopiaObraSituacao(self,obra) -> List[int]:
        situacao = []
        for each copia in obra.copias_obra:
            match obra.copias_obra._situacao:
                case Disponivel:
                    situacao.append(1)
                case Emprestado:
                    situacao.append(2)
                case Atrasado:
                    situacao.append(3)
                case Reservado:
                    situacao.append(4)
        return situacao

                
            
class CadastrarObraUseCase(ICadastrarObraUseCase):
    def cadastrarObra(self,obraNova) ->:
        if (obraNova != null && ObraNova not in futuraListaDeObras):    
            futuraListaDeObras.append(ObraNova)
            return True
        return False     
        ...


class CadastrarCopiaObraUseCase(ICadastrarCopiaObraUseCase):
    def cadastrarCopiaObra(self,obra,novaCopia) -> int:
        if (obraNova != null && id not in copias_obra.id):#checar se essa comparação funciona
            copias_obra.append(novaCopia)
        return novaCopia.id
        ...


class ListarSituacaoCopiaObraUseCase(IListarSituacaoCopiaObraUseCase):
    def listarCopiaObraSituacao(self,obra) -> None:
        situacao = consultarCopiaObraSituacao(IConsultarCopiaObraSituacaoUseCase)#não tenho certeza se o parametro está certo
        for indice,estado in enumerate(situacao):
            match estado:
                case 1:
                    print("Copia " obra.copias_obra[indice].id "está disponivel") 
                case 2:
                    print("Copia " obra.copias_obra[indice].id "está emprestada") 
                case 3:
                    print("Copia " obra.copias_obra[indice].id "está atrasada") 
                case 4:
                    print("Copia " obra.copias_obra[indice].id "está reservada") 
        ...


class ReservarObraUseCase(IReservarObraUseCase):
    def reservarObra(self,obra) -> int:
        situacao = consultarCopiaObraSituacao(IConsultarCopiaObraSituacaoUseCase)
        for indice,estado in enumerate(situacao): 
            if(estado == 1)
                obra.copias_obra[indice].Reservado.trocar_situacao
                return obra.copias_obra[indice].Reservado.id
        return -1        
        ...

class EmprestarObraUseCase(IEmprestarObraUseCase):
    def emprestarObra(self,obra) -> int:
        situacao = consultarCopiaObraSituacao(IConsultarCopiaObraSituacaoUseCase)
        for indice,estado in enumerate(situacao): 
            if(estado == 1)
                obra.copias_obra[indice].Reservado.trocar_situacao
                return obra.copias_obra[indice].Emprestado.id
        return -1  
        ...


class DevolverObraUseCase(IDevolverObraUseCase):
    def devolverObra(self,obra,copiaObra) -> int:
        situacao = consultarCopiaObraSituacao(IConsultarCopiaObraSituacaoUseCase)
        for indice,estado in enumerate(situacao): 
            if((obra.copias_obra[indice].id == copiaObra.id) && (estado==3||estado==4))
                obra.copias_obra[indice].Disponivel.trocar_situacao
                return 1
        return -1  
        ...
