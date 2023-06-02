import os
import threading
import webbrowser
from modules.funcs.funcs import *
from flask import Flask, request, render_template


template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'frontEnd', 'templates'))
static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'frontEnd', 'static'))

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

app.secret_key = 'chave_secreta'

dict_codigo_clientes =  get_codigo_clientes()
dict_status_contas_receber_clientes = get_contas_receber_clientes()
dict_dados_clientes = get_dados_clientes()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gerar_certidao', methods=['POST'])
def gerar_certidao():
    razao_social_pesquisado = request.json
    response = script(dict_dados_clientes = dict_dados_clientes, razao_social_pesquisado=razao_social_pesquisado, dict_codigo_clientes=dict_codigo_clientes, dict_status_contas_receber_clientes=dict_status_contas_receber_clientes)
    print(f'response: {response}')
    response = {
        'message': response
    }

    return response


if __name__ == '__main__':
    app_thread = threading.Thread(target=app.run, kwargs={'port': 5000})
    app_thread.daemon = True
    app_thread.start()
    webbrowser.open('http://localhost:5000')
    app_thread.join()
