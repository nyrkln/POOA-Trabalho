import os
from flask import Flask
from flask_restplus import Api
class Server():
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app,version='1.0',
        title='situação da pessoa',
        description='retorna a situação da pessoa',
        doc='/docs')
    def run(self):
        port = int(os.environ.get("PORT",5000))
        self.app.run(
            host = '0.0.0.0',
            debug=True,
            port = port
        )
            
server = Server()        