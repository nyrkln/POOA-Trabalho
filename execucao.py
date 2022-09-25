#Arquivo de teste, simulando movimentações de uma biblioteca
#Devido as APIs, a execução está bem lenta, mas só aguardar, pois a execução ira seguir
#!
#!
#!
#!
#!
#!
#!
#!
#!
#!
#!
#!
#!
import datetime
from pickle import APPEND
import requests
from pooa.casos_de_uso.obra.use_cases_concrete import ConsultarCopiaObraUseCase, AlterarDadosObraUseCase, CadastrarCopiaObraUseCase, CadastrarObraUseCase, DevolverObraUseCase, EmprestarObraUseCase, ListarSituacaoCopiaObraUseCase, ReservarObraUseCase,RemoverObraUseCase,ConsultarObrasAtrasadasUseCase,ConsultarCopiaObraSituacaoUseCase
from pooa.casos_de_uso.obra.use_cases_interfaces import ICadastrarObraUseCase
from pooa.casos_de_uso.pessoas.use_cases_concrete import AdicionarUsuarioUseCase, ConsultarPendenciasUseCase,RemoverUsuarioUseCase,AlterarDadosUsuarioUseCase,ConsultarLeitoresComPendenciasUseCase,ConsultarDisciplinasUseCase,ConsultarGruposAcademicosUseCase, ValidarUsuarioUseCase
from pooa.entidades.obra import CopiaObra, Obra
from pooa.entidades.pessoas import Usuario,UsuarioFactory,Funcionario,Administrador,Leitor,TipoUsuario,TipoLeitor
from pooa.casos_de_uso.banco.use_cases_concrete import LeitorBancoObraUseCase,LeitorBancoPessoaUseCase,ReescreveBancoObrassUseCase,ReescreveBancoPessoasUseCase,RequisicaoIdCopiaObraUseCase,RequisicaoIdObraUseCase,RequisicaoIdPessoaUseCase
from pooa.controladores.controllers import ControllerBanco,ControllerObra,ControllerMovimentacao,ControllerUser

ListaDeObras = [] 
ListaDePessoas = [[],[]]

#declaração dos controllers
controllerBanco = ControllerBanco(ReescreveBancoPessoasUseCase,ReescreveBancoObrassUseCase,LeitorBancoPessoaUseCase,LeitorBancoObraUseCase,RequisicaoIdPessoaUseCase,RequisicaoIdObraUseCase,RequisicaoIdCopiaObraUseCase)
controllerPessoa = ControllerUser(ConsultarDisciplinasUseCase,ConsultarGruposAcademicosUseCase,AlterarDadosUsuarioUseCase,ConsultarPendenciasUseCase,ConsultarLeitoresComPendenciasUseCase,RemoverUsuarioUseCase,AdicionarUsuarioUseCase,ValidarUsuarioUseCase)
controllerMovimentacao = ControllerMovimentacao(ReservarObraUseCase,EmprestarObraUseCase,DevolverObraUseCase)
controllerObra = ControllerObra(ConsultarCopiaObraUseCase,ConsultarCopiaObraSituacaoUseCase,RemoverObraUseCase,CadastrarObraUseCase,CadastrarCopiaObraUseCase,AlterarDadosObraUseCase,ListarSituacaoCopiaObraUseCase,ConsultarObrasAtrasadasUseCase)

#inicializa as listas com informações de nosso Banco de Dados
ListaDeObras =  controllerBanco.leitorBancoObras(ListaDeObras)
ListaDePessoas = controllerBanco.leitorBancoPessoas(ListaDePessoas)

#criando obras aleatorias para o teste
livro = Obra('teste','abril',None, 'Yuval Harari', ['Historia', 'cientifico'], datetime.date(2011, 1, 1), 459, 5, None)
copia = CopiaObra(1,1,-1,[1,datetime.date(2013, 1, 1),datetime.date(2013, 1, 1)])#data dummy standard para copias de obras na situação disponível


#ListaDeObras = controllerObra.cadastrarObra(livro,ListaDeObras,controllerBanco.requisicaoIdObra())

#ListaDeObras[len(ListaDeObras)-1].titulo = 'titulo alterado'

#ListaDeObras = controllerObra.alterarDadosObra(ListaDeObras[len(ListaDeObras)-1],ListaDeObras)

