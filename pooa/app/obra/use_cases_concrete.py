import datetime
from pooa.domain.obra import Obra, CopiaObra
from pickle import TRUE
from typing import List
import os
from pooa.domain.pessoas import TipoUsuario
from pooa.app.obra.use_cases_interfaces import (
    IAlterarDadosObraUseCase,
    ICadastrarCopiaObraUseCase,
    ICadastrarObraUseCase,
    IConsultarCopiaObraSituacaoUseCase,
    IConsultarCopiaObraUseCase,
    IDevolverObraUseCase,
    IEmprestarObraUseCase,
    IListarSituacaoCopiaObraUseCase,
    IReservarObraUseCase,
    IRemoverObraUseCase,
    IConsultarObrasAtrasadasUseCase
)

class ConsultarCopiaObraUseCase(IConsultarCopiaObraUseCase):
    def consultarCopiaObra(obra,id) -> CopiaObra:
        for copias in obra.copias_obra:
            if (copias.id == id):
                return copias
        return -1 

class ConsultarObrasAtrasadasUseCase(IConsultarObrasAtrasadasUseCase): 
    def consultarObrasAtrasadas(listadeobras,listadepessoas) -> list:
        listadedevedores = []
        listadeobrasatrasadas = []
        listadeidentificadores = []
        retorno = []
        for obras in listadeobras:
            for copias in obras.copias_obra:
                if copias.get_state() == 'Atrasado':
                    listadedevedores.append(copias.locatario)
                    listadeobrasatrasadas.append(obras.titulo)
                    listadeidentificadores.append(copias.id)      
        for indice,devedores in enumerate(listadedevedores):    
            for pessoas in listadepessoas[1]:
                if str(devedores).strip() == str(pessoas.identificador).strip():
                    print("a copia " + str(listadeidentificadores[indice]).strip()+" da obra: " + str(listadeobrasatrasadas[indice]).strip()+ " está atrasada, seu locatario é " + str(pessoas.nome).strip() + " seu telefone é " + str(pessoas.telefone).strip() + " e seu email é " + str(pessoas.email).strip())
        retorno.append(listadedevedores,listadeobrasatrasadas,listadeidentificadores)
        return retorno

class AlterarDadosObraUseCase(IAlterarDadosObraUseCase):
    def alterarDadosObra(obra,ListaDeObras) -> bool:
        for indice,obras in enumerate(ListaDeObras):
            if int(obras.isbn) == int(obra.isbn):
                lista = ListaDeObras[indice].copias_obra
                ListaDeObras[indice] = obra
                ListaDeObras[indice].copias_obra = lista 
                print("operação bem sucedida")
                return ListaDeObras
        return ListaDeObras

class RemoverObraUseCase(IRemoverObraUseCase):
    def removerObra(obra,ListaDeObras) -> list:
        for indice,obras in enumerate(ListaDeObras):
            if int(obras.isbn) == int(obra.isbn):
                ListaDeObras.pop(indice)
                print("operação bem sucedida")
                return ListaDeObras
        return ListaDeObras  

class ConsultarCopiaObraSituacaoUseCase(IConsultarCopiaObraSituacaoUseCase):
    def consultarCopiaObraSituacao(obra,listaDeObras) -> List[int]:
        indiceBusca = 0
        for indice,obras in enumerate(listaDeObras):
            if(int(obra.isbn) == int(obras.isbn)):
                indiceBusca = indice       
        situacao = []
        for obras in listaDeObras[indiceBusca].copias_obra:
            if (obras.get_state() == 'Disponivel'):
                    situacao.append(1)
            elif (obras.get_state() == 'Emprestado'):
                    situacao.append(2)
            elif (obras.get_state() == 'Atrasado'):
                    situacao.append(3)
            elif (obras.get_state() == 'Reservado'):
                    situacao.append(4)      
        return situacao
                        
class CadastrarObraUseCase(ICadastrarObraUseCase):
    def cadastrarObra(obraNova,ListaDeObras,isbn):
        obraNova.isbn = isbn
        for obras in ListaDeObras:
            if ((str(obraNova.titulo).strip() == str(obras.titulo).strip()) and (str(obraNova.nro_paginas).strip() == str(obras.nro_paginas).strip()) ):
                print("obra já cadastrada")
                return ListaDeObras
        ListaDeObras.append(obraNova)
        print("operação bem sucedida")
        return ListaDeObras

class CadastrarCopiaObraUseCase(ICadastrarCopiaObraUseCase):
    def cadastrarCopiaObra(obra,novaCopia,id) -> Obra:
        novaCopia.id = id
        obra.copias_obra.append(novaCopia)
        print("operação bem sucedida")
        return obra        

