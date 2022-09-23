from ast import List
import datetime
import os
from pooa.domain.pessoas import TipoUsuario, UsuarioFactory, TipoLeitor
from pooa.domain.obra import Obra, CopiaObra
from pooa.app.banco.use_cases_interfaces import(
    IReescreveBanco,ILeitorBanco,IRequisicaoId)

class ReescreveBancoPessoasUseCase(IReescreveBanco):
    def reescreveBanco(listaDeObjetos: List) -> None:
        with open(os.path.join("BD","BancoPessoa.txt"), "w") as af:
            pass
        with open(os.path.join("BD","BancoPessoa.txt"), "a+") as af:
            for pessoa in listaDeObjetos[0]:
                af.write(str(pessoa.identificador).strip())
                af.write('\n')
                af.write(pessoa.nome.strip())
                af.write('\n')
                af.write(str(pessoa.cpf).strip())
                af.write('\n')
                af.write(str(pessoa.cep).strip())
                af.write('\n')
                af.write(str(pessoa.data_nasc.strftime('%Y-%d-%m')).strip())
                af.write('\n')
                af.write(str(pessoa.telefone).strip())
                af.write('\n')
                af.write(str(pessoa.email).strip())
                af.write('\n')
                af.write(str(pessoa.usuario.value).strip())
                af.write('\n')
                af.write(str(pessoa.senha).strip())
                af.write('\n')
                if pessoa.usuario.value == 2:
                    af.write(str(pessoa.identificacao).strip())
                    af.write('\n')
                elif pessoa.usuario.value == 3:
                    af.write(str(pessoa.grupoAcademico).strip())
                    af.write('\n')
                    af.write(str(pessoa.idGrupoAcademico).strip())
                    af.write('\n')
                    af.write(str(pessoa.tipoLeitor.value))
                    af.write('\n')
                af.write('-1')
                af.write('\n')
            for pessoa in listaDeObjetos[1]:
                af.write(str(pessoa.identificador).strip())
                af.write('\n')
                af.write(pessoa.nome.strip())
                af.write('\n')
                af.write(str(pessoa.cpf).strip())
                af.write('\n')
                af.write(str(pessoa.cep).strip())
                af.write('\n')
                af.write(str(pessoa.data_nasc.strftime('%Y-%d-%m')).strip())
                af.write('\n')
                af.write(str(pessoa.telefone).strip())
                af.write('\n')
                af.write(str(pessoa.email).strip())
                af.write('\n')
                af.write(str(pessoa.usuario.value).strip())
                af.write('\n')
                af.write(str(pessoa.senha).strip())
                af.write('\n')
                if pessoa.usuario.value == 2:
                    af.write(str(pessoa.identificacao).strip())
                    af.write('\n')
                elif pessoa.usuario.value == 3:
                    af.write(str(pessoa.grupoAcademico).strip())
                    af.write('\n')
                    af.write(str(pessoa.idGrupoAcademico).strip())
                    af.write('\n')
                    af.write(str(pessoa.tipoLeitor.value))
                    af.write('\n')
                af.write('-1')
                af.write('\n')
            af.write('-5')
        
class ReescreveBancoObrassUseCase(IReescreveBanco):
    def reescreveBanco(listaDeObjetos: List) -> None:
        PlC = ""
        with open(os.path.join("BD","Banco.txt"), "w") as af:
            pass
        for obraNova in listaDeObjetos: 
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
                        af.write(str(copia.id)+','+str(situacao).strip()+','+'-1,-1,'+str(datetime.datetime.now().strftime('%Y-%d-%m'))+','+str(datetime.datetime.now().strftime('%Y-%d-%m'))+'\n')
                    elif (copia.get_state() == 'Emprestado'):
                        situacao = 2
                        af.write(str(copia.id)+','+str(situacao).strip()+','+str(copia.locatario).strip()+','+str(copia.funcionario)+','+str(copia.data_locacao.strftime('%Y-%d-%m')).strip()+','+str(copia.data_devolucao.strftime('%Y-%d-%m')).strip()+'\n')
                    elif (copia.get_state() == 'Atrasado'):
                        situacao = 3
                        af.write(str(copia.id)+','+str(situacao).strip()+','+str(copia.locatario).strip()+','+str(copia.funcionario)+','+str(copia.data_locacao.strftime('%Y-%d-%m')).strip()+','+str(copia.data_devolucao.strftime('%Y-%d-%m')).strip()+'\n')
                    elif (copia.get_state() == 'Reservado'):
                        situacao = 4 
                        af.write(str(copia.id)+','+str(situacao).strip()+','+str(copia.locatario).strip()+','+str(copia.funcionario)+','+str(copia.data_locacao.strftime('%Y-%d-%m')).strip()+','+str(copia.data_devolucao.strftime('%Y-%d-%m')).strip()+'\n') 
                af.write('-1')
                af.write('\n')
            PlC = ""    
        with open(os.path.join("BD","Banco.txt"), "a+") as af:
            af.write('-5')

class LeitorBancoPessoaUseCase(ILeitorBanco):
    def leitorBanco(listaDeObjetos: List):
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
                listaDeObjetos[0].append(cadastro)
            elif(usuario == 3):
                listaDeObjetos[1].append(cadastro)                
        rf.close()
        return listaDeObjetos

class LeitorBancoObraUseCase(ILeitorBanco):
    def leitorBanco(listaDeObjetos: List):
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
            listaDeObjetos.append(cadastro)
            proximo = rf.readline()
        rf.close()   
        return listaDeObjetos   

class RequisicaoIdPessoaUseCase(IRequisicaoId):
    def requisicaoId():
        with open(os.path.join("BD","idPessoa.txt"), "r+") as f:    
            Id = int(f.readline())
            f.seek(0)
            f.truncate(0)
            Id = int(Id)+100
            f.write(str(Id))
            f.write('\n')
        return Id    
 
class RequisicaoIdObraUseCase(IRequisicaoId):
    def requisicaoId():
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
        return Isbn 

class RequisicaoIdCopiaObraUseCase(IRequisicaoId):
    def requisicaoId():
        with open(os.path.join("BD","id.txt"), "r+") as rf:
            Id = int(rf.readline())+1
            Isbn = rf.readline()
            rf.seek(0)
            rf.truncate(0)
            rf.write(str(Id))
            rf.write('\n')
            rf.write(str(Isbn))
            rf.write('\n')
        return Id