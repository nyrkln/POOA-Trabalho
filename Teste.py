from pickle import APPEND
from pooa.app.obra.use_cases_concrete import AlterarDadosObraUseCase, CadastrarCopiaObraUseCase, CadastrarObraUseCase, ListarSituacaoCopiaObraUseCase
from pooa.app.obra.use_cases_interfaces import ICopiaObra
from pooa.domain.obra import CopiaObra, Obra
import datetime
import os
ListaDeObras = [] 
def leitorDeBanco(Lista):
    rf = open(os.path.join("BD","Banco copy.txt"),"r")
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

copia1Lobo = CopiaObra(1,1)
copia2Lobo = CopiaObra(2,2)
copia3Lobo = CopiaObra(3,3)
copia4Lobo = CopiaObra(4,4)
copiasLoboDeWallStreet = [copia1Lobo,copia2Lobo,copia3Lobo,copia4Lobo]
LoboDeWallStreet = Obra('O Lobo de Wall chato', 'Planeta', 500, 'Jordan Belfort', ['biografia', 'suspense', 'anos 80'], datetime.date(2013, 1, 1), 501, 5, copiasLoboDeWallStreet)
CadastrarObraUseCase.cadastrarObra(LoboDeWallStreet,ListaDeObras)
#print(LoboDeWallStreet.titulo)
#CadastrarCopiaObraUseCase.cadastrarCopiaObra(LoboDeWallStreet,copia1Lobo)
#ListarSituacaoCopiaObraUseCase.listarCopiaObraSituacao(LoboDeWallStreet)
AlterarDadosObraUseCase.alterarDadosObra(LoboDeWallStreet,ListaDeObras)