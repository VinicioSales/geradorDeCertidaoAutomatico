import os
import threading
import webbrowser
from modules.api.google import *
from modules.funcs.funcs import *
from flask import Flask, request, render_template, jsonify

status = get_liberacao()
print(status)

template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'frontEnd', 'templates'))
static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'frontEnd', 'static'))

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

app.secret_key = 'chave_secreta'

dict_codigo_clientes =  get_codigo_clientes()
dict_status_contas_receber_clientes = get_contas_receber_clientes()
dict_dados_clientes = get_dados_clientes()

#NOTE - index
@app.route('/')
def index():
    """
    Rota inicial que retorna a página inicial.

    Returns:
        str: O conteúdo da página inicial.
    """
    return render_template('index.html')

#NOTE - gerar_certidao
@app.route('/gerar_certidao', methods=['POST'])
def gerar_certidao():
    """
    Rota para gerar a certidão.

    Returns:
        dict: O objeto JSON contendo a mensagem de resposta.
    """
    if status == 'liberado':
        razao_social_pesquisado = request.json
        response = script(dict_dados_clientes = dict_dados_clientes, razao_social_pesquisado=razao_social_pesquisado, dict_codigo_clientes=dict_codigo_clientes, dict_status_contas_receber_clientes=dict_status_contas_receber_clientes)
        print(f'response: {response}')
        response = {
            'message': response
        }

        return response
    else:
        response = {
            'message': 'Acesso Negado!'
        }

        return response

#NOTE - get_nome_clientes
@app.route('/get_nome_clientes', methods=['GET'])
def get_nome_clientes():
    """
    Rota para obter a lista de nomes de clientes.

    Returns:
        dict: O objeto JSON contendo a lista de nomes de clientes.
    """
    lista_nome_clientes = get_nome_clientes_func()

    return jsonify(lista_nome_clientes)

if __name__ == '__main__':
    app_thread = threading.Thread(target=app.run, kwargs={'port': 5000})
    app_thread.daemon = True
    app_thread.start()
    webbrowser.open('http://localhost:5000')
    app_thread.join()