#começar o teste de movimentação aqui
#id_em_uso = controllerBanco.requisicaoIdCopiaObra() #em uma situação normal, usariamos diretamente no cadastro da copia, porém, como não teremos o suposto livre em mãos, o id vai ser guardado para a obra ser devolvida

#ListaDeObras[len(ListaDeObras)-1] = controllerObra.cadastrarCopiaObra(ListaDeObras[len(ListaDeObras)-1],copia,id_em_uso)

#ListaDeObras = controllerMovimentacao.reservarObra(ListaDeObras[len(ListaDeObras)-1],ListaDeObras,ListaDePessoas[1][0],ListaDePessoas[0][0])

#controllerObra.listarCopiaObraSituacao(ListaDeObras[len(ListaDeObras)-1],ListaDeObras)

#ListaDeObras = controllerMovimentacao.devolverObra(ListaDeObras[len(ListaDeObras)-1],ListaDeObras,id_em_uso) # copia sendo devolvida para ser devidamente emprestada

#ListaDeObras = controllerMovimentacao.emprestarObra(ListaDeObras[len(ListaDeObras)-1],ListaDeObras,ListaDePessoas[1][0],ListaDePessoas[0][0])

#controllerObra.listarCopiaObraSituacao(ListaDeObras[len(ListaDeObras)-1],ListaDeObras)

#ListaDeObras = controllerMovimentacao.devolverObra(ListaDeObras[len(ListaDeObras)-1],ListaDeObras,id_em_uso) #o id é passado, pois, na ida real, teriamos a copia em mãos na hora da devolução
#Acabar teste de movimentação aqui

#controllerObra.consultarObrasAtrasadas(ListaDeObras,ListaDePessoas)#as informações alem de printadas na tela, são retornadas em uma lista

#controllerObra.removerObra(ListaDeObras[len(ListaDeObras)-1],ListaDeObras)




#inicio do teste com pessoas

leitor2 = UsuarioFactory.build_usuario(TipoUsuario.LEITOR,None,'Valter',41905743950,15061730,datetime.date(2000, 9, 4),17991353055,'valter@ufscar.com','teste',[704030,TipoLeitor.PROFESSOR])

#ListaDePessoas = controllerPessoa.adicionarUsuario(ListaDePessoas,leitor2,RequisicaoIdPessoaUseCase.requisicaoId())

#ListaDePessoas[1][len(ListaDePessoas[1]) -1].nome = 'Professor'

#ListaDePessoas = controllerPessoa.alterarDadosUsuario(ListaDePessoas[1][len(ListaDePessoas[1])-1],ListaDePessoas)

#controllerPessoa.consultarLeitoresComPendencias(ListaDeObras,ListaDePessoas) #alem de printar, retorna as pessoas com pendencias

#print(controllerPessoa.validarUsuario('valter@ufscar.com','teste',ListaDePessoas))

#print(controllerPessoa.validarUsuario('valter@ufscar.com','teste1',ListaDePessoas))
#validações de login, um com as informações certas, outra com as erradas

#print(controllerPessoa.consultarGruposAcademicos(ListaDePessoas[1][len(ListaDePessoas[1])-1]))
#retorna alem do print, True se o usuario estiver inscrito em um grupo, informação que foi pegada da api de outros grupos na criação do usuario

#print(controllerPessoa.consultarDisciplina(ListaDePessoas[1][0]))#foi necessario mudar o usuario, pois professores não possuem o atributo disciplina
#retorna alem do print, True se o usuario estiver inscrito em um grupo, informação que foi pegada da api de outros grupos na criação do usuario

#print(controllerPessoa.consultarPendencias(ListaDePessoas[1][len(ListaDePessoas[1])-1].cpf,ListaDeObras,ListaDePessoas) )
#metodo utilizado em nossa api, retorna True se houverem pendencias e False se não

#ListaDePessoas = controllerPessoa.removerUsuario(ListaDePessoas[1][len(ListaDePessoas[1])-1],ListaDePessoas)


#ao final da execução, as informações latentes são gravadas em nosso banco, as mantendo de forma permanete
controllerBanco.reescreveBancoPessoas(ListaDePessoas)
controllerBanco.reescreveBancoObras(ListaDeObras) 

