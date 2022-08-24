from typing import List
from pooa.app.obra.use_cases_interfaces import (
    IAlterarDadosCopiaObraUseCase,
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
    def consultarCopiaObra(self) -> CopiaObra:
        ...


class AlterarDadosObraUseCase(IAlterarDadosObraUseCase):
    def alterarDadosObra(self) -> Obra:
        ...

class AlterarDadosCopiaObraUseCase(IAlterarDadosCopiaObraUseCase):
    def alterarDadosCopiaObra(self) -> CopiaObra:
        pass

class ConsultarCopiaObraSituacaoUseCase(IConsultarCopiaObraSituacaoUseCase):
    def consultarCopiaObraSituacao(self) -> List[CopiaObra]:
        ...


class CadastrarObraUseCase(ICadastrarObraUseCase):
    def cadastrarObra(self) -> Obra:
        ...


class CadastrarCopiaObraUseCase(ICadastrarCopiaObraUseCase):
    def cadastrarCopiaObra(self) -> CopiaObra:
        ...


class ListarSituacaoCopiaObraUseCase(IListarSituacaoCopiaObraUseCase):
    def listarCopiaObraSituacao(self) -> None:
        ...


class ReservarObraUseCase(IReservarObraUseCase):
    def reservarObra(self):
        ...


class EmprestarObraUseCase(IEmprestarObraUseCase):
    def emprestarObra(self):
        ...


class DevolverObraUseCase(IDevolverObraUseCase):
    def devolverObra(self):
        ...
