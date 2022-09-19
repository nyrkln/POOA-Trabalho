from distutils.log import debug
from http import server
from flask import Flask
from flask import request
from flask_restplus import Api,Resource
from server.instace import server
#from server.instace import server
#from server.situacao import *
import os 
from Teste import leitorDeBancoPessoas,leitorDeBancoObras,consultarPendencias

server = Flask(__name__)
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
port = int(os.environ.get('PORT', 5000))

if __name__ == '__main__':
#port = int(os.environ.get('PORT', 5000)) 
    server.run(host='0.0.0.0', port=port)
#server.run()