from typing import List
from xmlrpc.client import Boolean
from pooa.casos_de_uso.obra.use_cases_concrete import (
    CadastrarObraUseCase,
    ConsultarCopiaObraUseCase,
    AlterarDadosObraUseCase,
    RemoverObraUseCase,
    ConsultarCopiaObraSituacaoUseCase,
    CadastrarCopiaObraUseCase,
    ListarSituacaoCopiaObraUseCase,
    ReservarObraUseCase,
    EmprestarObraUseCase,
    DevolverObraUseCase,
    ConsultarObrasAtrasadasUseCase)

from pooa.casos_de_uso.pessoas.use_cases_concrete import (AlterarDadosUsuarioUseCase, 
    ConsultarDisciplinasUseCase, 
    ConsultarGruposAcademicosUseCase,
    ConsultarPendenciasUseCase,
    ConsultarLeitoresComPendenciasUseCase,
    RemoverUsuarioUseCase,
    AdicionarUsuarioUseCase,
    ValidarUsuarioUseCase)

from pooa.casos_de_uso.banco.use_cases_concrete import (
    ReescreveBancoPessoasUseCase,
    ReescreveBancoObrassUseCase,
    LeitorBancoPessoaUseCase,
    LeitorBancoObraUseCase,
    RequisicaoIdPessoaUseCase,
    RequisicaoIdObraUseCase,
    RequisicaoIdCopiaObraUseCase
)

from pooa.entidades.obra import Obra, CopiaObra

class ControllerObra:
    def __init__(
        self,
        consultar_copia_obra_use_case: ConsultarCopiaObraUseCase,
        consultar_copia_obra_situacao: ConsultarCopiaObraSituacaoUseCase,
        remover_obra_use_case: RemoverObraUseCase,
        cadastrar_obra_use_case: CadastrarObraUseCase,
        cadastrar_copia_obra_use_case: CadastrarCopiaObraUseCase,
        alterar_dados_obra_use_case: AlterarDadosObraUseCase,
        listar_situacao_copia_obra_use_case: ListarSituacaoCopiaObraUseCase,
        consultar_obras_atrasadas_use_case: ConsultarObrasAtrasadasUseCase
    ):
        self._consultar_obras_atrasadas_use_case = consultar_obras_atrasadas_use_case
        self._remover_obra_use_case = remover_obra_use_case
        self._consultar_copia_obra_use_case = consultar_copia_obra_use_case
        self._consultar_copia_obra_situacao = consultar_copia_obra_situacao
        self._cadastrar_obra_use_case = cadastrar_obra_use_case
        self._cadastrar_copia_obra_use_case = cadastrar_copia_obra_use_case
        self._alterar_dados_obra_use_case = alterar_dados_obra_use_case
        self._listar_situacao_copia_obra_use_case = listar_situacao_copia_obra_use_case
    
    def consultarObrasAtrasadas(self,listadeobras,listadepessoas) -> list:
        return self._consultar_obras_atrasadas_use_case.consultarObrasAtrasadas(listadeobras,listadepessoas)

    def consultarCopiaObra(self,obra,id) -> CopiaObra:
        return self._consultar_copia_obra_use_case.consultarCopiaObra(obra,id)

    def consultarCopiaObraSituacao(self,obra,listaDeObras) -> List[int]:
        return self._consultar_copia_obra_situacao.consultarCopiaObraSituacao(obra,listaDeObras)

    def removerObra(self,obra,ListaDeObras) -> list:
        return self._remover_obra_use_case.removerObra(obra,ListaDeObras)

    def cadastrarObra(self,obra,lista,id) -> List:
        return self._cadastrar_obra_use_case.cadastrarObra(obra,lista,id)  

    def cadastrarCopiaObra(self,obra,novaCopia,id) -> Obra:
        return self._cadastrar_copia_obra_use_case.cadastrarCopiaObra(obra,novaCopia,id)

    def alterarDadosObra(self,obra,ListaDeObras) -> bool:
        return self._alterar_dados_obra_use_case.alterarDadosObra(obra,ListaDeObras)

    def listarCopiaObraSituacao(self,obra,listaDeObras) -> list:
        return self._listar_situacao_copia_obra_use_case.listarCopiaObraSituacao(obra,listaDeObras)


class ControllerMovimentacao:
    def __init__(
        self,
        reservar_obra_use_case: ReservarObraUseCase,
        emprestar_obra_use_case: EmprestarObraUseCase,
        devolver_obra_use_case: DevolverObraUseCase
    ):
        self._reservar_obra_use_case = reservar_obra_use_case
        self._emprestar_obra_use_case = emprestar_obra_use_case
        self._devolver_obra_use_case = devolver_obra_use_case

    def reservarObra(self,obra,listaDeObras,locatario,funcionario) -> list:
        self._reservar_obra_use_case.reservarObra(obra,listaDeObras,locatario,funcionario)

    def emprestarObra(self,obra,listaDeObras,locatario,funcionario) -> list:
        self._emprestar_obra_use_case.emprestarObra(obra,listaDeObras,locatario,funcionario)

    def devolverObra(self,obra,listaDeObras,idCopia) -> list:
        self._devolver_obra_use_case.devolverObra(obra,listaDeObras,idCopia)


