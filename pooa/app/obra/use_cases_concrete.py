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
    IReservarObraUseCase,
    IRemoverObraUseCase,
    IConsultarObrasAtrasadasUseCase
)

def reescreve_bd(ListaDeObras):
    PlC = ""
    with open(os.path.join("BD","Banco.txt"), "w") as af:
        pass
    for obraNova in ListaDeObras: 
        with open(os.path.join("BD","Banco.txt"), "a+") as af:
            #af.write('\n')
            af.write(obraNova.titulo.strip())
            af.write('\n')
            af.write(obraNova.editora.strip())
            af.write('\n')
            af.write(str(obraNova.isbn)+'\n')
            af.write(obraNova.autor.strip())
            af.write('\n')
            for indice,palavra in enumerate(obraNova.palavras_chave):
                if(len(obraNova.palavras_chave) != indice+1):    
                    PlC = PlC + palavra + ","
                else:
                    PlC = PlC + palavra    
            af.write(PlC.strip())
            af.write('\n')
            af.write(str(obraNova.data_publi.strftime('%Y-%d-%m')).strip())
            af.write('\n')
            af.write(str(obraNova.nro_paginas).strip())
            af.write('\n')
            af.write(str(obraNova.categoria_obra).strip())
            af.write('\n')
            for copia in obraNova.copias_obra:
                situacao = 0
                if (copia.get_state() == 'Disponivel'):
                    situacao = 1
                    af.write(str(copia.id)+','+str(situacao).strip()+','+'-1'+'\n')
                elif (copia.get_state() == 'Emprestado'):
                    situacao = 2
                    af.write(str(copia.id)+','+str(situacao).strip()+','+str(copia.locatario).strip()+'\n')
                elif (copia.get_state() == 'Atrasado'):
                    situacao = 3
                    af.write(str(copia.id)+','+str(situacao).strip()+','+str(copia.locatario).strip()+'\n')
                elif (copia.get_state() == 'Reservado'):
                    situacao = 4 
                    af.write(str(copia.id)+','+str(situacao).strip()+','+str(copia.locatario).strip()+'\n') 
            af.write('-1')
            af.write('\n')
        PlC = ""    
    with open(os.path.join("BD","Banco.txt"), "a+") as af:
        af.write('-5')

class ConsultarCopiaObraUseCase(IConsultarCopiaObraUseCase):
    def consultarCopiaObra(self,obra,id):
        for copias in obra.copias_obra:
            if (copias.id == id):
                return copias
        return -1 
class ConsultarObrasAtrasadasUseCase(IConsultarObrasAtrasadasUseCase): 
    def consultarObrasAtrasadas(listadeobras,listadepessoas):
        listadedevedores = []
        listadeobrasatrasadas = []
        listadeidentificadores = []
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

        

class AlterarDadosObraUseCase(IAlterarDadosObraUseCase):
    def alterarDadosObra(obra,ListaDeObras) -> bool:
        for indice,obras in enumerate(ListaDeObras):
            if int(obras.isbn) == int(obra.isbn):
                lista = ListaDeObras[indice].copias_obra
                ListaDeObras[indice] = obra
                ListaDeObras[indice].copias_obra = lista 
                reescreve_bd(ListaDeObras)
                return True
        return False
        ...

