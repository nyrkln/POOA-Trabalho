from pooa.app.obra.use_cases_concrect import CadastrarCopiaObraUseCase, CadastrarObraUseCase
from pooa.app.obra.use_cases_interfaces import ICopiaObra
from pooa.domain.obra import Disponivel, Obra, CopiaObra
import datetime

#date = datetime.date(2013, 1, 1)
copiasLoboDeWallStreet = []
LoboDeWallStreet = Obra('O Lobo de Wall Street', 'Planeta', 500, 'Jordan Belfort', ['biografia', 'suspense', 'anos 80'], datetime.date(2013, 1, 1), 501, 5, copiasLoboDeWallStreet)
copia1Lobo = CopiaObra(1)

CadastrarCopiaObraUseCase.cadastrarCopiaObra(LoboDeWallStreet,copia1Lobo)