from typing import List
import os
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
from pooa.domain.obra import Atrasado, Disponivel, Emprestado, Obra, Reservado, TipoSituacao

#class CopiaObra(ICopiaObra):
    #def __init__(self):
    #    self._situacao: TipoSituacao = None
    #    self._id: int = 0

    #def get_situacao(self):
    #    return self._situacao
#    pass


class ConsultarCopiaObraUseCase(IConsultarCopiaObraUseCase):
    def consultarCopiaObra(self,obra,id):
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
            if (obras.copias_obra._state == Disponivel):
                    situacao.append(1)
            elif (obras.copias_obra._state == Emprestado):
                    situacao.append(2)
            elif (obras.copias_obra._state == Atrasado):
                    situacao.append(3)
            elif (obras.copias_obra._state == Reservado):
                    situacao.append(4)
        return situacao
                
            
class CadastrarObraUseCase(ICadastrarObraUseCase):
    def cadastrarObra(obraNova) :
        #file = open("Banco.txt", "r+")
        #file.close
        #with open('Banco.txt','r') as rf:
        PlC = ""
        with open(os.path.join("BD","id.txt"), "r+") as f:
            Id = int(f.readline())
            Isbn = int(f.readline())
            f.seek(0)
            f.truncate(0)
            f.write(str(Id))
            f.write('\n')
            Isbn = int(Isbn)+100
            f.write(str(Isbn))
            f.write('\n')
        with open(os.path.join("BD","Banco.txt"), "a+") as af:
            #with open("Banco.txt", "a") as af:
            af.write(obraNova.titulo)
            af.write('\n')
            af.write(obraNova.editora)
            af.write('\n')
            af.write(str(Isbn))
            af.write('\n')
            af.write(obraNova.autor)
            af.write('\n')
            for palavra in obraNova.palavras_chave:
                PlC = PlC + palavra + ","
            af.write(PlC)
            af.write('\n')
            af.write(str(obraNova.data_publi))
            af.write('\n')
            af.write(str(obraNova.nro_paginas))
            af.write('\n')
            af.write(str(obraNova.categoria_obra))
            af.write('\n')
            #for indice in obraNova.copias_obra: PARTE DE CADASTRO DE COPIA OBRA
                #af.write(Id+1)
                #af.write(',')
                #af.write(obraNova.copias_obra[indice].tipo_situacao)
                #af.write('\n')
            #af.write('-1\n')
            
            #rf.seek(len(proxId)+1)
            #with open("Banco2.txt", "w") as wf: TESTE DE COMO TRATAR O ARQUIVO
                #obraNova.
                #for line in rf:
                    #while(int(line) != -1):    
                    #wf.write(line)
                #print(line, end='')
                #listaObras = fobj.read()
        #futuraListaDeObras = [] #lembrar de tirar - mexer com bd
        #if (obraNova not in futuraListaDeObras):    
            #futuraListaDeObras.append(obraNova)
            #return True
        #return False

class CadastrarCopiaObraUseCase(ICadastrarCopiaObraUseCase):
    def cadastrarCopiaObra(obra,novaCopia) -> int:
        contaLinhas = 0
        Id = 0 
        with open(os.path.join("BD","id.txt"), "r+") as rf:
            Id = int(rf.readline())+1
            Isbn = rf.readline()
            rf.seek(0)
            rf.truncate(0)
            rf.write(str(Id))
            rf.write('\n')
            rf.write(str(Isbn))
        
        f = open(os.path.join("BD","Banco.txt"),"r")
        conteudo = f.readlines()
        f.close()
        with open(os.path.join("BD","Banco.txt"), "r+") as rf:
            comparacao = str(rf.readline())
            contaLinhas = contaLinhas + 1
            while(str(comparacao) != (str(obra.isbn)+"\n") and len(comparacao) != 0):
                comparacao = str(rf.readline())
                contaLinhas = contaLinhas + 1
                if comparacao.isdigit():
                    comparacao = int(comparacao)
        conteudo.insert(contaLinhas+5, str(Id)+",1"+'\n')
        f = open(os.path.join("BD","Banco.txt"), "w")
        conteudo = "".join(conteudo)
        f.write(conteudo)
        f.close()        

        
        #if (id not in copias_obra._id):#checar se essa comparação funciona 
            #copias_obra.append(novaCopia)
            #return novaCopia.id
        #return -1


class ListarSituacaoCopiaObraUseCase(IListarSituacaoCopiaObraUseCase):
    def listarCopiaObraSituacao(self,obra) -> None:
        situacao = consultarCopiaObraSituacao(IConsultarCopiaObraSituacaoUseCase)#não tenho certeza se o parametro está certo
        for indice,estado in enumerate(situacao):
            if(estado == 1):
                    print("Copia " + obra.copias_obra[indice]._id + "está disponivel") 
            elif(estado == 2):
                    print("Copia " + obra.copias_obra[indice]._id + "está emprestada") 
            elif(estado == 3):
                    print("Copia " + obra.copias_obra[indice]._id + "está atrasada") 
            elif(estado == 4):
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
