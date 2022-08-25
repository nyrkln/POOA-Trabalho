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
from pooa.domain.obra import use_cases_interfaces

class CopiaObra(ICopiaObra):
    def __init__(self):
        self._situacao: TipoSituacao = None
        self._id: int = 0

    def get_situacao(self):
        return self._situacao


class ConsultarCopiaObraUseCase(IConsultarCopiaObraUseCase):
    def consultarCopiaObra(self,obra,id) -> CopiaObra:
        for copias in obra.copias_obra:
            if (copias._id == id):
                return copias
        return -1        # usar -1 como retorno?
        


class AlterarDadosObraUseCase(IAlterarDadosObraUseCase):#não sei se é exatamente assim o funcionamento desejado
    def alterarDadosObra(self,obra,futuraListaDeObras) -> bool:
        for indice,obras in enumerate(futuraListaDeObras):
            if obras.titulo == obra.titulo:
                futuraListaDeObras.copias_obra[indice] = obra #tava sem copias_obra
                return True
        return False
        ...

class AlterarDadosCopiaObraUseCase(IAlterarDadosCopiaObraUseCase):#não sei se é exatamente assim o funcionamento desejado
    def alterarDadosCopiaObra(self,copiaObra,obra)  -> int:
        for indice,copia in enumerate(obra.copias_obra):
            if copia._id == copiaObra._id:
                obra.copias_obra[indice] = copiaObra
                return obra.copias_obra[indice].id
        return -1         


class ConsultarCopiaObraSituacaoUseCase(IConsultarCopiaObraSituacaoUseCase):
    def consultarCopiaObraSituacao(self,obra) -> List[int]:
        situacao = []
        for obras in obra.copias_obra:
            match obras.copias_obra._situacao:
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
    def cadastrarObra(self,obraNova) :
        futuraListaDeObras = [] #lembrar de tirar - mexer com bd
        if (obraNova not in futuraListaDeObras):    
            futuraListaDeObras.append(obraNova)
            return True
        return False     
        ...


class CadastrarCopiaObraUseCase(ICadastrarCopiaObraUseCase):
    def cadastrarCopiaObra(self,obra,novaCopia) -> int:
        if (id not in copias_obra._id):#checar se essa comparação funciona
            copias_obra.append(novaCopia)
            return novaCopia.id
        return -1    
        ...


class ListarSituacaoCopiaObraUseCase(IListarSituacaoCopiaObraUseCase):
    def listarCopiaObraSituacao(self,obra) -> None:
        situacao = consultarCopiaObraSituacao(IConsultarCopiaObraSituacaoUseCase)#não tenho certeza se o parametro está certo
        for indice,estado in enumerate(situacao):
            match estado:
                case 1:
                    print("Copia " + obra.copias_obra[indice]._id + "está disponivel") 
                case 2:
                    print("Copia " + obra.copias_obra[indice]._id + "está emprestada") 
                case 3:
                    print("Copia " + obra.copias_obra[indice]._id + "está atrasada") 
                case 4:
                    print("Copia " + obra.copias_obra[indice]._id + "está reservada") 
        ...


class ReservarObraUseCase(IReservarObraUseCase):
    def reservarObra(self,obra) -> int:
        situacao = consultarCopiaObraSituacao(IConsultarCopiaObraSituacaoUseCase)
        for indice,estado in enumerate(situacao): 
            if(estado == 1):
                obra.copias_obra[indice].Reservado.trocar_situacao
                return obra.copias_obra[indice]._id
        return -1        
        ...

class EmprestarObraUseCase(IEmprestarObraUseCase):
    def emprestarObra(self,obra) -> int:
        situacao = consultarCopiaObraSituacao(IConsultarCopiaObraSituacaoUseCase)
        for indice,estado in enumerate(situacao): 
            if(estado == 1):
                obra.copias_obra[indice].Reservado.trocar_situacao
                return obra.copias_obra[indice]._id
        return -1  
        ...


class DevolverObraUseCase(IDevolverObraUseCase):
    def devolverObra(self,obra,copiaObra) -> int:
        situacao = consultarCopiaObraSituacao(IConsultarCopiaObraSituacaoUseCase)
        for indice,estado in enumerate(situacao): 
            if((obra.copias_obra[indice]._id == copiaObra._id) and (estado==3 or estado==4)):
                obra.copias_obra[indice].Disponivel.trocar_situacao
                return obra.copias_obra[indice]._id
        return -1  
        ...
