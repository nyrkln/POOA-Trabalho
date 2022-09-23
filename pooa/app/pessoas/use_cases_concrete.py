import os
from pooa.app.pessoas.use_cases_interfaces import (
    IAdicionarUsuarioUseCase,
    IAlterarDadosUsuarioUseCase,
    IConsultarDisciplinasUseCase,
    IConsultarGruposAcademicosUseCase,
    IConsultarPendenciasUseCase,
    IRemoverUsuarioUseCase,
    IConsultarLeitoresComPendenciasUseCase,
)
class AdicionarUsuarioUseCase(IAdicionarUsuarioUseCase):
    def adicionarUsuario(ListaDePessoas,pessoa,id):
        pessoa.identificador = id
        for pessoas in ListaDePessoas[0]:
            if (int(pessoas.cpf) == int(pessoa.cpf)):
                print("Usuario já cadastrado")
                return ListaDePessoas
        for pessoas in ListaDePessoas[1]:
            if (int(pessoas.cpf) == int(pessoa.cpf)):
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
        print("o usuario "+str(usuario.identificador)+" está inscrito em "+str(usuario.materias)+" materias")

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


class ConsultarGruposAcademicosUseCase(IConsultarGruposAcademicosUseCase):
    def consultarGruposAcademicos(usuario):
        if(usuario.grupoAcademico == True):
            print("o usuario "+str(usuario.identificador)+" está inscrito no grupo academico "+str(usuario.idGrupoAcademico)+" materias")
        else:
            print("o usuario não está inscrito em um grupo academico")

class ConsultarPendenciasUseCase(IConsultarPendenciasUseCase):
    def consultarPendencias(usuario,listadeobras):
        for obras in listadeobras:
            for copias in obras.copias_obra:
                if (str(copias.locatario).strip() == str(usuario.identificador).strip()) and (copias.get_state() == 'Atrasado'):
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
