from flask import Flask

titulo = 'Flask Vercel'

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