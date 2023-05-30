from flask import Flask, request, render_template
from modules.funcs.funcs import *

app = Flask(__name__)

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
