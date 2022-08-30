from pickle import APPEND
from pooa.app.obra.use_cases_concrete import AlterarDadosObraUseCase, CadastrarCopiaObraUseCase, CadastrarObraUseCase, DevolverObraUseCase, EmprestarObraUseCase, ListarSituacaoCopiaObraUseCase, ReservarObraUseCase
from pooa.app.obra.use_cases_interfaces import ICopiaObra
from pooa.domain.obra import CopiaObra, Obra
import datetime
import os
ListaDeObras = [] 
def leitorDeBanco(Lista):
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
            copiaBase = CopiaObra(int(base[0]),int(base[1]))
            copias.append(copiaBase)
            proximo = rf.readline()
            if (str(proximo) == '-1\n'):
                sinal = False
        cadastro = Obra(nome,editora,isbn,autor,palavras_chave,data_publi,nro_paginas,categoria_obra,copias)    
        Lista.append(cadastro)
        proximo = rf.readline()
    rf.close()

leitorDeBanco(ListaDeObras)
#for obras in ListaDeObras:
copia1trabalho = CopiaObra(1,1)
copia2trabalho = CopiaObra(1,2)
copia3trabalho = CopiaObra(1,3)
copia4trabalho = CopiaObra(1,4)
copiasTrabalho = [copia1trabalho,copia2trabalho,copia3trabalho,copia4trabalho]
testeState = Obra('teste do state', 'Ufscar', 400, 'Alunos', ['computação', 'inovação'], datetime.date(2013, 1, 1), 23, 4, copiasTrabalho)
#trabalho_alterado = Obra('TrabalhoAcademicoPOO', 'Ufscar', 600, 'Alunos', ['computação', 'inovação'], datetime.date(2013, 1, 1), 23, 4, copiasTrabalho)
#CadastrarObraUseCase.cadastrarObra(testeState,ListaDeObras)
#CadastrarCopiaObraUseCase.cadastrarCopiaObra(testeState,copia1trabalho)
#ListarSituacaoCopiaObraUseCase.listarCopiaObraSituacao(testeState,ListaDeObras)
#print(ListaDeObras[5].titulo)
#AlterarDadosObraUseCase.alterarDadosObra(trabalho_alterado,ListaDeObras)
#print(ListaDeObras[5].titulo)
ListarSituacaoCopiaObraUseCase.listarCopiaObraSituacao(testeState,ListaDeObras)
ReservarObraUseCase.reservarObra(testeState,ListaDeObras)
ListarSituacaoCopiaObraUseCase.listarCopiaObraSituacao(testeState,ListaDeObras)
DevolverObraUseCase.devolverObra(testeState,ListaDeObras,81)
ListarSituacaoCopiaObraUseCase.listarCopiaObraSituacao(testeState,ListaDeObras)
EmprestarObraUseCase.emprestarObra(testeState,ListaDeObras)
ListarSituacaoCopiaObraUseCase.listarCopiaObraSituacao(testeState,ListaDeObras)