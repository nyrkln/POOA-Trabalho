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

def reescreve_bd(ListaDePessoas):
    with open(os.path.join("BD","BancoPessoa.txt"), "w") as af:
        pass
    with open(os.path.join("BD","BancoPessoa.txt"), "a+") as af:
        for pessoa in ListaDePessoas[0]:
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
        for pessoa in ListaDePessoas[1]:
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

class AdicionarUsuarioUseCase(IAdicionarUsuarioUseCase):
    def adicionarUsuario(futuraListaDePessoas,pessoa):
        conteudo = []
        Id = 0
        for pessoas in futuraListaDePessoas[0]:
            if (int(pessoas.cpf) == int(pessoa.cpf)):
                print("Usuario já cadastrado")
                return -1
        for pessoas in futuraListaDePessoas[1]:
            if (int(pessoas.cpf) == int(pessoa.cpf)):
                print("Usuario já cadastrado")
                return -1        
        with open(os.path.join("BD","idPessoa.txt"), "r+") as f:
            Id = int(f.readline())
            f.seek(0)
            f.truncate(0)
            Id = int(Id)+100
            f.write(str(Id))
            f.write('\n')
        pessoa.identificação = str(Id)    
            
        with open(os.path.join("BD","BancoPessoa.txt"), "r+") as bdf:
            new_file_content = ""
            for line in bdf:
                stripped_line = line.strip()
                new_line = stripped_line.replace("-5", str(Id))
                new_file_content += new_line +"\n"
                f.close() 
        writing_file = open(os.path.join("BD","BancoPessoa.txt"), "w") 
        writing_file.write(new_file_content)
        writing_file.close()

        with open(os.path.join("BD","BancoPessoa.txt"), "a+") as af:
            af.write(pessoa.nome)
            af.write('\n')
            af.write(str(pessoa.cpf))
            af.write('\n')
            af.write(str(pessoa.cep))
            af.write('\n')
            af.write(str(pessoa.data_nasc))
            af.write('\n')
            af.write(str(pessoa.telefone))
            af.write('\n')
            af.write(str(pessoa.email))
            af.write('\n')
            af.write(str(pessoa.usuario.value))
            af.write('\n')
            af.write(str(pessoa.senha))
            af.write('\n')
            if pessoa.usuario.value == 2:
                af.write(str(pessoa.identificacao))
                af.write('\n')
                futuraListaDePessoas[0].append(pessoa)
            elif pessoa.usuario.value == 3:
                af.write(str(pessoa.grupoAcademico))
                af.write('\n')
                af.write(str(pessoa.idGrupoAcademico))
                af.write('\n')
                af.write(str(pessoa.tipoLeitor.value))
                af.write('\n')
                futuraListaDePessoas[1].append(pessoa)
            af.write('-1')
            af.write('\n')
            af.write('-5')   


class ConsultarDisciplinasUseCase(IConsultarDisciplinasUseCase):
    def consultarDisciplina(self,usuario):
        ... 
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
    def consultarGruposAcademicos(self,usuario):
        ...

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
                reescreve_bd(listaDeUsuarios)
                return True
        for indice,usuarios in enumerate(listaDeUsuarios[1]):
            if str(usuario.cpf).strip() == str(usuarios.cpf).strip():
                identificador = listaDeUsuarios[1][indice].identificador
                listaDeUsuarios[1][indice] = usuario
                listaDeUsuarios[1][indice].identificador = identificador
                reescreve_bd(listaDeUsuarios)
                return True    
        return False
        ...

class RemoverUsuarioUseCase(IRemoverUsuarioUseCase):
    def removerUsuario(usuario,ListaDeUsuarios):
        for indice,usuarios in enumerate(ListaDeUsuarios[0]):
            if str(usuario.cpf).strip() == str(usuarios.cpf).strip():
                ListaDeUsuarios[0].pop(indice)
                reescreve_bd(ListaDeUsuarios)
                return True
        for indice,usuarios in enumerate(ListaDeUsuarios[1]):
            if str(usuario.cpf).strip() == str(usuarios.cpf).strip():
                ListaDeUsuarios[1].pop(indice)
                reescreve_bd(ListaDeUsuarios)
                return True    
        return False        
