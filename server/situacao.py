from os import uname
import resource
from flask import Flask
from flask import request
from flask_restplus import Api,Resource
from server.instace import server
from Teste import leitorDeBancoPessoas,leitorDeBancoObras,consultarPendencias
#teste
app, api = server.app, server.api
ListaDeObras = [] 
ListaDePessoas = [[],[]]
leitorDeBancoPessoas(ListaDePessoas)
leitorDeBancoObras(ListaDeObras)
def listaNomesDeObras(listadeobras):
    nomesDeObras = []
    for obras in listadeobras:
        nomesDeObras.append(obras.titulo.strip())
    return nomesDeObras    
@api.route('/situacao',methods=['GET'])
class situacao(Resource):
    def get(self):
        args = request.args.get('cpf')
        return consultarPendencias(str(request.args.get('cpf')).strip())

@api.route('/obras')
class situacao(Resource):
    def get(self):
        return listaNomesDeObras(ListaDeObras)