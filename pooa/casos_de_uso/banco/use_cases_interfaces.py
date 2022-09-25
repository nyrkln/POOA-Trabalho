from abc import ABC, abstractmethod
from typing import List

class IReescreveBanco(ABC):
    @abstractmethod
    def reescreveBanco(listaDeObjetos: List):
        pass

class ILeitorBanco(ABC):
    @abstractmethod
    def leitorBanco(listaDeObjetos: List):
        pass  

class IRequisicaoId(ABC):
    @abstractmethod
    def requisicaoId():
        pass  