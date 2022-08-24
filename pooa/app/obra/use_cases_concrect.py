from typing import List
from pooa.app.obra.use_cases_interfaces import (
    IAlterarDadosObraUseCase,
    ICadastrarCopiaObraUseCase,
    ICadastrarObraUseCase,
    IConsultarCopiaObraSituacaoUseCase,
    IConsultarCopiaObraUseCase,
    ICopiaObra,
    IDevolverObraUseCase,
    IEmprestarObraUseCase,
    IListarSituacaoCopiaObraUseCase,
    IReservarObraUseCase
)
from pooa.domain.obra import Obra, TipoSituacao


class CopiaObra(ICopiaObra):
    def __init__(self):
        self._situacao: TipoSituacao = None
        self._id: int = 0

    def get_situacao(self):
        ...


class ConsultarCopiaObraUseCase(IConsultarCopiaObraUseCase):
    def execute(self) -> CopiaObra:
        ...


class AlterarDadosObraUseCase(IAlterarDadosObraUseCase):
    def execute(self) -> CopiaObra:
        ...


class ConsultarCopiaObraSituacaoUseCase(IConsultarCopiaObraSituacaoUseCase):
    def execute(self) -> List[CopiaObra]:
        ...


class CadastrarObraUseCase(ICadastrarObraUseCase):
    def execute(self) -> Obra:
        ...


class CadastrarCopiaObraUseCase(ICadastrarCopiaObraUseCase):
    def execute(self) -> CopiaObra:
        ...


class ListarSituacaoCopiaObraUseCase(IListarSituacaoCopiaObraUseCase):
    def execute(self) -> None:
        ...


class ReservarObraUseCase(IReservarObraUseCase):
    def execute(self):
        ...


class EmprestarObraUseCase(IEmprestarObraUseCase):
    def execute(self):
        ...


class DevolverObraUseCase(IDevolverObraUseCase):
    def execute(self):
        ...
