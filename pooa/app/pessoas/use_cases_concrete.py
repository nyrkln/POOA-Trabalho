import os
from pooa.app.pessoas.use_cases_interfaces import (
    IAdicionarUsuarioUseCase,
    IAlterarDadosUsuarioUseCase,
    IConsultarDisciplinasUseCase,
    IConsultarGruposAcademicosUseCase
)

def reescreve_bd(ListaDePessoas):
    with open(os.path.join("BD","BancoPessoa.txt"), "w") as af:
        pass
    with open(os.path.join("BD","BancoPessoa.txt"), "a+") as af:
        for pessoa in ListaDePessoas[0]:
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
            elif pessoa.usuario.value == 3:
                af.write(str(pessoa.grupoAcademico))
                af.write('\n')
                af.write(str(pessoa.idGrupoAcademico))
                af.write('\n')
            af.write('-1')
            af.write('\n')
        for pessoa in ListaDePessoas[1]:
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
            elif pessoa.usuario.value == 3:
                af.write(str(pessoa.grupoAcademico))
                af.write('\n')
                af.write(str(pessoa.idGrupoAcademico))
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
                futuraListaDePessoas[1].append(pessoa)
            af.write('-1')
            af.write('\n')
            af.write('-5')   


class ConsultarDisciplinasUseCase(IConsultarDisciplinasUseCase):
    def consultarDisciplina(self,usuario):
        ...


class ConsultarGruposAcademicosUseCase(IConsultarGruposAcademicosUseCase):
    def consultarGruposAcademicos(self,usuario):
        ...


class AlterarDadosUsuarioUseCase(IAlterarDadosUsuarioUseCase):
    def alterarDadosUsuario(self,usuario,futuraListaDeUsuarios):
        for indice,usuarios in enumerate(futuraListaDeUsuarios[0]):
            if usuario.cpf == usuarios.cpf:
                futuraListaDeUsuarios[0][indice] = usuario
                reescreve_bd(futuraListaDeUsuarios)
                return True
        for indice,usuarios in enumerate(futuraListaDeUsuarios[1]):
            if usuario.cpf == usuarios.cpf:
                futuraListaDeUsuarios[1][indice] = usuario
                reescreve_bd(futuraListaDeUsuarios)
                return True    
        return False
        ...
