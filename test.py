import json
import requests
from src.backEnd.modules.data.credenciais import credenciais

app_key = credenciais['app_key']
app_secret = credenciais['app_secret']
url = 'https://app.omie.com.br/api/v1/geral/clientes/'

#NOTE - listar_clientes
def listar_clientes(pagina: int):
    """
    Função para listar os clientes.
    
    Args:
        pagina (int): O número da página atual.
        total_de_paginas (int): O número total de páginas.
    
    Returns:
        A resposta da requisição feita à API.

    """
    payload = json.dumps({
                            "call": "ListarClientes",
                            "app_key": app_key,
                            "app_secret": app_secret,
                            "param":[
                                        {
                                            "pagina": pagina,
                                            "registros_por_pagina": 500,
                                            "apenas_importado_api": "N"
                                        }
                                    ]
                        })
    headers ={
                'Content-Type': 'application/json'
            }
    response = requests.request("POST", url, headers=headers, data=payload)

    return response

def get_dados_clientes():
    """
    Itera sobre várias páginas para recuperar os dados dos clientes utilizando a função `listar_clientes`.

    Returns:
        Um dicionário contendo os dados dos clientes, onde a chave é a razão social e o valor é um dicionário com os dados do cliente.

    """
    dict_dados_clientes = {}
    pagina = 1
    total_de_paginas = 1
    while pagina <= total_de_paginas:
        response = listar_clientes(pagina=pagina)
        response = response.json()
        clientes_cadastro = response['clientes_cadastro']
        total_de_paginas = int(response['total_de_paginas'])
        for cliente in clientes_cadastro:
            dados_cliente = {}
            dados_cliente['razao_social'] = cliente['razao_social']
            dados_cliente['codigo_cliente_omie'] =  cliente['codigo_cliente_omie']
            dados_cliente['cnpj_cpf'] =  cliente['cnpj_cpf']
            dados_cliente['inscricao_municipal'] =  cliente['inscricao_municipal']
            dados_cliente['endereco'] =  cliente['endereco']
            dados_cliente['endereco_numero'] =  cliente['endereco_numero']
            dados_cliente['bairro'] =  cliente['bairro']
            dados_cliente['cidade'] =  cliente['cidade']

            codigo_cliente_omie = cliente['codigo_cliente_omie']
            dict_dados_clientes[codigo_cliente_omie] = dados_cliente
        pagina = pagina + 1

    return dict_dados_clientes

dict_dados_clientes = get_dados_clientes()

codigo_cliente_omie = '6550693862'

for cliente  in dict_dados_clientes.items():
    codigo_cliente_omie_tupla = str(cliente[0])
    if codigo_cliente_omie_tupla == codigo_cliente_omie:
        dados_cliente = cliente[1]
        razao_social = dados_cliente['razao_social']
        codigo_cliente_omie = dados_cliente['codigo_cliente_omie']
        cnpj_cpf = dados_cliente['cnpj_cpf']
        inscricao_municipal = dados_cliente['inscricao_municipal']
        endereco = dados_cliente['endereco']
        endereco_numero = dados_cliente['endereco_numero']
        bairro = dados_cliente['bairro']
        cidade = dados_cliente['cidade']
        break


