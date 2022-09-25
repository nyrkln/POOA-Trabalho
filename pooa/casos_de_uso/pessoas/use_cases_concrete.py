from ast import Return
import os
from pickle import TRUE
from pooa.casos_de_uso.pessoas.use_cases_interfaces import (
    IAdicionarUsuarioUseCase,
    IAlterarDadosUsuarioUseCase,
    IConsultarDisciplinasUseCase,
    IConsultarGruposAcademicosUseCase,
    IConsultarPendenciasUseCase,
    IRemoverUsuarioUseCase,
    IConsultarLeitoresComPendenciasUseCase,
    IValidarUsuarioUseCase
)
class ValidarUsuarioUseCase(IValidarUsuarioUseCase):
    def validarUsuario(login,senha,listadepessoas):
        for pessoas in listadepessoas[0]:
            if(pessoas.email.strip() == str(login).strip()):
                if(pessoas.senha.strip() == str(senha).strip()):
                    return True
                return False    
        for pessoas in listadepessoas[1]:  
            if(pessoas.email.strip() == str(login).strip()):
                if(pessoas.senha.strip() == str(senha).strip()):
                    return True
                return False   
        return False         

class AdicionarUsuarioUseCase(IAdicionarUsuarioUseCase):
    def adicionarUsuario(ListaDePessoas,pessoa,id):
        pessoa.identificador = id
        for pessoas in ListaDePessoas[0]:
            if (int(pessoas.cpf) == int(pessoa.cpf) or str(pessoas.email).strip() == str(pessoa.email).strip()):
                print("Usuario já cadastrado")
                return ListaDePessoas
        for pessoas in ListaDePessoas[1]:
            if (int(pessoas.cpf) == int(pessoa.cpf) or str(pessoas.email).strip() == str(pessoa.email).strip()):
                print("Usuario já cadastrado")
                return ListaDePessoas       
        if pessoa.usuario.value == 2:
            ListaDePessoas[0].append(pessoa)
            print("Operação bem sucedida")
        elif pessoa.usuario.value == 3:
            ListaDePessoas[1].append(pessoa)
            print("Operação bem sucedida")
        return ListaDePessoas     

class ConsultarDisciplinasUseCase(IConsultarDisciplinasUseCase):
    def consultarDisciplina(usuario):
        if(int(usuario.materias)>0):
            print("o usuario "+str(usuario.identificador).strip()+" está inscrito em "+str(usuario.materias)+" materias")
            return True
        else:
            return False

class ConsultarLeitoresComPendenciasUseCase(IConsultarLeitoresComPendenciasUseCase):    
    def consultarLeitoresComPendencias(listadeobras,listadepessoas):
        listadedevedores = []
        for obras in listadeobras:
            for copias in obras.copias_obra:
                if copias.get_state() == 'Atrasado':
                    listadedevedores.append(copias.locatario)
        for devedores in listadedevedores:    
            for pessoas in listadepessoas[1]:
                if str(devedores).strip() == str(pessoas.identificador).strip():
                    print("o usuario "+pessoas.nome.strip()+" de cpf: " + str(pessoas.cpf).strip()+ " está em débito com a biblioteca")
        return listadedevedores            

class ConsultarGruposAcademicosUseCase(IConsultarGruposAcademicosUseCase):
    def consultarGruposAcademicos(usuario):
        if(usuario.grupoAcademico == True):
            print("o usuario "+str(usuario.identificador).strip()+" está inscrito no grupo academico "+str(usuario.idGrupoAcademico))
            return True
        else:
            print("o usuario não está inscrito em um grupo academico")
            return False

class ConsultarPendenciasUseCase(IConsultarPendenciasUseCase):
    def consultarPendencias(cpf,ListaDeObras,ListaDePessoas):
        identificador = '-1'
        for pessoas in ListaDePessoas[0]:
            if(str(cpf).strip() == str(pessoas.cpf).strip()):
                identificador = str(pessoas.identificador).strip()
        for pessoas in ListaDePessoas[1]:
            if(str(cpf).strip() == str(pessoas.cpf).strip()):
                identificador = str(pessoas.identificador).strip()
        if(identificador == '-1'):
            return False
        for obras in ListaDeObras:
            for copias in obras.copias_obra:
                if (str(copias.locatario).strip() == str(identificador).strip()) and (copias.get_state() == 'Atrasado'):
                    return True
        return False
        
class AlterarDadosUsuarioUseCase(IAlterarDadosUsuarioUseCase):
    def alterarDadosUsuario(usuario,listaDeUsuarios):
        for indice,usuarios in enumerate(listaDeUsuarios[0]):
            if str(usuario.cpf).strip() == str(usuarios.cpf).strip():
                identificador = listaDeUsuarios[0][indice].identificador
                listaDeUsuarios[0][indice] = usuario
                listaDeUsuarios[0][indice].identificador = identificador
                print("Operação bem sucedida")
                return listaDeUsuarios
        for indice,usuarios in enumerate(listaDeUsuarios[1]):
            if str(usuario.cpf).strip() == str(usuarios.cpf).strip():
                identificador = listaDeUsuarios[1][indice].identificador
                listaDeUsuarios[1][indice] = usuario
                listaDeUsuarios[1][indice].identificador = identificador
                print("Operação bem sucedida")
                return listaDeUsuarios    
        return listaDeUsuarios

class RemoverUsuarioUseCase(IRemoverUsuarioUseCase):
    def removerUsuario(usuario,ListaDeUsuarios):
        for indice,usuarios in enumerate(ListaDeUsuarios[0]):
            if str(usuario.cpf).strip() == str(usuarios.cpf).strip():
                ListaDeUsuarios[0].pop(indice)
                print("Operação bem sucedida")
                return ListaDeUsuarios
        for indice,usuarios in enumerate(ListaDeUsuarios[1]):
            if str(usuario.cpf).strip() == str(usuarios.cpf).strip():
                ListaDeUsuarios[1].pop(indice)
                print("Operação bem sucedida")
                return ListaDeUsuarios    
        return ListaDeUsuarios        
