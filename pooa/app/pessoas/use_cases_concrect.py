from pooa.app.pessoas.use_cases_interfaces import (
    IAlterarDadosUsuarioUseCase,
    IConsultarDisciplinasUseCase,
    IConsultarGruposAcademicosUseCase
)


class ConsultarDisciplinasUseCase(IConsultarDisciplinasUseCase):
    def execute(self):
        ...


class ConsultarGruposAcademicosUseCase(IConsultarGruposAcademicosUseCase):
    def execute(self):
        ...


class AlterarDadosUsuarioUseCase(IAlterarDadosUsuarioUseCase):
    def execute(self):
        ...
