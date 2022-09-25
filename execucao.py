import datetime
from pickle import APPEND
import requests
from pooa.app.obra.use_cases_concrete import AlterarDadosObraUseCase, CadastrarCopiaObraUseCase, CadastrarObraUseCase, DevolverObraUseCase, EmprestarObraUseCase, ListarSituacaoCopiaObraUseCase, ReservarObraUseCase,RemoverObraUseCase,ConsultarObrasAtrasadasUseCase,ConsultarCopiaObraSituacaoUseCase
from pooa.app.obra.use_cases_interfaces import ICadastrarObraUseCase
from pooa.app.pessoas.use_cases_concrete import AdicionarUsuarioUseCase, ConsultarPendenciasUseCase,RemoverUsuarioUseCase,AlterarDadosUsuarioUseCase,ConsultarLeitoresComPendenciasUseCase,ConsultarDisciplinasUseCase,ConsultarGruposAcademicosUseCase, ValidarUsuarioUseCase
from pooa.domain.obra import CopiaObra, Obra
from pooa.domain.pessoas import Usuario,UsuarioFactory,Funcionario,Administrador,Leitor,TipoUsuario,TipoLeitor
from pooa.app.banco.use_cases_concrete import LeitorBancoObraUseCase,LeitorBancoPessoaUseCase,ReescreveBancoObrassUseCase,ReescreveBancoPessoasUseCase,RequisicaoIdCopiaObraUseCase,RequisicaoIdObraUseCase,RequisicaoIdPessoaUseCase
from pooa.adapters.controllers import ControllerBanco,ControllerObra,ControllerMovimentacao,ControllerUser

ListaDeObras = [] 
ListaDePessoas = [[],[]]

controllerBanco = ControllerBanco(ReescreveBancoPessoasUseCase,ReescreveBancoObrassUseCase,LeitorBancoPessoaUseCase,LeitorBancoObraUseCase,RequisicaoIdPessoaUseCase,RequisicaoIdObraUseCase,RequisicaoIdCopiaObraUseCase)
controllerPessoa = ControllerUser(ConsultarDisciplinasUseCase,ConsultarGruposAcademicosUseCase,AlterarDadosUsuarioUseCase,ConsultarPendenciasUseCase,ConsultarLeitoresComPendenciasUseCase,RemoverUsuarioUseCase,AdicionarUsuarioUseCase,ValidarUsuarioUseCase)


ListaDeObras =  controllerBanco.leitorBancoObras(ListaDeObras)
ListaDePessoas = controllerBanco.leitorBancoPessoas(ListaDePessoas)

#print(controllerPessoa.validarUsuario('othepaladini@gmail.com','teste',ListaDePessoas))

#controllerPessoa.consultarPendencias("4905743840",ListaDeObras,ListaDePessoas)

livro = Obra('Sapiens','abril',None, 'Yuval Harari', ['Historia', 'cientifico'], datetime.date(2011, 1, 1), 459, 5, None)
leitor1 = UsuarioFactory.build_usuario(TipoUsuario.LEITOR,11950,'joao',41905743896,15061730,datetime.date(2000, 9, 4),17991353055,'othepaladini@gmail.com','teste',[769111,TipoLeitor.ALUNO_GRADUACAO])
funcionario1 = UsuarioFactory.build_usuario(TipoUsuario.FUNCIONARIO,12450,'balconista',41905743877,15061730,datetime.date(2000, 9, 4),17991353055,'othepaladini@gmail.com','teste',12450)


copia1 = CopiaObra(1,1,-1,[1,datetime.date(2013, 1, 1),datetime.date(2013, 1, 1)])
copia2 = CopiaObra(1,2,ListaDePessoas[1][0].identificador,[funcionario1.identificador,datetime.date(2013, 1, 1),datetime.date(2013, 1, 1)])
copia3 = CopiaObra(1,3,leitor1.identificador,[funcionario1.identificador,datetime.date(2013, 1, 1),datetime.date(2013, 1, 1)])
copia4 = CopiaObra(1,4,leitor1.identificador,[funcionario1.identificador,datetime.date(2013, 1, 1),datetime.date(2013, 1, 1)])
copiasTrabalho = [copia1,copia2,copia3,copia4]



