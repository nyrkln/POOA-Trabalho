from pickle import APPEND
from pooa.app.obra.use_cases_concrete import AlterarDadosObraUseCase, CadastrarCopiaObraUseCase, CadastrarObraUseCase, DevolverObraUseCase, EmprestarObraUseCase, ListarSituacaoCopiaObraUseCase, ReservarObraUseCase
from pooa.app.obra.use_cases_interfaces import ICopiaObra
from pooa.app.pessoas.use_cases_concrete import AdicionarUsuarioUseCase, ConsultarPendenciasUseCase
from pooa.domain.obra import CopiaObra, Obra
from pooa.domain.pessoas import Usuario,UsuarioFactory,Funcionario,Administrador,Leitor,TipoUsuario
import datetime
import os
from pooa.domain.pessoas import TipoUsuario, UsuarioFactory
ListaDeObras = [] 
ListaDePessoas = [[],[]]


def leitorDeBancoPessoas(Lista):
    rf = open(os.path.join("BD","BancoPessoa.txt"),"r")
    proximo = str(rf.readline())
    while(proximo != '-5'):
        identificador = proximo
        nome = str(rf.readline())
        cpf = str(rf.readline())
        cep = str(rf.readline())
        data_nasc = datetime.datetime.strptime(str(rf.readline()),"%Y-%d-%m\n")
        telefone = str(rf.readline())
        email = str(rf.readline())
        usuario = int(rf.readline())
        senha = str(rf.readline())
        if(usuario == 2):
            parametro_dif = str(rf.readline())
        elif(usuario == 3):
            parametro_dif_bool = bool(str(rf.readline()))    
            parametro_dif = str(rf.readline())
        proximo = str(rf.readline())
        proximo = str(rf.readline())    
        cadastro = UsuarioFactory.build_usuario(TipoUsuario(usuario),identificador,nome,cpf,cep,data_nasc,telefone,email,senha,parametro_dif)    
        if(usuario == 2):    
            ListaDePessoas[0].append(cadastro)
        elif(usuario == 3):
            ListaDePessoas[1].append(cadastro)                
    rf.close()



def leitorDeBancoObras(Lista):
    rf = open(os.path.join("BD","Banco.txt"),"r")
    proximo = str(rf.readline())
    while(proximo != '-5'):
        nome = proximo
        editora = str(rf.readline())
        isbn = int(rf.readline())
        autor = str(rf.readline())
        palavras_chave = str(rf.readline()).split(",")
        data_publi = datetime.datetime.strptime(str(rf.readline()),"%Y-%d-%m\n")
        nro_paginas = int(rf.readline())
        categoria_obra = int(rf.readline())
        copias = []
        proximo = rf.readline()
        sinal = True
        while(sinal and str(proximo) != '-1\n'):
            base = str(proximo).split(",")
            copiaBase = CopiaObra(int(base[0]),int(base[1]),str(base[2].strip('\n')))
            copias.append(copiaBase)
            proximo = rf.readline()
            if (str(proximo) == '-1\n'):
                sinal = False
        cadastro = Obra(nome,editora,isbn,autor,palavras_chave,data_publi,nro_paginas,categoria_obra,copias)    
        Lista.append(cadastro)
        proximo = rf.readline()
    rf.close()





leitorDeBancoObras(ListaDeObras)
leitorDeBancoPessoas(ListaDePessoas)
leitor1 = UsuarioFactory.build_usuario(TipoUsuario.LEITOR,12,'matheus',41905743840,15061730,datetime.date(2000, 9, 4),17991353055,'othepaladini@gmail.com','teste',769111)
#for obras in ListaDeObras:
copia1trabalho = CopiaObra(1,1,-1)
copia2trabalho = CopiaObra(1,2,ListaDePessoas[0][0])
copia3trabalho = CopiaObra(1,3,leitor1)
copia4trabalho = CopiaObra(1,4,leitor1)
copiasTrabalho = [copia1trabalho,copia2trabalho,copia3trabalho,copia4trabalho]
livro = Obra('senhor dos aneis', 'abril',"1400" , 'J.R.R Tolkien', ['ficção', 'aventura'], datetime.date(2013, 1, 1), 1200, 5, copiasTrabalho)
#trabalho_alterado = Obra('TrabalhoAcademicoPOO', 'Ufscar', 600, 'Alunos', ['computação', 'inovação'], datetime.date(2013, 1, 1), 23, 4, copiasTrabalho)
#CadastrarObraUseCase.cadastrarObra(livro,ListaDeObras)
CadastrarCopiaObraUseCase.cadastrarCopiaObra(livro,copia2trabalho)
#ListarSituacaoCopiaObraUseCase.listarCopiaObraSituacao(testeState,ListaDeObras)
#print(ListaDeObras[5].titulo)
#AlterarDadosObraUseCase.alterarDadosObra(trabalho_alterado,ListaDeObras)
#print(ListaDeObras[5].titulo)
#ListarSituacaoCopiaObraUseCase.listarCopiaObraSituacao(testeState,ListaDeObras)
#ReservarObraUseCase.reservarObra(testeState,ListaDeObras)
#ListarSituacaoCopiaObraUseCase.listarCopiaObraSituacao(testeState,ListaDeObras)
#DevolverObraUseCase.devolverObra(livro,ListaDeObras,103)
#ListarSituacaoCopiaObraUseCase.listarCopiaObraSituacao(testeState,ListaDeObras)
#EmprestarObraUseCase.emprestarObra(testeState,ListaDeObras)
#ListarSituacaoCopiaObraUseCase.listarCopiaObraSituacao(testeState,ListaDeObras)
#leitor1 = UsuarioFactory.build_usuario(TipoUsuario.LEITOR,11950,'pedro',41905743842,15061730,datetime.date(2000, 9, 4),17991353055,'othepaladini@gmail.com','teste',769111)
#copia5trabalho = CopiaObra(1,2,ListaDePessoas[1][5])
#CadastrarCopiaObraUseCase.cadastrarCopiaObra(livro,copia5trabalho)
#print(ListaDePessoas[1][5])
#print(ListaDeObras[7].copias_obra[0].state)
#print(ConsultarPendenciasUseCase.consultarPendencias(ListaDePessoas[1][5],ListaDeObras))
#print(leitor1.idGrupoAcademico)
#AdicionarUsuarioUseCase.adicionarUsuario(ListaDePessoas,leitor1)
#print(ListaDePessoas)