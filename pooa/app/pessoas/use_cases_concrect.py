from pooa.app.pessoas.use_cases_interfaces import (
    IAlterarDadosUsuarioUseCase,
    IConsultarDisciplinasUseCase,
    IConsultarGruposAcademicosUseCase
)


class ConsultarDisciplinasUseCase(IConsultarDisciplinasUseCase):
    def consultarDisciplina(self,usuario):
        ...


class ConsultarGruposAcademicosUseCase(IConsultarGruposAcademicosUseCase):
    def consultarGruposAcademicos(self,usuario):
        ...


class AlterarDadosUsuarioUseCase(IAlterarDadosUsuarioUseCase):
    def alterarDadosUsuario(self,usuario,futuraListaDeUsuarios):
        for indice,usuarios in enumerate(futuraListaDeUsuarios):
            if usuario.cpf == usuarios.cpf:
                futuraListaDeUsuarios[indice] = usuario
                return True
        return False
        ...