class ControllerUser:
    def __init__(
        self,
        consultar_disciplinas_use_case: ConsultarDisciplinasUseCase,
        consultar_grupos_academicos_use_case: ConsultarGruposAcademicosUseCase,
        alterar_dados_usuarios_use_case: AlterarDadosUsuarioUseCase,
        consultar_pendencias_use_case: ConsultarPendenciasUseCase,
        consultar_leitores_com_pendencias_use_case: ConsultarLeitoresComPendenciasUseCase,
        remover_usuario_use_case: RemoverUsuarioUseCase,
        adicionar_usuario_use_case: AdicionarUsuarioUseCase,
        validar_usuario_use_case : ValidarUsuarioUseCase
    ):
        self._consultar_disciplinas_use_case = consultar_disciplinas_use_case
        self._consultar_grupos_academicos_use_case = consultar_grupos_academicos_use_case
        self._alterar_dados_usuarios_use_case = alterar_dados_usuarios_use_case
        self._consultar_pendencias_use_case = consultar_pendencias_use_case
        self._consultar_leitores_com_pendencias_use_case = consultar_leitores_com_pendencias_use_case
        self._remover_usuario_use_case = remover_usuario_use_case
        self._adicionar_usuario_use_case = adicionar_usuario_use_case
        self._validar_usuario_use_case = validar_usuario_use_case

    def consultarDisciplina(self,usuario) -> Boolean:
        return self._consultar_disciplinas_use_case.consultarDisciplina(usuario)  # Integração com o grupo 5

    def consultarGruposAcademicos(self,usuario) -> Boolean:
        return self._consultar_grupos_academicos_use_case.consultarGruposAcademicos(usuario)#Integração com o grupo 7

    def alterarDadosUsuario(self,usuario,listaDeUsuarios) -> list:
        return self._alterar_dados_usuarios_use_case.alterarDadosUsuario(usuario,listaDeUsuarios)

    def consultarPendencias(self,cpf,ListaDeObras,ListaDePessoas) -> Boolean:
        return self._consultar_pendencias_use_case.consultarPendencias(cpf,ListaDeObras,ListaDePessoas)    

    def consultarLeitoresComPendencias(self,listadeobras,listadepessoas) -> list:
        return self._consultar_leitores_com_pendencias_use_case.consultarLeitoresComPendencias(listadeobras,listadepessoas)

    def removerUsuario(self,usuario,ListaDeUsuarios) -> list:
        return self._remover_usuario_use_case.removerUsuario(ListaDeUsuarios)   

    def adicionarUsuario(self,ListaDePessoas,pessoa,id) -> list:
        return self._adicionar_usuario_use_case.AdicionarUsuario(ListaDePessoas,pessoa,id) 

    def validarUsuario(self,login,senha,listadepessoas) -> list:
        return self._validar_usuario_use_case.validarUsuario(login,senha,listadepessoas)    


class ControllerBanco:
        def __init__(
        self,
        reescreve_banco_pessoas_use_case: ReescreveBancoPessoasUseCase,
        reescreve_banco_obras_use_case: ReescreveBancoObrassUseCase,
        leitor_banco_pessoa_use_case: LeitorBancoPessoaUseCase,
        leitor_banco_obra_use_case: LeitorBancoObraUseCase,
        requisicao_id_pessoa_use_case: RequisicaoIdPessoaUseCase,
        requisicao_id_obra_use_case: RequisicaoIdObraUseCase,
        requisicao_id_copia_obra_use_case: RequisicaoIdCopiaObraUseCase
    ):
            self._reescreve_banco_pessoas_use_case = reescreve_banco_pessoas_use_case
            self._reescreve_banco_obras_use_case = reescreve_banco_obras_use_case
            self._leitor_banco_pessoa_use_case = leitor_banco_pessoa_use_case
            self._leitor_banco_obra_use_case = leitor_banco_obra_use_case
            self._requisicao_id_pessoa_use_case = requisicao_id_pessoa_use_case
            self._requisicao_id_obra_use_case = requisicao_id_obra_use_case
            self._requisicao_id_copia_obra_use_case = requisicao_id_copia_obra_use_case  
        
        def reescreveBancoPessoas(self,listaDeObjetos: List) -> None:
            return self._reescreve_banco_pessoas_use_case.reescreveBanco(listaDeObjetos)

        def reescreveBancoObras(self,listaDeObjetos: List) -> None:
            return self._reescreve_banco_obras_use_case.reescreveBanco(listaDeObjetos)

        def leitorBancoPessoas(self,listaDeObjetos: List) -> None:
            return self._leitor_banco_pessoa_use_case.leitorBanco(listaDeObjetos)     

        def leitorBancoObras(self,listaDeObjetos: List) -> None:
            return self._leitor_banco_obra_use_case.leitorBanco(listaDeObjetos)

        def requisicaoIdPessoa(self) -> int:
            return self._requisicao_id_pessoa_use_case.requisicaoId()

        def requisicaoIdObra(self) -> int:
            return self._requisicao_id_obra_use_case.requisicaoId()   

        def requisicaoIdCopiaObra(self) -> int:
            return self._requisicao_id_copia_obra_use_case.requisicaoId()   

