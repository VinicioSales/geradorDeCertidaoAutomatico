import os
from flask import Flask, request, render_template
from modules.funcs.funcs import *

template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'frontEnd', 'templates'))

app = Flask(__name__, template_folder=template_dir)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gerar_certidao', methods=['POST'])
def gerar_certidao():
    nome_cliente = request.form.get('nomeCliente')
    script()
    return 'Certidão gerada com sucesso para o cliente: ' + nome_cliente

if __name__ == '__main__':
    app.run(debug=True)
