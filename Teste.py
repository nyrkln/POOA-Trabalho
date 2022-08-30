from pickle import APPEND
from pooa.app.obra.use_cases_concrete import AlterarDadosObraUseCase, CadastrarCopiaObraUseCase, CadastrarObraUseCase, ListarSituacaoCopiaObraUseCase
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
copia1biblia = CopiaObra(1,1)
copia2biblia = CopiaObra(2,1)
copia3biblia = CopiaObra(3,3)
copia4biblia = CopiaObra(4,4)
copiasBiblia = [copia1biblia,copia2biblia,copia3biblia,copia4biblia]
biblia = Obra('biblia', 'Planeta', 700, 'Jordan Belfort', ['biografia', 'suspense', 'anos 80'], datetime.date(2013, 1, 1), 501, 5, copiasBiblia)
#CadastrarObraUseCase.cadastrarObra(biblia,ListaDeObras)
#print(biblia.titulo)
#CadastrarCopiaObraUseCase.cadastrarCopiaObra(biblia,copia3biblia)
ListarSituacaoCopiaObraUseCase.listarCopiaObraSituacao(biblia,ListaDeObras)
#AlterarDadosObraUseCase.alterarDadosObra(biblia,ListaDeObras)