class RemoverObraUseCase(IRemoverObraUseCase):
    def removerObra(obra,ListaDeObras) -> bool:
        for indice,obras in enumerate(ListaDeObras):
            if int(obras.isbn) == int(obra.isbn):
                ListaDeObras.pop(indice)
                reescreve_bd(ListaDeObras)
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
    def cadastrarObra(obraNova,futuraListaDeObras):
        PlC = ""
        conteudo = []
        for obras in futuraListaDeObras:
            if ((str(obraNova.titulo).strip() == str(obras.titulo).strip()) and (str(obraNova.nro_paginas).strip() == str(obras.nro_paginas).strip()) ):
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
            obraNova.id = Id
            
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
            af.write('-5')
            futuraListaDeObras.append(obraNova)

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
                    conteudo.insert(contaLinhas+5, str(Id)+","+str(situacao)+',-1'+'\n')
            elif (novaCopia.get_state() == 'Emprestado'):
                    situacao = 2
                    conteudo.insert(contaLinhas+5, str(Id)+","+str(situacao)+','+str(novaCopia.get_locatario()).strip()+'\n')
            elif (novaCopia.get_state() == 'Atrasado'):
                    situacao = 3
                    conteudo.insert(contaLinhas+5, str(Id)+","+str(situacao)+','+str(novaCopia.get_locatario()).strip()+'\n')
            elif (novaCopia.get_state() == 'Reservado'):
                    situacao = 4
                    conteudo.insert(contaLinhas+5, str(Id)+","+str(situacao)+','+str(novaCopia.get_locatario()).strip()+'\n')
        f = open(os.path.join("BD","Banco.txt"), "w")
        conteudo = "".join(conteudo)
        f.write(conteudo)
        f.close()
        obra.copias_obra.append(novaCopia)        

        

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
    def reservarObra(obra,listaDeObras,locatario) -> int:
        numeroObra = 0
        situacao = ConsultarCopiaObraSituacaoUseCase.consultarCopiaObraSituacao(obra,listaDeObras)
        for indice,estado in enumerate(situacao): 
            if(estado == 1):
                for indice2, conteudo in enumerate(listaDeObras):
                    if(int(conteudo.isbn) == int(obra.isbn)):
                        numeroObra = indice2
                        listaDeObras[numeroObra].copias_obra[indice].state = 'Reservado'
                        listaDeObras[numeroObra].copias_obra[indice].locatario = str(locatario.identificador)
                        print("A copia de id: " + str(listaDeObras[numeroObra].copias_obra[indice].id) + " Agora está reservada")
                        reescreve_bd(listaDeObras)
                        return obra.copias_obra[indice].id    
        print("Não existem obras desse título disponíveis")
        return -1        
        ...

class EmprestarObraUseCase(IEmprestarObraUseCase):
    def emprestarObra(obra,listaDeObras,locatario) -> int:
        numeroObra = 0
        situacao = ConsultarCopiaObraSituacaoUseCase.consultarCopiaObraSituacao(obra,listaDeObras)
        for indice,estado in enumerate(situacao): 
            if(estado == 1):
                for indice2, conteudo in enumerate(listaDeObras):
                    if(int(conteudo.isbn) == int(obra.isbn)):
                        numeroObra = indice2
                        listaDeObras[numeroObra].copias_obra[indice].state = 'Emprestado'
                        listaDeObras[numeroObra].copias_obra[indice].locatario = str(locatario.identificador)
                        print("A copia de id: " + str(listaDeObras[numeroObra].copias_obra[indice].id) + " Agora está emprestada")
                        reescreve_bd(listaDeObras)
                        return obra.copias_obra[indice].id
                #falta gravar no banco, mas na execução atual já funciona
        print("Não existem obras desse título disponíveis")        
        return -1              
        ...


class DevolverObraUseCase(IDevolverObraUseCase):
    def devolverObra(obra,listaDeObras,idCopia) -> int:
            numeroObra = 0
            for indice2, conteudo in enumerate(listaDeObras):
                if(int(conteudo.isbn) == int(obra.isbn)):
                    numeroObra = indice2
            situacao = ConsultarCopiaObraSituacaoUseCase.consultarCopiaObraSituacao(obra,listaDeObras)
            for indice,estado in enumerate(situacao): 
                if((listaDeObras[indice2].copias_obra[indice].id == idCopia) and (estado == 2 or estado == 3 or estado == 4)):
                    listaDeObras[numeroObra].copias_obra[indice].state = 'Disponivel'
                    listaDeObras[numeroObra].copias_obra[indice].locatario = '-1'
                    print("A copia de id: " + str(listaDeObras[numeroObra].copias_obra[indice].id) + " Agora está Disponivel")
                    reescreve_bd(listaDeObras)
                    return obra.copias_obra[indice].id
            print("Cópia já estava disponível Disponivel")        
            return -1    
    