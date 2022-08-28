from pooa.app.obra.use_cases_concrect import CadastrarObraUseCase
from pooa.domain.obra import Obra
import datetime

#date = datetime.date(2013, 1, 1)
copiasLoboDeWallStreet = []
LoboDeWallStreet = Obra('O Lobo de Wall Street', 'Planeta', 1000, 'Jordan Belfort', ['biografia', 'suspense', 'anos 80'], datetime.date(2013, 1, 1), 501, 5, copiasLoboDeWallStreet)
CadastrarObraUseCase.cadastrarObra(LoboDeWallStreet)