from flask import Flask
from ddd import titulo

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'

@app.route('/ddd')
def ddd():
    return f'vem importado - {titulo}'