from pickle import APPEND
from pooa.app.obra.use_cases_concrect import CadastrarCopiaObraUseCase, CadastrarObraUseCase
from pooa.app.obra.use_cases_interfaces import ICopiaObra
from pooa.domain.obra import Autor, Disponivel, Obra, CopiaObra
import datetime
import os
ListaDeObras = [] 
def leitorDeBanco(Lista):
    rf = open(os.path.join("BD","Banco.txt"),"r")
    proximo = str(rf.readline())
    while(proximo != '-5\n'):
        nome = proximo
        editora = str(rf.readline())
        isbn = int(rf.readline())
        autor = str(rf.readline())
        palavras_chave = str(rf.readline()).split(",")
        data_publi = datetime.datetime.strptime(str(rf.readline()),'%Y-%d-%m\n')
        nro_paginas = int(rf.readline())
        categoria_obra = int(rf.readline())
        copias = []
        proximo = rf.readline()
        sinal = True
        while(sinal and str(proximo) != '-1\n'):
            base = str(proximo).split(",")
            copiaBase = CopiaObra(int(base[0]))
            copias.append(copiaBase)
            proximo = rf.readline()
            if (str(proximo) == '-1\n'):
                sinal = False
        cadastro = Obra(nome,editora,isbn,autor,palavras_chave,data_publi,nro_paginas,categoria_obra,copias)    
        Lista.append(cadastro)
        proximo = rf.readline()

leitorDeBanco(ListaDeObras)

#print(ListaDeObras[0])

#date = datetime.date(2013, 1, 1)
copia1Lobo = CopiaObra(1)
copiasLoboDeWallStreet = [copia1Lobo]
LoboDeWallStreet = Obra('O Lobo de Wall Street', 'Planeta', 500, 'Jordan Belfort', ['biografia', 'suspense', 'anos 80'], datetime.date(2013, 1, 1), 501, 5, copiasLoboDeWallStreet)
#CadastrarObraUseCase.cadastrarObra(LoboDeWallStreet,ListaDeObras)
CadastrarCopiaObraUseCase.cadastrarCopiaObra(LoboDeWallStreet,copia1Lobo)