
from typing import List
from pooa.app.obra.use_cases_concrect import CopiaObra
from pooa.app.obra.use_cases_interfaces import (
    IAlterarDadosObraUseCase,
    ICadastrarCopiaObraUseCase,
    ICadastrarObraUseCase,
    IConsultarCopiaObraSituacaoUseCase,
    IConsultarCopiaObraUseCase,
    IDevolverObraUseCase,
    IEmprestarObraUseCase,
    IListarSituacaoCopiaObraUseCase,
    IReservarObraUseCase
)
from pooa.app.pessoas.use_cases_interfaces import IAlterarDadosUsuarioUseCase, IConsultarDisciplinasUseCase, IConsultarGruposAcademicosUseCase
from pooa.domain.obra import Obra


class ControllerObra:
    def __init__(
        self,
        consultar_copia_obra_use_case: IConsultarCopiaObraUseCase,
        consultar_copia_obra_situacao: IConsultarCopiaObraSituacaoUseCase,
        cadastrar_obra_use_case: ICadastrarObraUseCase,
        cadastrar_copia_obra_use_case: ICadastrarCopiaObraUseCase,
        alterar_dados_obra_use_case: IAlterarDadosObraUseCase,
        listar_situacao_copia_obra_use_case: IListarSituacaoCopiaObraUseCase
    ):
        self._consultar_copia_obra_use_case = consultar_copia_obra_use_case
        self._consultar_copia_obra_situacao = consultar_copia_obra_situacao
        self._cadastrar_obra_use_case = cadastrar_obra_use_case
        self._cadastrar_copia_obra_use_case = cadastrar_copia_obra_use_case
        self._alterar_dados_obra_use_case = alterar_dados_obra_use_case
        self._listar_situacao_copia_obra_use_case = listar_situacao_copia_obra_use_case

    def consultar_copia_obra(self) -> CopiaObra:
        return self._consultar_copia_obra_use_case.execute()

    def consultar_copia_obra_situacao(self) -> List[CopiaObra]:
        return self._consultar_copia_obra_situacao.execute()

    def cadastrar_obra(self) -> Obra:
        return self._cadastrar_obra_use_case.execute()

    def cadastrar_copia_obra(self) -> CopiaObra:
        return self._cadastrar_copia_obra_use_case.execute()

    def alterar_dados_obra(self) -> CopiaObra:
        return self._alterar_dados_obra_use_case.execute()

    def listar_situacao_copia_obra(self) -> None:
        return self._listar_situacao_copia_obra_use_case.execute()


class ControllerMovimentacao:
    def __init__(
        self,
        reservar_obra_use_case: IReservarObraUseCase,
        emprestar_obra_use_case: IEmprestarObraUseCase,
        devolver_obra_use_case: IDevolverObraUseCase
    ):
        self._reservar_obra_use_case = reservar_obra_use_case
        self._emprestar_obra_use_case = emprestar_obra_use_case
        self._devolver_obra_use_case = devolver_obra_use_case

    def reservar_obra(self):
        self._reservar_obra_use_case.execute()

    def emprestar_obra(self):
        self._emprestar_obra_use_case.execute()

    def devolver_obra(self):
        self._devolver_obra_use_case.execute()


class ControllerUser:
    def __init__(
        self,
        consultar_disciplinas_use_case: IConsultarDisciplinasUseCase,
        consultar_grupos_academicos_use_case: IConsultarGruposAcademicosUseCase,
        alterar_dados_usuarios_use_case: IAlterarDadosUsuarioUseCase
    ):
        self._consultar_disciplinas_use_case = consultar_disciplinas_use_case
        self._consultar_grupos_academicos_use_case = consultar_grupos_academicos_use_case
        self._alterar_dados_usuarios_use_case = alterar_dados_usuarios_use_case

    def consultar_disciplinas(self):
        return self._consultar_disciplinas_use_case.execute()

    def consultar_grupos_academicos(self):
        return self._consultar_grupos_academicos_use_case.execute()

    def alterar_dados_usuarios(self):
        return self._alterar_dados_usuarios_use_case.execute()