#CadastrarObraUseCase.cadastrarObra(livro,ListaDeObras)
#ICadastrarObraUseCase.cadastrarObra(livro,ListaDeObras)

livro = Obra('Sapiens','abril',"1800" , 'Yuval Harari', ['Historia', 'cientifico','intrigante'], datetime.date(2011, 1, 1), 459, 5, [])
#AlterarDadosObraUseCase.alterarDadosObra(livro,ListaDeObras)
#RemoverObraUseCase.removerObra(ListaDeObras[1],ListaDeObras)
#CadastrarCopiaObraUseCase.cadastrarCopiaObra(livro,copia1)
#ReservarObraUseCase.reservarObra(livro,ListaDeObras,leitor1,funcionario1)
#ListarSituacaoCopiaObraUseCase.listarCopiaObraSituacao(livro,ListaDeObras)
#EmprestarObraUseCase.emprestarObra(livro,ListaDeObras,leitor1,funcionario1)
#ListarSituacaoCopiaObraUseCase.listarCopiaObraSituacao(livro,ListaDeObras)
#DevolverObraUseCase.devolverObra(livro,ListaDeObras,139)
#DevolverObraUseCase.devolverObra(ListaDeObras[0],ListaDeObras,101)###obra com atraso
#print(ConsultarCopiaObraSituacaoUseCase.consultarCopiaObraSituacao(ListaDeObras[0],ListaDeObras)[2])
#ListarSituacaoCopiaObraUseCase.listarCopiaObraSituacao(livro,ListaDeObras)
#ConsultarObrasAtrasadasUseCase.consultarObrasAtrasadas(ListaDeObras,ListaDePessoas)

leitor2 = UsuarioFactory.build_usuario(TipoUsuario.LEITOR,None,'Valter',41905743950,15061730,datetime.date(2000, 9, 4),17991353055,'valter@ufscar.com','teste',[704030,TipoLeitor.PROFESSOR])
#funcionario2 = 
#ListaDePessoas = AdicionarUsuarioUseCase.adicionarUsuario(ListaDePessoas,leitor2,RequisicaoIdPessoaUseCase.requisicaoId())
#ListaDeObras = CadastrarObraUseCase.cadastrarObra(livro,ListaDeObras,RequisicaoIdObraUseCase.requisicaoId())
#ListaDeObras[2] = CadastrarCopiaObraUseCase.cadastrarCopiaObra(ListaDeObras[2],copia1,RequisicaoIdCopiaObraUseCase.requisicaoId())

#leitor2 = UsuarioFactory.build_usuario(TipoUsuario.LEITOR,None,'Valter',41905743950,15061745,datetime.date(2000, 9, 4),17991353055,'valter@ufscar.com','teste',[704030,TipoLeitor.PROFESSOR])
#AlterarDadosUsuarioUseCase.alterarDadosUsuario(leitor2,ListaDePessoas)
#ConsultarLeitoresComPendenciasUseCase.consultarLeitoresComPendencias(ListaDeObras,ListaDePessoas)
#RemoverUsuarioUseCase.removerUsuario(leitor2,ListaDePessoas)
#print(leitor1.idGrupoAcademico)
#ConsultarDisciplinasUseCase.consultarDisciplina(leitor1)#integraçao
#ConsultarGruposAcademicosUseCase.consultarGruposAcademicos(leitor1)
leitor3 = UsuarioFactory.build_usuario(TipoUsuario.LEITOR,11750,'jonas',41905743832,15061730,datetime.date(2000, 9, 4),17991353055,'othepaladini@gmail.com','teste',[-1,TipoLeitor.ALUNO_GRADUACAO])
#ConsultarGruposAcademicosUseCase.consultarGruposAcademicos(leitor3)
#print(ListaDePessoas)
controllerBanco.reescreveBancoPessoas(ListaDePessoas)
controllerBanco.reescreveBancoObras(ListaDeObras)

