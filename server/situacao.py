from os import uname
import resource
from flask import Flask
from flask import request
from flask_restplus import Api,Resource
from server.instace import server
from Teste import leitorDeBancoPessoas,leitorDeBancoObras,consultarPendencias

app, api = server.app, server.api
ListaDeObras = [] 
ListaDePessoas = [[],[]]
leitorDeBancoPessoas(ListaDePessoas)
leitorDeBancoObras(ListaDeObras)

@api.route('/situacao',methods=['GET'])
class situacao(Resource):
    def get(self):
        args = request.args.get('cpf')
        return consultarPendencias(str(request.args.get('cpf')).strip())