class ListarSituacaoCopiaObraUseCase(IListarSituacaoCopiaObraUseCase):
    def listarCopiaObraSituacao(obra,listaDeObras) -> List:
        indiceBusca = 0
        for indice,obras in enumerate(listaDeObras):
            if(int(obra.isbn) == int(obras.isbn)):
                indiceBusca = indice       
        situacao = []
        situacao = ConsultarCopiaObraSituacaoUseCase.consultarCopiaObraSituacao(obra,listaDeObras)
        for indice,estado in enumerate(situacao):
            if(estado == 1):
                    print("Copia " + str(listaDeObras[indiceBusca].copias_obra[indice].id) + " está disponivel") 
            elif(estado == 2):
                    print("Copia " + str(listaDeObras[indiceBusca].copias_obra[indice].id) + " está emprestada") 
            elif(estado == 3):
                    print("Copia " + str(listaDeObras[indiceBusca].copias_obra[indice].id) + " está atrasada") 
            elif(estado == 4):
                    print("Copia " + str(listaDeObras[indiceBusca].copias_obra[indice].id) + " está reservada") 
        return situacao

class ReservarObraUseCase(IReservarObraUseCase):   
    def reservarObra(obra,listaDeObras,locatario,funcionario) -> list:
        numeroObra = 0
        situacao = ConsultarCopiaObraSituacaoUseCase.consultarCopiaObraSituacao(obra,listaDeObras)
        for indice,estado in enumerate(situacao): 
            if(estado == 1 and funcionario.usuario == TipoUsuario.FUNCIONARIO and locatario.grupoAcademico == True):
                for indice2, conteudo in enumerate(listaDeObras):
                    if(int(conteudo.isbn) == int(obra.isbn)):
                        numeroObra = indice2
                        listaDeObras[numeroObra].copias_obra[indice].state = 'Reservado'
                        listaDeObras[numeroObra].copias_obra[indice].locatario = str(locatario.identificador)
                        listaDeObras[numeroObra].copias_obra[indice].data_locacao = datetime.datetime.now()
                        listaDeObras[numeroObra].copias_obra[indice].data_devolucao = listaDeObras[numeroObra].copias_obra[indice].data_locacao + datetime.timedelta(days=5)
                        listaDeObras[numeroObra].copias_obra[indice].funcionario = funcionario.identificacao
                        print("A copia de id: " + str(listaDeObras[numeroObra].copias_obra[indice].id) + " Agora está reservada")
                        return listaDeObras   
        print("Não existem obras desse título disponíveis")
        return listaDeObras        

class EmprestarObraUseCase(IEmprestarObraUseCase):
    def emprestarObra(obra,listaDeObras,locatario,funcionario) -> list:
        numeroObra = 0
        situacao = ConsultarCopiaObraSituacaoUseCase.consultarCopiaObraSituacao(obra,listaDeObras)
        for indice,estado in enumerate(situacao): 
            if(estado == 1 and funcionario.usuario == TipoUsuario.FUNCIONARIO and locatario.grupoAcademico == True):
                for indice2, conteudo in enumerate(listaDeObras):
                    if(int(conteudo.isbn) == int(obra.isbn)):
                        numeroObra = indice2
                        listaDeObras[numeroObra].copias_obra[indice].state = 'Emprestado'
                        listaDeObras[numeroObra].copias_obra[indice].locatario = str(locatario.identificador)
                        listaDeObras[numeroObra].copias_obra[indice].data_locacao = datetime.datetime.now()
                        listaDeObras[numeroObra].copias_obra[indice].data_devolucao = listaDeObras[numeroObra].copias_obra[indice].data_locacao + datetime.timedelta(days=5)
                        listaDeObras[numeroObra].copias_obra[indice].funcionario = funcionario.identificacao
                        print("A copia de id: " + str(listaDeObras[numeroObra].copias_obra[indice].id) + " Agora está emprestada")
                        return listaDeObras
        print("Não existem obras desse título disponíveis")        
        return listaDeObras              

class DevolverObraUseCase(IDevolverObraUseCase):
    def devolverObra(obra,listaDeObras,idCopia) -> list:
            numeroObra = 0
            for indice2, conteudo in enumerate(listaDeObras):
                if(int(conteudo.isbn) == int(obra.isbn)):
                    numeroObra = indice2
            situacao = ConsultarCopiaObraSituacaoUseCase.consultarCopiaObraSituacao(obra,listaDeObras)
            for indice,estado in enumerate(situacao):
                if((listaDeObras[numeroObra].copias_obra[indice].id == idCopia) and (estado == 2 or estado == 3 or estado == 4)):
                    if((datetime.date.today() - listaDeObras[numeroObra].copias_obra[indice].data_devolucao).days>0):
                        print("o usuario deve "+str(int((datetime.date.today() - listaDeObras[numeroObra].copias_obra[indice].data_devolucao).days)*3)+" reais a biblioteca")
                    listaDeObras[numeroObra].copias_obra[indice].state = 'Disponivel'
                    listaDeObras[numeroObra].copias_obra[indice].locatario = '-1'
                    listaDeObras[numeroObra].copias_obra[indice].data_locacao = None
                    listaDeObras[numeroObra].copias_obra[indice].data_devolucao = None
                    listaDeObras[numeroObra].copias_obra[indice].funcionario = None
                    print("A copia de id: " + str(listaDeObras[numeroObra].copias_obra[indice].id) + " Agora está Disponivel")
                    return listaDeObras
            print("Cópia já estava disponível Disponivel")        
            return listaDeObras   
    