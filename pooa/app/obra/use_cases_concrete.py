from typing import List
import os

from pooa.app.obra.use_cases_interfaces import (
    IAlterarDadosCopiaObraUseCase,
    IAlterarDadosObraUseCase,
    ICadastrarCopiaObraUseCase,
    ICadastrarObraUseCase,
    IConsultarCopiaObraSituacaoUseCase,
    IConsultarCopiaObraUseCase,
    IDevolverObraUseCase,
    IEmprestarObraUseCase,
    IListarSituacaoCopiaObraUseCase,
    IReservarObraUseCase
)

def reescreve_bd(ListaDeObras):
     for obraNova in ListaDeObras: 
        with open(os.path.join("BD","Banco.txt"), "w") as af:
            #af.write('\n')
            af.write(obraNova.editora)
            af.write('\n')
            af.write(str(obraNova.isbn))
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
            af.write('-1')
            af.write('\n')
        af.write('-5\n')

def reescreve_bd2(CopiaObra):
    ...


class ConsultarCopiaObraUseCase(IConsultarCopiaObraUseCase):
    def consultarCopiaObra(self,obra,id):
        for copias in obra.copias_obra:
            if (copias.id == id):
                return copias
        return -1        # usar -1 como retorno?
        


class AlterarDadosObraUseCase(IAlterarDadosObraUseCase):
    def alterarDadosObra(obra,futuraListaDeObras) -> bool:
        for indice,obras in enumerate(futuraListaDeObras):
            if int(obras.isbn) == int(obra.isbn):
                futuraListaDeObras[indice] = obra 
                reescreve_bd(futuraListaDeObras)
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
    def cadastrarObra(obraNova,futuraListaDeObras) :
        #file = open("Banco.txt", "r+")
        #file.close
        #with open('Banco.txt','r') as rf:
        PlC = ""
        conteudo = []
        for obras in futuraListaDeObras:
            if (int(obraNova.isbn) == int(obras.isbn)):
                print("obra já cadastrada")
                return -1
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
            
        with open(os.path.join("BD","Banco.txt"), "r+") as bdf:
            new_file_content = ""
            for line in bdf:
                stripped_line = line.strip()
                new_line = stripped_line.replace("-5", str(obraNova.titulo))
                new_file_content += new_line +"\n"
                f.close() #NECESSARIO?
        writing_file = open(os.path.join("BD","Banco.txt"), "w")  #CODIGO EXEMPLO??
        writing_file.write(new_file_content)
        writing_file.close()

        with open(os.path.join("BD","Banco.txt"), "a+") as af:
            #af.write('\n')
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
            af.write('-1')
            af.write('\n')
            af.write('-5\n')
            futuraListaDeObras.append(obraNova)
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
                if(len(comparacao) == 0):
                    print("obra não encontrada")
                    return -1
            situacao = 0       
            if (novaCopia.get_state() == 'Disponivel'):
                    situacao = 1
            elif (novaCopia.get_state() == 'Emprestado'):
                    situacao = 2
            elif (novaCopia.get_state() == 'Atrasado'):
                    situacao = 3
            elif (novaCopia.get_state() == 'Reservado'):
                    situacao = 4       

        conteudo.insert(contaLinhas+5, str(Id)+","+str(situacao)+'\n')
        f = open(os.path.join("BD","Banco.txt"), "w")
        conteudo = "".join(conteudo)
        f.write(conteudo)
        f.close()
        obra.copias_obra.append(novaCopia)        

        
        #if (id not in copias_obra._id):#checar se essa comparação funciona 
            #copias_obra.append(novaCopia)
            #return novaCopia.id
        #return -1


class ListarSituacaoCopiaObraUseCase(IListarSituacaoCopiaObraUseCase):
    def listarCopiaObraSituacao(obra,listaDeObras):
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
        


class ReservarObraUseCase(IReservarObraUseCase):   
    def reservarObra(obra,listaDeObras) -> int:
        numeroObra = 0
        situacao = ConsultarCopiaObraSituacaoUseCase.consultarCopiaObraSituacao(obra,listaDeObras)
        for indice,estado in enumerate(situacao): 
            if(estado == 1):
                for indice2, conteudo in enumerate(listaDeObras):
                    if(conteudo.isbn == obra.isbn):
                        numeroObra = indice2
                listaDeObras[numeroObra].copias_obra[indice].state = 'Reservado'
                print("A copia de id: " + str(listaDeObras[numeroObra].copias_obra[indice].id) + " Agora está reservada")
                return obra.copias_obra[indice].id
                #falta gravar no banco, mas na execução atual já funciona
        return -1        
        ...

class EmprestarObraUseCase(IEmprestarObraUseCase):
    def emprestarObra(obra,listaDeObras) -> int:
        numeroObra = 0
        situacao = ConsultarCopiaObraSituacaoUseCase.consultarCopiaObraSituacao(obra,listaDeObras)
        for indice,estado in enumerate(situacao): 
            if(estado == 1):
                for indice2, conteudo in enumerate(listaDeObras):
                    if(conteudo.isbn == obra.isbn):
                        numeroObra = indice2
                listaDeObras[numeroObra].copias_obra[indice].state = 'Emprestado'
                print("A copia de id: " + str(listaDeObras[numeroObra].copias_obra[indice].id) + " Agora está emprestada")
                return obra.copias_obra[indice].id
                #falta gravar no banco, mas na execução atual já funciona
        return -1              
        ...


class DevolverObraUseCase(IDevolverObraUseCase):
    def devolverObra(obra,listaDeObras,idCopia) -> int:
            numeroObra = 0
            for indice2, conteudo in enumerate(listaDeObras):
                if(conteudo.isbn == obra.isbn):
                    numeroObra = indice2
            situacao = ConsultarCopiaObraSituacaoUseCase.consultarCopiaObraSituacao(obra,listaDeObras)
            for indice,estado in enumerate(situacao): 
                if((listaDeObras[indice2].copias_obra[indice].id == idCopia) and (estado == 2 or estado == 3 or estado == 4)):
                    listaDeObras[numeroObra].copias_obra[indice].state = 'Disponivel'
                    print("A copia de id: " + str(listaDeObras[numeroObra].copias_obra[indice].id) + " Agora está Disponivel")
                    return obra.copias_obra[indice].id
                    #falta gravar no banco, mas na execução atual já funciona
            return -1    
    