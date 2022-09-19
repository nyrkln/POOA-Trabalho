from flask import Flask

app = Flask(__name__)
def hello_world():
    return 'teste'