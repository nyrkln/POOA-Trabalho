from abc import ABC, abstractmethod

from pooa.domain.obra import TipoSituacao


class Observer(ABC):
    @abstractmethod
    def notificar_atraso(self):
        ...


class AtrasoObserver(Observer):
    def __init__(self):
        self._tipo_situacao = TipoSituacao

    def atualizar(self): ...
