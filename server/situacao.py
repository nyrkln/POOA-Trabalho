from os import uname
from flask import Flask
from flask import request
from flask_restplus import Api,Resource
from server.instace import server
from pooa.casos_de_uso.banco.use_cases_concrete import LeitorBancoObraUseCase,LeitorBancoPessoaUseCase,ReescreveBancoObrassUseCase,ReescreveBancoPessoasUseCase,RequisicaoIdCopiaObraUseCase,RequisicaoIdObraUseCase,RequisicaoIdPessoaUseCase
from pooa.casos_de_uso.obra.use_cases_concrete import ConsultarCopiaObraUseCase,ConsultarCopiaObraSituacaoUseCase,RemoverObraUseCase,CadastrarObraUseCase,CadastrarCopiaObraUseCase,AlterarDadosObraUseCase,ListarSituacaoCopiaObraUseCase,ConsultarObrasAtrasadasUseCase
from pooa.controladores.controllers import ControllerBanco,ControllerObra, ControllerUser
from pooa.casos_de_uso.pessoas.use_cases_concrete import (AlterarDadosUsuarioUseCase,ConsultarDisciplinasUseCase,ConsultarGruposAcademicosUseCase,ConsultarPendenciasUseCase,ConsultarLeitoresComPendenciasUseCase,RemoverUsuarioUseCase,AdicionarUsuarioUseCase,ValidarUsuarioUseCase)


app, api = server.app, server.api
ListaDeObras = [] 
ListaDePessoas = [[],[]]
controllerBanco = ControllerBanco(ReescreveBancoPessoasUseCase,ReescreveBancoObrassUseCase,LeitorBancoPessoaUseCase,LeitorBancoObraUseCase,RequisicaoIdPessoaUseCase,RequisicaoIdObraUseCase,RequisicaoIdCopiaObraUseCase)
controllerObra = ControllerObra(ConsultarCopiaObraUseCase,ConsultarCopiaObraSituacaoUseCase,RemoverObraUseCase,CadastrarObraUseCase,CadastrarCopiaObraUseCase,AlterarDadosObraUseCase,ListarSituacaoCopiaObraUseCase,ConsultarObrasAtrasadasUseCase)
controllerPessoas = ControllerUser(ConsultarDisciplinasUseCase,ConsultarGruposAcademicosUseCase,AlterarDadosUsuarioUseCase,ConsultarPendenciasUseCase,ConsultarLeitoresComPendenciasUseCase,RemoverUsuarioUseCase,AdicionarUsuarioUseCase,ValidarUsuarioUseCase)

controllerBanco.leitorBancoPessoas(ListaDePessoas)
controllerBanco.leitorBancoObras(ListaDeObras)

def listaNomesDeObras(listadeobras):
    nomesDeObras = []
    for obras in listadeobras:
        nomesDeObras.append(obras.titulo.strip())
    return nomesDeObras    

def consultarPendencias(cpf,listadeobras,listadepessoas):
    identificador = '-1'
    for pessoas in ListaDePessoas[0]:
        if(str(cpf).strip() == str(pessoas.cpf).strip()):
            identificador = str(pessoas.identificador).strip()
    for pessoas in ListaDePessoas[1]:
        if(str(cpf).strip() == str(pessoas.cpf).strip()):
            identificador = str(pessoas.identificador).strip()
    if(identificador == '-1'):
        return False
    for obras in ListaDeObras:
        for copias in obras.copias_obra:
            if (str(copias.locatario).strip() == str(identificador).strip()) and (copias.get_state() == 'Atrasado'):
                return True
    return False            


@api.route('/situacao',methods=['GET'])
class situacao(Resource):
    def get(self):
        args = request.args.get('cpf')
        return controllerPessoas.consultarPendencias(str(request.args.get('cpf')).strip(),ListaDeObras,ListaDePessoas)

@api.route('/obras')
class situacao(Resource):
    def get(self):
        return listaNomesDeObras(ListaDeObras)