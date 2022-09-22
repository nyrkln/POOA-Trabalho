from pickle import APPEND
from pooa.app.obra.use_cases_concrete import AlterarDadosObraUseCase, CadastrarCopiaObraUseCase, CadastrarObraUseCase, DevolverObraUseCase, EmprestarObraUseCase, ListarSituacaoCopiaObraUseCase, ReservarObraUseCase,RemoverObraUseCase,ConsultarObrasAtrasadasUseCase
from pooa.app.obra.use_cases_interfaces import ICopiaObra
from pooa.app.pessoas.use_cases_concrete import AdicionarUsuarioUseCase, ConsultarPendenciasUseCase,RemoverUsuarioUseCase,AlterarDadosUsuarioUseCase,ConsultarLeitoresComPendenciasUseCase,ConsultarDisciplinasUseCase,ConsultarGruposAcademicosUseCase
from pooa.domain.obra import CopiaObra, Obra
from pooa.domain.pessoas import Usuario,UsuarioFactory,Funcionario,Administrador,Leitor,TipoUsuario,TipoLeitor
import datetime
import os
from pooa.domain.pessoas import TipoUsuario, UsuarioFactory
import requests
import json

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
            parametro_dif = []    
            parametro_dif.append(str(rf.readline()))
            parametro_dif.append(TipoLeitor(int(rf.readline())))
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
            data_emprestimo = datetime.datetime.strptime(base[4].strip('\n'),"%Y-%d-%m").date()
            data_devolucao = datetime.datetime.strptime(base[5].strip('\n'),"%Y-%d-%m").date()
            copiaBase = CopiaObra(int(base[0]),int(base[1]),str(base[2].strip('\n')),[str(base[3].strip('\n')),data_emprestimo,data_devolucao])
            copias.append(copiaBase)
            proximo = rf.readline()
            if (str(proximo) == '-1\n'):
                sinal = False
        cadastro = Obra(nome,editora,isbn,autor,palavras_chave,data_publi,nro_paginas,categoria_obra,copias)    
        Lista.append(cadastro)
        proximo = rf.readline()
    rf.close()


def consultarPendencias(usuario):
    identificador = '-1'
    for pessoas in ListaDePessoas[0]:
        if(str(usuario).strip() == str(pessoas.cpf).strip()):
            identificador = str(pessoas.identificador).strip()

    for pessoas in ListaDePessoas[1]:
        if(str(usuario).strip() == str(pessoas.cpf).strip()):
            identificador = str(pessoas.identificador).strip()
    if(identificador == '-1'):
        return False
    for obras in ListaDeObras:
        for copias in obras.copias_obra:
            if (str(copias.locatario).strip() == str(identificador).strip()) and (copias.get_state() == 'Atrasado'):
                return True
    return False            



leitorDeBancoObras(ListaDeObras)
leitorDeBancoPessoas(ListaDePessoas)

livro = Obra('Sapiens','abril',None, 'Yuval Harari', ['Historia', 'cientifico'], datetime.date(2011, 1, 1), 459, 5, None)
leitor1 = UsuarioFactory.build_usuario(TipoUsuario.LEITOR,11950,'joao',41905743896,15061730,datetime.date(2000, 9, 4),17991353055,'othepaladini@gmail.com','teste',[769111,TipoLeitor.ALUNO_GRADUACAO])
funcionario1 = UsuarioFactory.build_usuario(TipoUsuario.FUNCIONARIO,12450,'balconista',41905743877,15061730,datetime.date(2000, 9, 4),17991353055,'othepaladini@gmail.com','teste',12450)

copia1 = CopiaObra(1,1,-1,[1,datetime.date(2013, 1, 1),datetime.date(2013, 1, 1)])
copia2 = CopiaObra(1,2,ListaDePessoas[1][0].identificador,[funcionario1.identificador,datetime.date(2013, 1, 1),datetime.date(2013, 1, 1)])
copia3 = CopiaObra(1,3,leitor1.identificador,[funcionario1.identificador,datetime.date(2013, 1, 1),datetime.date(2013, 1, 1)])
copia4 = CopiaObra(1,4,leitor1.identificador,[funcionario1.identificador,datetime.date(2013, 1, 1),datetime.date(2013, 1, 1)])
copiasTrabalho = [copia1,copia2,copia3,copia4]


#CadastrarObraUseCase.cadastrarObra(livro,ListaDeObras)

livro = Obra('Sapiens','abril',"1700" , 'Yuval Harari', ['Historia', 'cientifico','intrigante'], datetime.date(2011, 1, 1), 459, 5, copiasTrabalho)
#AlterarDadosObraUseCase.alterarDadosObra(livro,ListaDeObras)
#RemoverObraUseCase.removerObra(ListaDeObras[1],ListaDeObras)
#CadastrarCopiaObraUseCase.cadastrarCopiaObra(livro,copia1)
#ReservarObraUseCase.reservarObra(livro,ListaDeObras,leitor1,funcionario1)
#ListarSituacaoCopiaObraUseCase.listarCopiaObraSituacao(livro,ListaDeObras)
#EmprestarObraUseCase.emprestarObra(livro,ListaDeObras,leitor1,funcionario1)
#ListarSituacaoCopiaObraUseCase.listarCopiaObraSituacao(livro,ListaDeObras)
#DevolverObraUseCase.devolverObra(livro,ListaDeObras,139)
#ListarSituacaoCopiaObraUseCase.listarCopiaObraSituacao(livro,ListaDeObras)
#ConsultarObrasAtrasadasUseCase.consultarObrasAtrasadas(ListaDeObras,ListaDePessoas)

leitor2 = UsuarioFactory.build_usuario(TipoUsuario.LEITOR,None,'Valter',41905743950,15061730,datetime.date(2000, 9, 4),17991353055,'valter@ufscar.com','teste',[704030,TipoLeitor.PROFESSOR])
#funcionario2 = 
#AdicionarUsuarioUseCase.adicionarUsuario(ListaDePessoas,leitor2)
#leitor2 = UsuarioFactory.build_usuario(TipoUsuario.LEITOR,None,'Valter',41905743950,15061745,datetime.date(2000, 9, 4),17991353055,'valter@ufscar.com','teste',[704030,TipoLeitor.PROFESSOR])
#AlterarDadosUsuarioUseCase.alterarDadosUsuario(leitor2,ListaDePessoas)
#ConsultarLeitoresComPendenciasUseCase.consultarLeitoresComPendencias(ListaDeObras,ListaDePessoas)
#RemoverUsuarioUseCase.removerUsuario(leitor2,ListaDePessoas)
#print(leitor1.idGrupoAcademico)
#ConsultarDisciplinasUseCase.consultarDisciplina(leitor1)#integraçao
#ConsultarGruposAcademicosUseCase.consultarGruposAcademicos(leitor1)
leitor3 = UsuarioFactory.build_usuario(TipoUsuario.LEITOR,11750,'jonas',41905743832,15061730,datetime.date(2000, 9, 4),17991353055,'othepaladini@gmail.com','teste',[-1,TipoLeitor.ALUNO_GRADUACAO])
#ConsultarGruposAcademicosUseCase.consultarGruposAcademicos(leitor3)






#print(ListaDePessoas)






