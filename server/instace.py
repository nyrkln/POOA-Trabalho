from flask import Flask
from flask_restplus import Api
import os 
class Server():
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app,version='1.0',
        title='situação da pessoa',
        description='retorna a situação da pessoa',
        doc='/docs')
    def run(self):
        self.app.run(
        debug=True,
        host='0.0.0.0',
        port=int(os.environ.get('PORT', 5000))
        )    
server = Server()        