import os
from flask import Flask, request, render_template
from modules.funcs.funcs import *

template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'frontEnd', 'templates'))

app = Flask(__name__, template_folder=template_dir, static_folder='frontEnd/static')

dict_codigo_clientes =  get_codigo_clientes()
dict_status_contas_receber_clientes = get_contas_receber_clientes()
dict_dados_clientes = get_dados_clientes()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gerar_certidao', methods=['POST'])
def gerar_certidao():
    razao_social_pesquisado = request.form.get('razaoSocial')
    script(dict_dados_clientes = dict_dados_clientes, razao_social_pesquisado=razao_social_pesquisado, dict_codigo_clientes=dict_codigo_clientes, dict_status_contas_receber_clientes=dict_status_contas_receber_clientes)
    return 'Requisição feita com sucesso para o cliente: ' + razao_social_pesquisado

if __name__ == '__main__':
    app.run(debug=True)
